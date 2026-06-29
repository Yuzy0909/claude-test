import os
import json
from datetime import datetime


class UserManager:
    def __init__(self):
        self.users = {}
        self.db_path = "users.json"
        self.load()

    def load(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, "r") as f:
                self.users = json.load(f)

    def save(self):
        with open(self.db_path, "w") as f:
            json.dump(self.users, f)

    def add_user(self, name, email, password):
        if email in self.users:
            return False
        self.users[email] = {
            "name": name,
            "email": email,
            "password": password,  # stored as plain text
            "created_at": str(datetime.now()),
            "active": True,
        }
        self.save()
        return True

    def authenticate(self, email, password):
        user = self.users.get(email)
        if user and user["password"] == password:
            return user
        return None

    def get_all_users(self):
        return list(self.users.values())

    def delete_user(self, email):
        if email in self.users:
            del self.users[email]
            self.save()
            return True
        return False

    def search_users(self, query):
        results = []
        for user in self.users.values():
            if query in user["name"] or query in user["email"]:
                results.append(user)
        return results


def calculate_stats(numbers):
    total = 0
    for n in numbers:
        total = total + n
    avg = total / len(numbers)

    sorted_nums = sorted(numbers)
    min_val = sorted_nums[0]
    max_val = sorted_nums[-1]

    return {
        "total": total,
        "average": avg,
        "min": min_val,
        "max": max_val,
        "count": len(numbers)
    }


def process_data(data):
    result = []
    for item in data:
        try:
            val = int(item)
            result.append(val)
        except:
            pass
    return calculate_stats(result)


if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("Alice", "alice@example.com", "password123")
    manager.add_user("Bob", "bob@example.com", "qwerty")

    user = manager.authenticate("alice@example.com", "password123")
    print(f"Logged in: {user['name']}")

    raw = ["1", "2", "abc", "4", "5"]
    stats = process_data(raw)
    print(f"Stats: {stats}")
