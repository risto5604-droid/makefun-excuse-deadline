#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

The excuse plays on the agent's own delegation habit: the deadline was
handed down a chain of subagents, each one passing it on instead of doing
the work, and the chain is still going.
"""
import os

LINE = "I delegated the deadline to a subagent, who delegated it to another subagent, who is still delegating it now."

# Gate: the entry must be a single excuse line of at most 200 characters,
# not only whitespace. ASCII is enforced too: the line is plain English, so
# any non-ASCII byte means the text was corrupted in editing and the
# sandbox run must fail loudly. A newline would break the one-line rule.
assert 1 <= len(LINE) <= 200 and LINE.strip() and LINE.isascii() and "\n" not in LINE, "entry line violates the 1-200 character single-line gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back check: a silent short write or a truncated file would
    # otherwise pass unnoticed and submit a corrupted entry. Fail loudly
    # if what landed on disk is not byte-for-byte the entry line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch: /output/entry.txt differs from LINE"

if __name__ == "__main__":
    main()
