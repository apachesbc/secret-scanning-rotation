# scripts/simulate_leak.py
# WARNING: This file contains FAKE secrets for portfolio/demo purposes only.
# These credentials are not real and have never been used.

# Simulated leaked private key (FAKE)
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2a2rwplBQLF29amygykEMmYz0+Kcj3bKBp29Po3KXHP+PnAf
mNGGOqWWDoqjEXpMlCEFDGaUlMcFMRcOSJmIaGRBtCMmMmMmMmMmMmMmMmMmMmM
-----END RSA PRIVATE KEY-----"""

# Simulated leaked database URL (FAKE)
DATABASE_URL = "postgresql://admin:SuperSecret123@prod-db.example.com:5432/myapp"

def main():
    print("Simulating application startup...")
    print("This file exists to demonstrate secret detection tools.")

if __name__ == "__main__":
    main()
