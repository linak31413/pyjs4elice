KEYS_REQUIRED  = {"id", "status", "elapsed_ms"}
STATUS_ALLOWED = {"ok", "fail"}

def validate_response(data):
    errors = []
    missing = KEYS_REQUIRED - data.keys()
    if missing:
        errors.append(f"missing={sorted(missing)}")
    if "status" in data and data["status"] not in STATUS_ALLOWED:
        errors.append("invalid-status")
    if "elapsed_ms" in data:
        if not isinstance(data["elapsed_ms"], (int,float)):
            errors.append("elapsed-type")
        elif data["elapsed_ms"] < 0:
            errors.append("elapsed-negative")
    return errors
