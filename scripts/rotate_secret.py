import datetime
import secrets

ROTATION_LOG = "rotation_audit.log"
OLD_KEY_DEMO = "AKIA" + "IOSFODNN7EXAMPLE"

def log(msg):
    timestamp = datetime.datetime.utcnow().isoformat()
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(ROTATION_LOG, "a") as f:
        f.write(line + "\n")

def simulate_revoke(key_id):
    log(f"STEP 1 - DETECT:  Leaked key identified: {key_id[:8]}...REDACTED")
    log(f"STEP 2 - REVOKE:  Sending revocation request to AWS IAM (simulated)")
    log(f"STEP 2 - REVOKE:  Key {key_id[:8]}... status -> INACTIVE")

def generate_new_secret():
    new_key_id = "AKIA" + secrets.token_hex(8).upper()
    new_secret = secrets.token_urlsafe(40)
    log(f"STEP 3 - ROTATE:  New key generated: {new_key_id[:8]}...REDACTED")
    log(f"STEP 3 - ROTATE:  New secret: [REDACTED - stored in Secrets Manager]")
    return new_key_id, new_secret

def update_secret_store(key_id, secret):
    log(f"STEP 4 - UPDATE:  Writing to AWS Secrets Manager (simulated)")
    log(f"STEP 4 - UPDATE:  Rotation complete. New key: {key_id[:8]}...REDACTED")

def verify_new_secret(key_id):
    log(f"STEP 5 - VERIFY:  Testing new credentials against AWS STS (simulated)")
    log(f"STEP 5 - VERIFY:  Response: 200 OK - Identity confirmed")
    log(f"STEP 5 - VERIFY:  Rotation SUCCESSFUL")

if __name__ == "__main__":
    print("\n" + "="*55)
    print("  SECRET ROTATION WORKFLOW - SIMULATION")
    print("="*55 + "\n")
    simulate_revoke(OLD_KEY_DEMO)
    new_key_id, new_secret = generate_new_secret()
    update_secret_store(new_key_id, new_secret)
    verify_new_secret(new_key_id)
    print(f"\nAudit log written to: {ROTATION_LOG}\n")
