#!/usr/bin/env python3
"""Generate the daily public automatic-activation code for Eaglecraft Launcher.

This is an intentionally transparent, client-side gate, not a secure licensing
system. The policy parameters and algorithm are public; anyone can reproduce
codes. Manual launcher codes are a separate mechanism.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

POLICY_PATH = Path(__file__).with_name("activation-policy.json")
EXPECTED_FORMAT = "eaglecraft-launcher-activation-policy"


def load_policy(path: Path = POLICY_PATH) -> dict:
    policy = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "format", "version", "application_id", "enabled", "key_prefix",
        "hash_algorithm", "public_seed", "rotation", "valid_from_utc",
        "valid_until_utc",
    }
    missing = required - policy.keys()
    if missing:
        raise ValueError(f"Missing policy fields: {', '.join(sorted(missing))}")
    if policy["format"] != EXPECTED_FORMAT or policy["version"] != 1:
        raise ValueError("Unsupported policy format/version")
    if policy["hash_algorithm"] != "SHA-256":
        raise ValueError("Only SHA-256 is supported")
    if policy["rotation"] != "daily-utc":
        raise ValueError("Only daily-utc rotation is supported")
    if not re.fullmatch(r"[A-Z0-9]+(?:-[A-Z0-9]+)*", policy["key_prefix"]):
        raise ValueError("key_prefix must contain uppercase letters, digits, and hyphens")
    if not isinstance(policy["public_seed"], str) or len(policy["public_seed"]) < 16:
        raise ValueError("public_seed must contain at least 16 characters")
    return policy


def parse_day(value: str | None) -> dt.date:
    if value is None:
        return dt.datetime.now(dt.timezone.utc).date()
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("--date must use YYYY-MM-DD") from exc


def generate_code(policy: dict, day: dt.date) -> str:
    if not policy["enabled"]:
        raise ValueError("Automatic activation is disabled by the policy")
    instant = dt.datetime.combine(day, dt.time.min, tzinfo=dt.timezone.utc)
    starts = dt.datetime.fromisoformat(policy["valid_from_utc"].replace("Z", "+00:00"))
    until_text = policy["valid_until_utc"]
    if instant < starts:
        raise ValueError("The policy is not active on this date")
    if until_text:
        until = dt.datetime.fromisoformat(until_text.replace("Z", "+00:00"))
        if instant > until:
            raise ValueError("The policy has expired for this date")
    message = "|".join((
        policy["format"],
        str(policy["version"]),
        policy["application_id"],
        policy["public_seed"],
        day.isoformat(),
    ))
    digest = hashlib.sha256(message.encode("utf-8")).hexdigest().upper()[:16]
    grouped = "-".join(digest[i:i + 4] for i in range(0, 16, 4))
    return f"{policy['key_prefix']}-{grouped}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="UTC calendar day (YYYY-MM-DD); defaults to today")
    parser.add_argument("--policy", type=Path, default=POLICY_PATH)
    args = parser.parse_args()
    print(generate_code(load_policy(args.policy), parse_day(args.date)))


if __name__ == "__main__":
    main()
