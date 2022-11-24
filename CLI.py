import functions
#from functions import get_list, write_list
import time

now = time.strftime("%d/%m/%Y %H:%M:%S")
print("It is", now)
while True:
     action = input("Type add, show, edit, complete, or exit: ")
     action.strip()

     if action.startswith("add"):
         operation = action[4:]

         # file = open("operation.txt", 'r')
         # list = file.readlines()
         # file.close()
         # We can make here context manager instead of block above
         list = functions.get_list()

         list.append(operation + '\n')

         # file = open("operation.txt", 'w')
         # file.writelines(list)
         # file.close()
         functions.write_list(list, "operation.txt")

     elif action.startswith("show"):
         # file = open("operation.txt", 'r')
         # list = file.readlines()
         # file.close()
         list = functions.get_list()

         for index, item in enumerate(list):
             item = item.strip('\n')
             print(f"{index + 1}.{item}")

     elif action.startswith("edit"):
        try:
             number = int(action[5:])
             print(number)

             number -= 1

             list = functions.get_list()

             new_operation = input("Enter new operation: ")
             list[number] = new_operation + '\n'

             functions.write_list(list, "operation.txt")

        except ValueError:
            print("Your command is not valid")
            continue

     elif action.startswith("complete"):
         try:
             number = int(action[9:])

             list = functions.get_list()

             index = number - 1
             operation_removal = list[index].strip('\n')
             list.pop(index)

             functions.write_list(list, "operation.txt")

             message = f"Operation {operation_removal} was removed from the list"
             print(message)

         except IndexError:
             print("There is no item with that number")
             continue

     elif action.startswith("exit"):
         break

     else:
         print("You entered invalid variable")
