import hashlib
import os
import time

def calculate_sha256(filepath):
    """Generates a unique SHA-256 fingerprint for a target file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

target_file = "important_system_file.txt"
# Monitor a local file for unauthorized modifications
script_dir = os.path.dirname(os.path.abspath(__file__))
monitor_dir = os.path.join(script_dir, "fim")
target_file = os.path.join(monitor_dir, "important_system_file.txt")
print(f"Starting FIM baseline for {target_file}...")

# Create file if it doesn't exist for test purposes
os.makedirs(monitor_dir, exist_ok=True)
if not os.path.exists(target_file):
    with open(target_file, "w") as f: f.write("Initial secure configuration state.")

baseline_hash = calculate_sha256(target_file)

try:
    while True:
        time.sleep(5)  # Scan every 5 seconds
        current_hash = calculate_sha256(target_file)
        
        if current_hash is None:
            print("🚨 ALERT: Monitored file has been deleted!")
            break
        elif current_hash != baseline_hash:
            print("🚨 ALERT: File modification detected! Integrity compromised.")
            # Reset baseline to register the new known state or alert endlessly
            baseline_hash = current_hash
        else:
            print("File is secure. No changes detected.")
except KeyboardInterrupt:
    print("Monitoring stopped.")
