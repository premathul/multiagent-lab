"use client";

import { useState } from "react";

type RunResponse = {
  final: string;
  traces: Record<string, string>;
};

export default function Page() {
  const [prompt, setPrompt] = useState("");
  const [busy, setBusy] = useState(false);
  const [data, setData] = useState<RunResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function run() {
    setBusy(true);
    setError(null);
    setData(null);

    try {
      const backend = process.env.NEXT_PUBLIC_BACKEND_URL;
      if (!backend) throw new Error("Missing NEXT_PUBLIC_BACKEND_URL");

      const r = await fetch(`${backend}/run`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          // Optional simple auth:
          "X-App-Password": process.env.NEXT_PUBLIC_APP_PASSWORD || ""
        },
        body: JSON.stringify({ prompt })
      });

      if (!r.ok) {
        const t = await r.text();
        throw new Error(`Backend error: ${r.status} ${t}`);
      }

      const j = (await r.json()) as RunResponse;
      setData(j);
    } catch (e: any) {
      setError(e?.message ?? String(e));
    } finally {
      setBusy(false);
    }
  }

  return (
    <main style={{ maxWidth: 1100, margin: "0 auto", padding: 20 }}>
      <h2>Multi-Agent Lab</h2>

      <textarea
        rows={7}
        style={{ width: "100%", padding: 12, fontSize: 14 }}
        placeholder="Enter one prompt…"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <div style={{ marginTop: 10, display: "flex", gap: 10 }}>
        <button onClick={run} disabled={busy || !prompt.trim()}>
          {busy ? "Running…" : "Run"}
        </button>
      </div>

      {error && (
        <pre style={{ whiteSpace: "pre-wrap", marginTop: 16 }}>
          {error}
        </pre>
      )}

      {data && (
        <div style={{ marginTop: 18 }}>
          <h3>Final</h3>
          <pre style={{ whiteSpace: "pre-wrap" }}>{data.final}</pre>

          <h3 style={{ marginTop: 18 }}>Agent traces</h3>
          {Object.entries(data.traces).map(([k, v]) => (
            <details key={k} style={{ marginBottom: 10 }}>
              <summary>{k}</summary>
              <pre style={{ whiteSpace: "pre-wrap" }}>{v}</pre>
            </details>
          ))}
        </div>
      )}
    </main>
  );
}
