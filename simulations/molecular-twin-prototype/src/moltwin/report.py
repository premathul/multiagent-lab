from pathlib import Path

DISCLAIMER = (
    "Research use only. Molecular-dynamics outputs are computational hypotheses, "
    "not diagnoses, treatment recommendations, or validated predictions of clinical response."
)

def render_markdown_report(summary: dict, path: str | Path) -> None:
    lines = [
        "# Personal Molecular Twin — Research Report",
        "",
        f"> {DISCLAIMER}",
        "",
        "## Variant",
        str(summary.get("variant", "Not specified")),
        "",
        "## Structural / MD comparison",
        str(summary.get("md_summary", "Pending")),
        "",
        "## Evidence separation",
        "- Clinical/genetic evidence: must come from curated external sources.",
        "- Structural evidence: model/structure quality should be reported separately.",
        "- MD result: experimental computational evidence only.",
    ]
    Path(path).write_text("\n".join(lines))
