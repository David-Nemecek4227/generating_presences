import json
import uuid
import random

# Načtení dat ze systemdata.json
with open('systemdata_scrape.json', 'r', encoding='utf-8') as f:
    system_data = json.load(f)

# Zde umístěte váš kód pro generování záznamů events_users
students = [
    {"user_id": "89d1e724-ae0f-11ed-9bd8-0242ac110002"},
    {"user_id": "89d1f34a-ae0f-11ed-9bd8-0242ac110002"},
    {"user_id": "89d1f3cc-ae0f-11ed-9bd8-0242ac110002"},
    {"user_id": "89d1f430-ae0f-11ed-9bd8-0242ac110002"},
    {"user_id": "89d1f48a-ae0f-11ed-9bd8-0242ac110002"},
    {"user_id": "89d1f4e4-ae0f-11ed-9bd8-0242ac110002"},
    {"user_id": "89d1f534-ae0f-11ed-9bd8-0242ac110002"},
    {"user_id": "89d1f58e-ae0f-11ed-9bd8-0242ac110002"},
    {"user_id": "89d1f5de-ae0f-11ed-9bd8-0242ac110002"},
    {"user_id": "89d1f638-ae0f-11ed-9bd8-0242ac110002"}
]

teachers = [
    {"user_id": "2d9dc5ca-a4a2-11ed-b9df-0242ac120003"},
    {"user_id": "2d9dc868-a4a2-11ed-b9df-0242ac120003"},
    {"user_id": "2d9dc9a8-a4a2-11ed-b9df-0242ac120003"},
    {"user_id": "2d9dcbec-a4a2-11ed-b9df-0242ac120003"}
]

student_groups = [
    {"groups_id": "9baf3b54-ae0f-11ed-9bd8-0242ac110002"},
    {"groups_id": "9baf3d70-ae0f-11ed-9bd8-0242ac110002"},
    {"groups_id": "9baf3de8-ae0f-11ed-9bd8-0242ac110002"},
    {"groups_id": "9baf3e42-ae0f-11ed-9bd8-0242ac110002"},
    {"groups_id": "9baf3e92-ae0f-11ed-9bd8-0242ac110002"},
    {"groups_id": "9baf3eec-ae0f-11ed-9bd8-0242ac110002"},
    {"groups_id": "9baf3f3c-ae0f-11ed-9bd8-0242ac110002"},
    {"groups_id": "9baf3f96-ae0f-11ed-9bd8-0242ac110002"},
    {"groups_id": "9baf3fe6-ae0f-11ed-9bd8-0242ac110002"},
    {"groups_id": "9baf4040-ae0f-11ed-9bd8-0242ac110002"}
]

events = system_data['events']
eventpresencetypes = system_data['eventpresencetypes']

# Příprava seznamů pro nové záznamy
new_events_users = []
new_event_groups = []

# Iterace přes každou událost
for event in events:
    # Vybrání jednoho učitele, tří studentů a jedné skupiny pro každou událost
    selected_teacher = random.choice(teachers)
    selected_students = random.sample(students, 3)
    selected_group = random.choice(student_groups)

    # Vytvoření záznamu pro učitele
    attendance_teacher = random.choice(eventpresencetypes)
    teacher_record_id = str(uuid.uuid4())
    new_events_users.append({
        "id": teacher_record_id,
        "user_id": selected_teacher['user_id'],
        "event_id": event['id'],
        "invitation_id": "e8713b6e-a79c-11ed-b76e-0242ac110002",  # přidělené invitation_id pro učitele
        "presencetype_id": attendance_teacher['id']
    })

    # Vytvoření záznamů pro studenty
    for student in selected_students:
        attendance_student = random.choice(eventpresencetypes)
        student_record_id = str(uuid.uuid4())
        new_events_users.append({
            "id": student_record_id,
            "user_id": student['user_id'],
            "event_id": event['id'],
            "invitation_id": "e8713f06-a79c-11ed-b76e-0242ac110002",  # přidělené invitation_id pro studenty
            "presencetype_id": attendance_student['id']
        })

    # Vytvoření záznamu pro skupinu
    new_event_groups.append({
        "id": str(uuid.uuid4()),
        "group_id": selected_group['groups_id'],
        "event_id": event['id']
    })

# Přidání nových záznamů do existujících seznamů events_users a event_groups
if 'events_users' not in system_data:
    system_data['events_users'] = []
if 'event_groups' not in system_data:
    system_data['event_groups'] = []

system_data['events_users'].extend(new_events_users)
system_data['event_groups'].extend(new_event_groups)

# Uložení aktualizovaných dat zpět do systemdata.json
with open('systemdata.json', 'w', encoding='utf-8') as f:
    json.dump(system_data, f, indent=4, sort_keys=False)

print("Nové záznamy byly úspěšně přidány do systemdata.json")
