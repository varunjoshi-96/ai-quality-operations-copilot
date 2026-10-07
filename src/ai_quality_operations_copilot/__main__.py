from __future__ import annotations

import json
import sys

from .copilot import classify_ticket_dict


def main() -> int:
    ticket = " ".join(sys.argv[1:]).strip()
    if not ticket:
        print('Usage: python -m ai_quality_operations_copilot "<ticket text>"')
        return 2
    print(json.dumps(classify_ticket_dict(ticket), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
