statuses = [200, 200, 404, 500]
pass_count = 0
for status in statuses:
    if status == 200:
        pass_count += 1
        print(status, "PASS")
    else:
        print(status, "FAIL")
print("PASS count:", pass_count)
