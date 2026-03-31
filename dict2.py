wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def find_job(guy):
    staff = {}
    for key, value in wards.items():
        
user_person = input("What person do you want to know about?")
print(find_job(user_person))