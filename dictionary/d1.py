student_data = {
    "id1": {"name": "Jim", "class": "V", "subject integration": "Reading, Math, Science"},
    "id2": {"name": "Bob", "class": "V", "subject integration": "Reading, Math, Science"},
    "id3": {"name": "Joe", "class": "V", "subject integration": "Reading, Math, Science"},
}

result = {}
seen = set()

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject integration"])
    if unique_key not in seen:
        seen.add(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)