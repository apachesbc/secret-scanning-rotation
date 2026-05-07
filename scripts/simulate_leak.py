# scripts/simulate_leak.py
# WARNING: This file contains FAKE secrets for portfolio/demo purposes only.
# These credentials are not real and have never been used.

import os

# Simulated leaked AWS credentials (FAKE)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLEX"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Simulated leaked GitHub token (FAKE)
GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ012345678"

# Simulated leaked Stripe key (FAKE)
STRIPE_SECRET_KEY = "sk_live_aBcDeFgHiJkLmNoPqRsTuVwXy"

def main():
    print("Simulating application startup...")
    print("This file exists to demonstrate secret detection tools.")

if __name__ == "__main__":
    main()
