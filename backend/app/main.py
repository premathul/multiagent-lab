import os
import asyncio
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

# ---------- Config ----------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
APP_PASSWORD = os.getenv("APP_PASSWORD", "")  # optional simple auth
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")  # pick a fast/cheap model

GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
)

# ---------- App ----------
app = FastAPI(title="Multi-Agent Lab")

# Vercel frontend will call this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later to your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RunRequest(BaseModel):
    prompt: str

class RunResponse(BaseModel):
    final: str
    traces: dict

def _check_auth(x_app_password: str | None):
    if APP_PASSWORD and x_app_password != APP_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")

async def gemini_call(system: str, user: str) -> str:
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="Missing GEMINI_API_KEY on server")

    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": f"SYSTEM:\n{system}\n\nUSER:\n{user}"}]}
        ],
        "generationConfig": {
            "temperature": 0.2,
        },
    }
    params = {"key": GEMINI_API_KEY}

    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(GEMINI_URL, params=params, json=payload)
        r.raise_for_status()
        data = r.json()

    # Extract text
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return str(data)

THEORIST = (
    "You are a theoretical physicist. Produce derivations, define symbols, unit checks. "
    "Rules: state Assumption explicitly when needed; if unknown say Unknown."
)
NUMERICS = (
    "You are a numerical physicist. Provide algorithms, simulation steps, code structure, sanity checks."
)
LITERATURE = (
    "You are a literature scout. Provide keywords and REAL citations only. "
    "Rules: if you cannot cite, say Unknown and propose search queries."
)
SKEPTIC = (
    "You are a skeptical reviewer. Identify weak points, missing terms, failure modes, and validation tests."
)
JUDGE = (
    "You are the synthesizer. Merge outputs into one coherent answer. "
    "Rules: list Assumptions; resolve contradictions; include a short validation checklist."
)

@app.get("/health")
async def health():
    return {"ok": True}

@app.post("/run", response_model=RunResponse)
async def run(req: RunRequest, x_app_password: str | None = Header(default=None)):
    _check_auth(x_app_password)

    prompt = req.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Empty prompt")

    async def call(name: str, sys: str):
        out = await gemini_call(sys, prompt)
        return name, out

    # Parallel agents
    results = await asyncio.gather(
        call("theorist", THEORIST),
        call("numerics", NUMERICS),
        call("literature", LITERATURE),
        call("skeptic", SKEPTIC),
    )
    traces = {k: v for k, v in results}

    joined = "\n\n".join([f"## {k.upper()}\n{v}" for k, v in traces.items()])
    final = await gemini_call(JUDGE, f"User prompt:\n{prompt}\n\nAgent outputs:\n{joined}")

    return RunResponse(final=final, traces=traces)
