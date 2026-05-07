# Secret Scanning & Rotation Pipeline

Portfolio project demonstrating enterprise-grade secret detection and rotation workflows using GitLeaks, TruffleHog, pre-commit hooks, and GitHub Actions.

## What This Project Does

| Layer | Tool | Purpose |
|---|---|---|
| Local scan | GitLeaks | Scans git history for leaked secrets |
| Local scan | TruffleHog | Deep entropy and pattern scanning |
| Pre-commit | GitLeaks hook | Blocks secrets before they are committed |
| CI/CD | GitHub Actions | Automated scanning on every push and PR |
| Rotation | Custom Python | Simulates detect, revoke, rotate, verify |

## Tools and Stack

- GitLeaks v8 — pattern-based secret scanning
- TruffleHog v3 — entropy and verified credential scanning
- pre-commit — git hook framework
- GitHub Actions — CI/CD automation
- Python 3.13 — rotation simulation scripts
- AWS IAM and Secrets Manager — rotation target (simulated)

## Running Locally

```bash
gitleaks detect --source . --verbose
trufflehog git file://$(pwd) --no-verification
python3 scripts/rotate_secret.py
python3 scripts/verify_rotation.py
```

## Key Security Concepts Demonstrated

1. Defence in depth — multiple scanning layers (local and CI/CD)
2. Shift-left security — catching secrets at commit time, not after push
3. Audit logging — every rotation event timestamped
4. Least privilege — rotation scoped to specific key only
5. Zero-trust — new credentials verified before old ones fully retired
