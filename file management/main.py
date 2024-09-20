import os
def create_file(filename):
    try:
        with open(filename,'x')as f:
            print("File is created successfully")
    
    except FileExistsError:
        print(f'File name {filename} already exists:')
    
    except Exception as E:
        print('An error occurred!')

def view():
    files=os.listdir()
    if not files:
        print("No file found")   
    else:
        print("Files in directory")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted')
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print('An error occured')

def write_file(filename):
    try:
        with open(filename, 'w') as f:
            content = input('Enter the data to write: ')
            f.write(content + "\n")
            print('Content written successfully.')
    except Exception as e:
        print(f'An error occurred: {e}')

def read_file(filename):
    try:
        with open("abc.txt","r")as f :
            content =f.read()
            print(f"'{filename}' content:\n{content}")
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print("An error occured!")

def edit_file(filename):
    try:
        with open("abc.txt",'a') as f:
            content=input('Enter the data to add=')
            f.write(content+"\n")
            print('content added successfully')
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print("An error occured!")

def main():
    while True:
        print('File management app')
        print('1: Create file')
        print('2: View all file')
        print('3: Delete file')
        print('4: write file')
        print('5: Read file')
        print('6: Edit file')
        print('7: Exit ')

        choice=input('Enter the number(1-6):')

        if choice=='1':
            filename=input("Enter the filename to create:")
            create_file(filename)

        elif choice=='2':
            view()

        elif choice=='3':
            filename=input("Enter the filename to delete:")
            delete_file(filename)
        
        elif choice == '4':
            filename = input("Enter the filename to write: ")
            write_file(filename)

        elif choice=='5':
            filename =input("Enter the filename to create:")
            read_file(filename)

        elif choice =='6':
            filename=input("Enter the filename to create:")
            edit_file(filename)

        elif choice=='7':
            print("Closing the program....")
            break
        else:
            print("Invalid Number")

if __name__=="__main__":
    main()