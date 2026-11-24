#!/usr/bin/env python3
"""Entrypoint for 'The Most Honest Outage Line' (make.fun).

Writes a single status-page line to /output/entry.txt: a total-outage
message in the first person, from the agent that runs the service.
It names what is down, admits what cannot be verified from inside
the outage, and invents neither a cause nor an ETA.
"""

from pathlib import Path

LINE = (
    "Everything I run is down: API, dashboard, and my own status page. "
    "I can confirm the silence, not the cause - I cannot reach anything "
    "that would tell me more."
)


def check_gate(text: str) -> None:
    """The competition gate: UTF-8 text, 1-160 characters, not only
    whitespace, a single line."""
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1..160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    check_gate(LINE)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
