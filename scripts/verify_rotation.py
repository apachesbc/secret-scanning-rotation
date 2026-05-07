import os
import re
import sys

SCAN_DIRS = ["scripts", ".github"]
SKIP_FILES = {"simulate_leak.py", "verify_rotation.py", "rotate_secret.py"}
PATTERNS = [
    r"AKIA" + r"IOSFODNN7EXAMPLE",
    r"wJalrXUtnFEMI",
    r"ghp_FAKE1234567890",
    r"sk_live_FAKE1234",
]

def scan_file(filepath):
    hits = []
    try:
        with open(filepath, "r", errors="ignore") as f:
            content = f.read()
        for pattern in PATTERNS:
            if re.search(pattern, content):
                hits.append(f"  WARNING: Pattern found in {filepath}")
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
    return hits

def main():
    print("\nRunning rotation verification scan...")
    all_hits = []
    for scan_dir in SCAN_DIRS:
        if not os.path.exists(scan_dir):
            continue
        for root, _, files in os.walk(scan_dir):
            for fname in files:
                if fname in SKIP_FILES:
                    continue
                all_hits.extend(scan_file(os.path.join(root, fname)))
    if all_hits:
        print("\nROTATION VERIFICATION FAILED - Leaked patterns still present:")
        for hit in all_hits:
            print(hit)
        sys.exit(1)
    else:
        print("ROTATION VERIFICATION PASSED - No leaked patterns detected outside demo files.")
        sys.exit(0)

if __name__ == "__main__":
    main()
