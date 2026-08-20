def calculate_average(numbers):
    total = 0

    for n in numbers:
        total += n

    return total / len(numbers)


def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user

    return None


users = [
    {"name": "Jayant", "age": 20},
    {"name": "Alex", "age": 21},
]

print(calculate_average([]))
print(find_user(users, "John")["age"])