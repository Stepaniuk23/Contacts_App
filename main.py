from contacts import (
    add_contact, find_contact, delete_contact,
    update_contact, list_contacts, load_contacts)



def main():
    load_contacts()
    while True:
        print("\n📋 Меню:")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Удалить контакт")
        print("4. Обновить контакт")
        print("5. Просмотреть все контакты")
        print("6. Выйти")

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            name = input("Введите имя: ")
            phone = input("Введите телефон (12 цифр): ")
            email = input("Введите email: ")
            add_contact(name, phone, email)

        elif choice == "2":
            query = input("Введите имя или телефон для поиска: ")
            find_contact(query)

        elif choice == "3":
            query = input("Введите имя или телефон для удаления: ")
            delete_contact(query)

        elif choice == "4":
            query = input("Введите имя или телефон для обновления: ")
            new_name = input("Введите новое имя: ")
            new_phone = input("Введите новый телефон (12 цифр): ")
            new_email = input("Введите новый email: ")
            update_contact(query, new_name, new_phone, new_email)

        elif choice == "5":
            list_contacts()

        elif choice == "6":
            print("👋 Выход из программы.")
            break

        else:
            print("❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()