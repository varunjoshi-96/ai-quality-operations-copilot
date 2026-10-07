"""Minimal runnable contract for the AI Quality Operations Copilot.

This is a deterministic project skeleton only. Production LLM/RAG behavior is
intentionally out of scope for T003 and will be added in later tasks.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class CopilotResult:
    classification: str
    reason: str
    evidence_step: str


def classify_ticket(ticket_text: str) -> CopilotResult:
    """Return a deterministic placeholder classification and evidence step."""
    if not isinstance(ticket_text, str) or not ticket_text.strip():
        raise ValueError("ticket_text must be a non-empty string")

    text = ticket_text.lower()
    if any(term in text for term in ("refund", "unauthorized", "chargeback")):
        return CopilotResult(
            classification="high_risk_review",
            reason="Ticket contains a financial-risk signal requiring review.",
            evidence_step="SOP-04",
        )
    if any(term in text for term in ("login", "password", "access denied")):
        return CopilotResult(
            classification="access_issue",
            reason="Ticket contains an authentication or access signal.",
            evidence_step="SOP-02",
        )
    return CopilotResult(
        classification="standard_review",
        reason="No configured high-risk or access keyword was detected.",
        evidence_step="SOP-01",
    )


def classify_ticket_dict(ticket_text: str) -> dict[str, str]:
    """Return the contract as a JSON-serializable dictionary."""
    return asdict(classify_ticket(ticket_text))
