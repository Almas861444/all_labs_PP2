import os
import string


#1
path = r"C:\Users\Алмас\Documents"
all = list(os.listdir(path))
print(all)

#2
def check_access(path):
    if not os.path.exists(path):
        print("path doesn't exist")
        return 
    else:
        print('path does exist')
        if os.access(path, os.R_OK):
            print("readable")
        else:
            print("don't readable")
        if os.access(path, os.W_OK):
            print("writable")
        else:
            print("don't writable")
        if os.access(path, os.X_OK):
            print("executable")
        else:
            print("don't executable")

if __name__ == "__main__":
    path_to_check = r"C:\Users\Алмас\Documents" 
    
check_access(path_to_check)

#3
def check(path):
    if os.path.exists(path):
        print("Name of file: ", os.path.basename(path))
        print("Name of directory: ", os.path.dirname(path))
    return "success"
print(check(path))

#4
with open("sometext.txt") as f:
    data = f.read()
print(len(list(data.split("\n"))))
f.close()

#5
def writesome(list_of_elements):
    with open("sometext.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text += str(i) + ' '
        f.write(text)
        f.close()
    
 
writesome([56789, 83948, "aoalsjkls", "ssjdkd"])

#6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("Hello World!")

if __name__ == "__main__":
    generate_files()

#7
def copier():
    string = str(input("Enter the name of file: "))
    with open(string) as file:
        data = file.read()
    file.close()
    copy_path = ""
    for i in range(len(string)):
        if string[i] == '.':
            copy_path += '_1'
        copy_path += string[i]
    with open(copy_path, "+w") as file_copy:
        file_copy.write(data)
    file.close()
    
    return 0

copier()

#8
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            try:
                os.remove(path)
                print(f"Файл '{path}' успешно удален.")
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
            else:
                print("The file deleted")
        else:
            print(f"Отсутствует право на запись в файл '{path}'.")
    else:
        print(f"Файл '{path}' не существует.")

delete_file(r"C:\Users\Алмас\Documents\LABS_PP2\labs\lab6\Z.txt")