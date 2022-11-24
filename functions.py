FILEPATH = "operation.txt"

def get_list(filepath=FILEPATH):
    """
    Read the text file and return list of operations
    """
    with open(filepath, 'r') as file_local:
        list_local = file_local.readlines()
    return list_local

def write_list(list_arg, filepath=FILEPATH):
    """
    Write the operation items list in the 'operation.txt' file
    """
    with open(filepath, 'w') as file:
        file.writelines(list_arg)

if __name__ == "__main__":
    print("Hello from functions")
    print(get_list())