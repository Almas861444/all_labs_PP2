import psycopg2
import csv

def connect():
    return psycopg2.connect(
        dbname = "phonebook_db",
        user = "postgres",
        password = "Almas200",
        host = "localhost",
        port="5432"
    )

conn = connect()
cur = conn.cursor()

# 1. Insert from CSV
def insert_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook22 (name, phone) VALUES (%s, %s)", (row['name'], row['phone']))
    conn.commit()
    print("Inserted from CSV.")

# 2. Search by pattern (name or phone)
def search_by_pattern():
    keyword = input("Search by (name or phone): ")
    cur.execute("""
    SELECT * FROM phonebook22
    WHERE name ILIKE %s OR phone LIKE %s
    """, ('%' + keyword + '%', '%' + keyword + '%'))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")

# 3. Insert or update user
def insert_or_update_user():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    cur.execute("SELECT * FROM phonebook22 WHERE name = %s", (name,))
    result = cur.fetchone()

    if result:
        cur.execute("UPDATE phonebook22 SET phone = %s WHERE name = %s", (phone, name))
        print("Phone number updated.")
    else:
        cur.execute("INSERT INTO phonebook22 (name, phone) VALUES (%s, %s)", (name, phone))
        print("New user inserted.")

    conn.commit()

# 4. Update both name and phone
def update_data():
    old_name = input("Current name: ")
    new_name = input("New name: ")
    new_phone = input("New phone: ")
    cur.execute("UPDATE phonebook22 SET name = %s, phone = %s WHERE name = %s", (new_name, new_phone, old_name))
    conn.commit()
    print("Updated.")

# 5. Delete by name or phone
def delete_data():
    value = input("Delete by name or phone: ")
    cur.execute("DELETE FROM phonebook22 WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    print("Deleted.")

# 6. Paginated results
def get_paginated():
    limit = int(input("Enter number of records per page: "))
    page = int(input("Enter page number: "))
    offset = limit * (page-1)
    cur.execute("SELECT * FROM phonebook22 LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# 7. Show all records
def show_all():
    cur.execute("SELECT * FROM phonebook22")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert_many_users_directly():
    names = input("Names: ").split(',')
    phones = input("Phones: ").split(',')

    names = [n.strip() for n in names]
    phones = [p.strip() for p in phones]

    if len(names) != len(phones):
        print("Error!")
        return

    invalid = []
    for name, phone in zip(names, phones):
        if phone.isdigit():  # Тек цифрлардан тұруы керек
            cur.execute("INSERT INTO phonebook22 (name, phone) VALUES (%s, %s)", (name, phone))
            print(f"Added contact -> name: {name}, phone: {phone}")
        else:
            invalid.append((name, phone))

    conn.commit()

    if invalid:
        print("\n Error phone:")
        for n, p in invalid:
            print(f"name: {n}, phone: {p}")
    else:
        print("\n All contacts added well.")

   
    conn.commit()
    cur.close()
    conn.close()

def menu():
    while True:
        print("\nPhoneBook Menu")
        print("1. Insert from CSV")
        print("2. Search by pattern")
        print("3. Insert or update user")
        print("4. Update name & phone")
        print("5. Delete by name or phone")
        print("6. Paginated view")
        print("7. Show all")
        print("8. Many contacts")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == '1':
            file_path = input('C:/Users/Алмас/Desktop/Documents/labs_PP2/labs/lab10/aaa.csv')
            insert_from_csv(file_path)
        elif choice == '2':
            search_by_pattern()
        elif choice == '3':
            insert_or_update_user()
        elif choice == '4':
            update_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            get_paginated()
        elif choice == '7':
            show_all()
        elif choice == '8':
            insert_many_users_directly()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()

menu()