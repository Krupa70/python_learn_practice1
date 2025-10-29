def read_my_file():
    try:
        with open("C:\\Users\\kpand\\Downloads\\test.txt", "r") as my_file:
            content = my_file.readlines()
            print(content)
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")

def write_to_file():
    try:
        with open("C:\\Users\\kpand\\Downloads\\test.txt", "a") as my_file:
            my_file.write("Appending a new line to the file.\n")
    except IOError as io_error:
        print(f"Error: {io_error}")       
    finally:
        print("File operation attempted.")
        

if __name__ == "__main__":
    read_my_file()
    print("-------------------------------------")
    write_to_file()
    print("-------------------------------------")

    read_my_file()
