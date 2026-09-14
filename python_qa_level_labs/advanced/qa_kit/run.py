from src.loader import load_cases
from src.validators import validate_response
from src.reporter import save_report

STATUS_PASS = "PASS"
STATUS_FAIL = "FAIL"

results=[]
for tc in load_cases():
    errors=validate_response(tc["actual"])
    results.append({"tc_id"  : tc["tc_id"],
                    "status" : STATUS_PASS if not errors else STATUS_FAIL,
                    "reason" : errors})
    print(results[-1])
save_report(results)
