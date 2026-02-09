# Apps backend data: Constants and Functions.
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file & return the list of to-do items. """
    with open(filepath, 'r') as f:
        todos_local = f.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)


# Testing the App locally before exporting any function.
if __name__ == "__main__":
    print("Test dummy data: Import from the function module.")
    print(get_todos())
    print(f"The FILEPATH name is: {FILEPATH}")
