jobs = [
    {"customer": "Lee", "service": "Oil change", "bay": 2},
    {"customer": "Ortiz", "service": "Brakes", "bay": 4},
    {"customer": "Shah", "service": "Tires", "bay": 1},
]


def find_customer_service(jobs, customer_name):
    for job in jobs:
        if job["customer"] == customer_name:
            return job["service"]
    return "Not found"

print(find_customer_service(jobs, "Lee"))
print(find_customer_service(jobs, "Shah"))
print(find_customer_service(jobs, "Kim"))

service = find_customer_service(jobs, "Ortiz")

print(f"Ortiz is in for {service}")