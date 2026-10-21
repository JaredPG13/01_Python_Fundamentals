with open("test_note.txt", "r") as file:
    contents = file.read()
lines = contents.splitlines()

print(f"Notes on file: {len(lines)}")
for line in lines:
    print(f"- {line}")
print(f"Most recent note: {lines[-1]}")
