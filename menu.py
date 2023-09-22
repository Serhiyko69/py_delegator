import os
from abc import ABC, abstractmethod
from notebook.nb_main import NoteManager
import importlib
class UserInterface(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_commands(self):
        pass

class ConsoleUserInterface(UserInterface):
    def display_menu(self):

        pass

    def display_contacts(self, contacts):

        pass

    def display_notes(self, notes):

        pass

    def display_commands(self):

        pass


class Menu:
    def __init__(self, user_interface):
        self.choices = {
            1: ("calend", "calend_main"),
            2: ("Addressbook", "start"),
            3: ("notebook.nb_main", "nb_main"),
            4: ("file_sorter", "start"),
            5: ("exchanger", "ex_main")
        }
        self.user_interface = user_interface



    def make_decision(self, choice):
        module_name, function_name = self.choices.get(choice)

        if not module_name:
            return

        if choice == 3:
            note_folder = "notebook/notes"
            note_manager = NoteManager(note_folder)
            note_manager.nb_main()
            return True

        try:
            if choice == 4:
                directory_path = input("Enter the path to directory: ")
                if os.path.exists(directory_path) and os.path.isdir(directory_path):
                    function = getattr(importlib.import_module(module_name), function_name)
                    function(directory_path)
                else:
                    print("Invalid directory path. Please enter a valid directory path.")
            else:
                function = getattr(importlib.import_module(module_name), function_name)
                function()
        except ModuleNotFoundError:
            print("Module not found.")
        except AttributeError:
            print("Function not found in the module.")

def main():
    print("Choose an option:")
    print("1. Calendar")
    print("2. Address Book")
    print("3. Notebook")
    print("4. File Sorter")
    print("5. Exchanger")
    print("6. Exit")

    user_interface = ConsoleUserInterface()  # Створення об'єкту інтерфейсу
    menu = Menu(user_interface)  # Передача об'єкту інтерфейсу в меню

    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 6:
                break
            menu.make_decision(choice)  # Виклик методу make_decision з об'єкта menu
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()


   # +------------------+
   # |     UserInterface|<<abstract>>
   # +------------------+
   # | <<abstractmethod>>display_menu()
   # | <<abstractmethod>>display_contacts(contacts)
   # | <<abstractmethod>>display_notes(notes)
   # | <<abstractmethod>>display_commands()
   # +------------------+
   #           /_\
   #            |
   #            |
   #            |
   #            |
   #            |
   #            |
   #            |
   #            v
   # +-----------------------+
   # | ConsoleUserInterface  |
   # +-----------------------+
   # | display_menu()        |
   # | display_contacts(contacts) |
   # | display_notes(notes) |
   # | display_commands()    |
   # +-----------------------+
   #            |
   #            |
   #            |
   #            |
   #            |
   #            |
   #            |
   #            v
   # +-----------------------+
   # |         Menu          |
   # +-----------------------+
   # | choices               |
   # | user_interface        |
   # | make_decision(choice) |
   # +-----------------------+
   #            |
   #            |
   #            |
   #            |
   #            |
   #            |
   #            |
   #            v
   # +------------------------+
   # |    Module Functions    |
   # +------------------------+
   # | (Various functions in  |
   # | different modules)     |
   # +------------------------+
