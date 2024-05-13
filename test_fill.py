import json
import uuid
import random

# Seznam uživatelů z vašeho systému
users = [
    {"name": "John", "surname": "Newbie", "email": "john.newbie@world.com"},
    {"name": "Julia", "surname": "Newbie", "email": "julia.newbie@world.com"},
    {"name": "Johnson", "surname": "Newbie", "email": "johnson.newbie@world.com"},
    {"name": "Jepeto", "surname": "Newbie", "email": "jepeto.newbie@world.com"},
    {"name": "Jana", "surname": "Newbie", "email": "jana.newbie@world.com"},
    {"name": "Jolana", "surname": "Newbie", "email": "jolana.newbie@world.com"},
    {"name": "Jitka", "surname": "Newbie", "email": "jitka.newbie@world.com"},
    {"name": "Jaroslava", "surname": "Newbie", "email": "jaroslava.newbie@world.com"},
    {"name": "Lada", "surname": "Newbie", "email": "lada.newbie@world.com"},
    {"name": "Ludmila", "surname": "Newbie", "email": "ludmila.newbie@world.com"},
    {"name": "Lucie", "surname": "Newbie", "email": "lucie.newbie@world.com"},
    {"name": "Nola", "surname": "Newbie", "email": "nola.newbie@world.com"},
    {"name": "Neva", "surname": "Newbie", "email": "neva.newbie@world.com"},
    {"name": "Nora", "surname": "Newbie", "email": "nora.newbie@world.com"}
]

# Vytvoření datové struktury pro vyučování s náhodnou přítomností studentů
vyucovani = []

for i in range(1):  # Počet vyučovacích hodin
    vyucovalny_predmet = "Matematika"  # Předmět
    datum = "2024-05-13"  # Datum

    # Náhodná přítomnost studentů
    studenti = []
    for user in users:
        studenti.append({"id": str(uuid.uuid4()), "name": user["name"], "surname": user["surname"], "email": user["email"], "pritomen": random.choice([True, False])})

    vyucovani.append({"predmet": vyucovalny_predmet, "datum": datum, "studenti": studenti})

# Vytvoření celkové datové struktury
data = {"vyucovani": vyucovani}

# Uložení dat do nového JSON souboru
with open("test.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data byla úspěšně uložena do souboru 'test.json'.")
