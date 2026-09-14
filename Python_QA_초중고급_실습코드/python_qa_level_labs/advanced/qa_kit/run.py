from src.loader import load_cases
from src.validators import validate_response
from src.reporter import save_report

results=[]
for tc in load_cases():
    errors=validate_response(tc["actual"])
    results.append({"tc_id":tc["tc_id"],"status":"PASS" if not errors else "FAIL","reason":errors})
    print(results[-1])
save_report(results)
