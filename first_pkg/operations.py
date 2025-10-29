from  messaging import display_details
def add(a,b):
    display_details("Adding values", a, b)
    return a + b

subsstrat = lambda a,b:  a - b

def multiply(a,b):
    display_details("Multiplying values", a, b)
    return a * b    

division = lambda a,b: a / b if b != 0 else None;

if __name__ == "__main__":
    try:
        multiply(4,3)
    except ValueError as ve: 
        print(f"Error: {ve}")
    else :
        print("Multiplication successful.")
    finally:
        print("Operation completed.")