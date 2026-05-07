# scripts/simulate_leak.py
# WARNING: This file contains FAKE secrets for portfolio/demo purposes only.
# These credentials are not real and have never been used.

import os

# Simulated leaked AWS credentials (FAKE)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Simulated leaked GitHub token (FAKE)
GITHUB_TOKEN = "ghp_FAKE1234567890abcdefghijklmnopqrstuv"

# Simulated leaked Stripe key (FAKE)
STRIPE_SECRET_KEY = "sk_live_FAKE1234567890abcdefghij"

def main():
    print("Simulating application startup...")
    print(f"Connecting with key: {AWS_ACCESS_KEY_ID[:8]}...")
    print("This file exists to demonstrate secret detection tools.")
    print("In a real scenario, these would be detected and blocked.")

if __name__ == "__main__":
    main()