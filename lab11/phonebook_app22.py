import psycopg2
import csv

conn = psycopg2.connect(
    dbname = "phonebook_db",
    user = "postgres",
    password = "Almas200",
    host = "localhost",
    port = "5432"
)

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
    page = int(input("Enter page number (starting from 0): "))
    offset = limit * page
    cur.execute("SELECT * FROM phonebook22 get_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# 7. Show all records
def show_all():
    cur.execute("SELECT * FROM phonebook22")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Menu
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
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()

menu()