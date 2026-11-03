item = {"product_name": "Milk", "quantity": 5, "reorder_level": 2, "shelf_location": "D2"}
print(f"{item['product_name']}: {item['quantity']} on shelf {item['shelf_location']}")
if item["quantity"] <= item["reorder_level"]:
    print(f"REORDER: {item['product_name']} is down to {item['quantity']} (reorder level {item['reorder_level']})")

appointment = {
    "patient_name": "Luis Ortega",
    "doctor": "Dr. Patel",
    "time": "10:30 AM",
    "copay": 25,
}
print(f"{appointment['patient_name']} sees {appointment['doctor']} at {appointment['time']}. Copay: ${appointment['copay']}")