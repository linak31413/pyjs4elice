def validate_response(data):
    errors = []
    required = {"id", "status", "elapsed_ms"}
    missing = required - data.keys()
    if missing:
        errors.append(f"missing={sorted(missing)}")
    if "status" in data and data["status"] not in {"ok", "fail"}:
        errors.append("invalid-status")
    if "elapsed_ms" in data:
        if not isinstance(data["elapsed_ms"], (int, float)):
            errors.append("elapsed-type")
        elif data["elapsed_ms"] < 0:
            errors.append("elapsed-negative")
    return errors
