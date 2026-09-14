def check_status(actual, expected=200):
    return actual == expected

test_cases = [
    {"id":"TC-001","actual":200,"expected":200},
    {"id":"TC-002","actual":404,"expected":200},
]
for tc in test_cases:
    passed = check_status(tc["actual"], tc["expected"])
    print(tc["id"], "PASS" if passed else "FAIL")
