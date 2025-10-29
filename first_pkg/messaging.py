def display(message):
    print(f"Message: {message}")    

def display_details(message, arg1, arg2):
    if arg1 > arg2:
        raise ValueError("arg1 must be >= arg2")
    print(f"{message}: {arg1}, {arg2}")


if __name__ == "__main__":
    display("This is a test message.")
    display_details("Details", 5, 10)