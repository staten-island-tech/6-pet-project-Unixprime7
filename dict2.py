wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def find_job(guy):
    staff = {}
    for key, value in wards.items():
        for people in value:
            staff[people] = [key]
            if guy == people:
                return staff[people]
user_person = input("What person do you want to know about?")
print(find_job(user_person))