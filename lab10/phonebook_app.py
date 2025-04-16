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

# CSV
def insert_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook22 (name, phone) VALUES (%s, %s)", (row['name'], row['phone']))
    conn.commit()
    print("Inserted from CSV.")

# From Input
def insert_from_input():
    name = input("insert name: ")
    phone = input("insert phone: ")
    cur.execute("INSERT INTO phonebook22 (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Inserted.")

# Update
def update_data():
    name = input("Updated? name: ")
    new_name = input("New name: ")
    new_phone = input("New phone: ")
    cur.execute("UPDATE phonebook22 SET name = %s, phone = %s WHERE name = %s", (new_name, new_phone, name))
    conn.commit()
    print("Updated")

# Search
def search_data():
    filter_name = input("Search? name: ")
    cur.execute("SELECT * FROM phonebook22 WHERE name LIKE %s OR phone LIKE %s", (f'%{filter_name}%', f'%{filter_name}%'))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Didn't find.")

# Delete
def delete_data():
    name = input("Delete? name: ")
    cur.execute("DELETE FROM phonebook22 WHERE name = %s", (name,))
    conn.commit()
    print("Deleted.")

# see all
def show_all():
    cur.execute("SELECT * FROM phonebook22")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def menu():
    while True:
        print("\n Phone_Book")
        print("1. from CSV")
        print("2. from input")
        print("3. update")
        print("4. search")
        print("5. delete")
        print("6. see all")
        print("0. EXIT")

        choice = input("Choose: ")

        if choice == '1':
            insert_from_csv('aaa.csv')  # CSV файлы сол папкада болуы керек
        elif choice == '2':
            insert_from_input()
        elif choice == '3':
            update_data()
        elif choice == '4':
            search_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            show_all()
        elif choice == '0':
            break
        else:
            print("Wrong choice!")


    cur.close()
    conn.close()


menu()