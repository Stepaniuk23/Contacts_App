import os

contacts = []

def load_contacts():
    if not os.path.exists("contacts.txt"):
        open("contacts.txt", "w").close()
        return
    with open("contacts.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == 3:
                name, phone, email = parts
                contacts.append({"name": name, "phone": phone, "email": email})

def save_contacts():
    with open("contacts.txt", "w", encoding="utf-8") as f:
        for c in contacts:
            line = f"{c['name']};{c['phone']};{c['email']}\n"
            f.write(line)


def add_contact(name, phone, email):
    if not name or not phone or not email:
        print("❌ Данные не могут быть пустыми.")
        return
    if not phone.isdigit() or len(phone) != 12:
        print("❌ Телефон должен содержать ровно 12 цифр.")
        return
    if "@" not in email or "." not in email:
        print("❌ Email некорректный.")
        return

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts()
    print("✅ Контакт успешно добавлен!")


def find_contact(query):
    results = []
    for c in contacts:
        if c["name"] == query or c["phone"] == query:
            results.append(c)
    if not results:
        print("❌ Контактов не найдено.")
    else:
        print("✅ Найденные контакты:")
        for c in results:
            print(c)


def delete_contact(query):
    deleted_count = 0
    remaining = []
    for c in contacts:
        if c["name"] == query or c["phone"] == query:
            deleted_count += 1
        else:
            remaining.append(c)
    contacts[:] = remaining
    save_contacts()
    if deleted_count == 0:
        print("❌ Контактов для удаления не найдено.")
    else:
        print(f"✅ Удалено контактов: {deleted_count}")


def update_contact(query, new_name, new_phone, new_email):
    updated_count = 0
    for c in contacts:
        if c["name"] == query or c["phone"] == query:
            if not new_name or not new_phone or not new_email:
                print("❌ Новые данные не могут быть пустыми.")
                return
            if not new_phone.isdigit() or len(new_phone) != 12:
                print("❌ Телефон должен содержать ровно 12 цифр.")
                return
            if "@" not in new_email or "." not in new_email:
                print("❌ Email некорректный.")
                return
            c["name"] = new_name
            c["phone"] = new_phone
            c["email"] = new_email
            updated_count += 1
    save_contacts()
    if updated_count == 0:
        print("❌ Контактов для обновления не найдено.")
    else:
        print(f"✅ Обновлено контактов: {updated_count}")


def list_contacts():
    if not contacts:
        print("❌ Список контактов пуст.")
        return
    sorted_contacts = sorted(contacts, key=lambda c: c["name"])
    print("📒 Все контакты:")
    for c in sorted_contacts:
        print(c)