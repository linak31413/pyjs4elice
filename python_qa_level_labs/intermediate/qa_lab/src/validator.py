def is_valid_status(actual, expected):
    return actual == expected

def is_fast_enough(elapsed_ms, limit_ms=1000):
    return elapsed_ms <= limit_ms
