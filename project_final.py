import os
import shutil
import random

from colorama import Fore, init

def ascii_intro():
    """Intro dot art"""
    print("""
          
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⠟⠿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⡿⠛⠉⠀⠀⠀⠀⠙⠻⢿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⠿⠋⠁⠀⠀⢀⣠⣶⣦⣄⡀⠀⠀⠉⠛⠿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⡿⠟⠉⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠈⠙⠻⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣇⠀⠀⢀⣠⣶⣿⣿⣿⣿⠟⠋⠀⠈⠛⠿⣿⣿⣿⣷⣦⣄⠀⠀⠀⣽⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡿⠟⠋⠀⠈⢿⣿⣧⣾⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣶⣾⣿⠟⠀⠈⠙⠿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⣀⣴⣾⣿⣿⡿⠛⠉⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⡍⢀⣤⣶⣿⠀⠀⠀⠀⠀⢠⣿⣦⣄⡈⣹⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠙⠻⢿⣿⣿⣶⣤⡀⠀⠀⠀
                ⣠⣴⣿⣿⣿⠿⠋⠁⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠈⠛⠿⣿⣿⣷⣦⡀
                ⣿⣿⡟⠉⠀⠀⠀⣠⣴⣾⣿⣿⣿⡿⠟⠉⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠈⠙⠻⢿⣿⣿⣿⣶⣤⣀⠀⠀⠈⠙⣿⣿⡇
                ⣿⣿⡇⠀⠀⢰⣿⣿⣿⣿⠟⠋⠁⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠉⠛⠿⣿⣿⣿⣷⡆⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⡏⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⢹⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣀⡄⠀⢸⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⡇⠀⢸⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⣇⣀⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣇⣀⣸⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⣇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⡏⠉⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⡏⠉⢹⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⡇⠀⢸⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠋⠉⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠃⠀⢸⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⣿⣿⡇
                ⣿⣿⡇⠀⠀⠸⣿⣿⣿⣷⣦⣄⡀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⣀⣤⣶⣿⣿⣿⡿⠃⠀⠀⣿⣿⡇
                ⣿⣿⣧⣄⠀⠀⠀⠉⠻⢿⣿⣿⣿⣷⣤⣀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢀⣠⣴⣾⣿⣿⣿⠿⠛⠁⠀⠀⢀⣠⣿⣿⡇
                ⠙⠻⣿⣿⣿⣶⣄⡀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⣀⣤⣶⣿⣿⡿⠟⠁
                ⠀⠀⠀⠉⠻⢿⣿⣿⣷⣤⣀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣃⠈⠛⠿⣿⠀⠀⠀⠀⠀⠘⡿⠟⠋⢁⣹⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⣠⣴⣾⣿⣿⠿⠛⠁⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣷⣦⣄⡀⢀⣾⣿⠟⠿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⠟⢻⣿⣦⠀⢀⣤⣶⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣏⠀⠀⠈⠙⠻⢿⣿⣿⣿⣦⣄⡀⢀⣠⣶⣿⣿⣿⡿⠟⠉⠀⠀⠀⣻⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣷⣦⣄⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⢀⣠⣴⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣶⣄⡀⠀⠀⠈⠙⠿⠟⠋⠀⠀⠀⣀⣤⣾⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣷⣦⣀⠀⠀⠀⢀⣠⣴⣾⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣶⣶⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀
                     _____                 _             ____ _     ___ 
                    | ____|_ __ ___  _ __ (_)_ __ ___   / ___| |   |_ _|
                    |  _| | '_ ` _ \| '_ \| | '__/ _ \ | |   | |    | | 
                    | |___| | | | | | |_) | | | |  __/ | |___| |___ | | 
                    |_____|_| |_| |_| .__/|_|_|  \___|  \____|_____|___|
                                |_|                                 
                        
                    ===================================================
                                Type 'help' to see the command 
                    ===================================================
    """)

def ls():
    """Showing file list and folder in Directory for now"""
    for item in os.listdir(os.getcwd()):
        print(item)

def pwd():
    """Showing Work Directory for now"""
    print(os.getcwd())

def cd(path):
    """Changing Work Directory"""
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found")
    except NotADirectoryError:
        print(f"Error: '{path}' bukan Directory")

def mkdir(directory_name):
    """Making new Directory"""
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' successfully created")
    except FileExistsError:
        print(f"Error: Directory '{directory_name}' exists")
    except OSError as e:
        print(f"Error: {e}")

def rmdir(directory_name):
    """Deleting directory if empty"""
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' successfully deleted")
    except FileNotFoundError:
        print(f"Error: Directory '{directory_name}' not found")
    except OSError:
        print(f"Error: Directory '{directory_name}' not empty or can't be deleted")

def touch(file_name):
    """Make empty file"""
    try:
        with open(file_name, 'a'):
            os.utime(file_name, None)
        print(f"File '{file_name}' successfully created")
    except OSError as e:
        print(f"Error: {e}")

def rm(file_name):
    """Deleting file"""
    try:
        os.remove(file_name)
        print(f"File '{file_name}' successfully deleted")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
    except IsADirectoryError:
        print(f"Error: '{file_name}' is a directory, use rmdir to delete the directory")

def cp(source, destination):
    """Copy files from one location to another"""
    try:
        shutil.copy(source, destination)
        print(f"File '{source}' successfully copied to '{destination}'")
    except FileNotFoundError:
        print(f"Error: File '{source}' not found")
    except OSError as e:
        print(f"Error: {e}")

def mv(source, destination):
    """Move or rename file/directory"""
    try:
        shutil.move(source, destination)
        print(f"'{source}' successfully removed/changed into '{destination}'")
    except FileNotFoundError:
        print(f"Error: '{source}' not found")
    except OSError as e:
        print(f"Error: {e}")

init(autoreset=True)

def help_command():
    command_colors = {
        "ls"        : Fore.CYAN,
        "pwd"       : Fore.GREEN,
        "cd"        : Fore.YELLOW,
        "mkdir"     : Fore.MAGENTA,
        "rmdir"     : Fore.RED,
        "touch"     : Fore.BLUE,
        "rm"        : Fore.WHITE,
        "cp"        : Fore.LIGHTYELLOW_EX,
        "mv"        : Fore.LIGHTGREEN_EX,
        "search"    : Fore.LIGHTCYAN_EX,
        "tree"      : Fore.LIGHTMAGENTA_EX,
        "joke"      : Fore.LIGHTBLUE_EX,
        "help"      : Fore.LIGHTWHITE_EX,
        "clear"     : Fore.LIGHTGREEN_EX,
        "exit"      : Fore.LIGHTRED_EX,
    }
    
    commands = {
        "ls"        : "Displaying a list of files and folders in the current directory",
        "pwd"       : "Displaying the current working directory",
        "cd"        : "Changing the working directory",
        "mkdir"     : "Creating a new directory",
        "rmdir"     : "Delete directory (if empty)",
        "touch"     : "Create a new blank file",
        "rm"        : "Delete file",
        "cp"        : "Scopying files from one location to another",
        "mv"        : "Move or rename file/directory",
        "search"    : "Looking for files or directories by name",
        "tree"      : "Displaying directory structure in tree shape",
        "joke"      : "Showing random jokes for entertainment",
        "help"      : "Displaying the existing command list and function",
        "clear"     : "Clear the terminal screen",
        "exit"      : "Out of CLI",
    }

    for cmd, desc in commands.items():
        print(command_colors[cmd] + f"{cmd}: {desc}")

def clear():
    """Clears terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def search(pattern):
    """Search for files or directories by name"""
    print(f"Searching '{pattern}' in {os.getcwd()}:")
    for root, dirs, files in os.walk(os.getcwd()):
        for name in dirs + files:
            if pattern in name:
                print(os.path.join(root, name))

def tree(path=".", indent=""):
    """Displays the directory structure in the form of a tree"""
    try:
        entries = os.listdir(path)
        for i, entry in enumerate(entries):
            connector = "└── " if i == len(entries) - 1 else "├── "
            print(indent + connector + entry)
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                tree(full_path, indent + ("    " if i == len(entries) - 1 else "│   "))
    except PermissionError:
        print(indent + "└── [Permission Denied]")

def joke():
    """Showing random jokes for entertainment"""
    jokes = [
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "Why don’t eggs tell jokes? Because they might crack up.",
    "Why do cows have hooves instead of feet? Because they lactose.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why can't you trust an atom? Because they make up everything.",
    "Why did the math book look sad? Because it had too many problems." ,   ]
    print(random.choice(jokes))

def main():
    ascii_intro()
    while True:
        command = input("shell> ").strip()
        if not command:
            continue
        args = command.split()
        cmd = args[0].lower()

        try:
            if cmd == "ls":
                ls()
            elif cmd == "pwd":
                pwd()
            elif cmd == "cd":
                cd(args[1])
            elif cmd == "mkdir":
                mkdir(args[1])
            elif cmd == "rmdir":
                rmdir(args[1])
            elif cmd == "touch":
                touch(args[1])
            elif cmd == "rm":
                rm(args[1])
            elif cmd == "cp":
                cp(args[1], args[2])
            elif cmd == "mv":
                mv(args[1], args[2])
            elif cmd == "search":
                search(args[1])
            elif cmd == "tree":
                tree(args[1] if len(args) > 1 else ".")
            elif cmd == "joke":
                joke()
            elif cmd == "help":
                help_command()
            elif cmd == "clear":
                clear()
            elif cmd == "exit":
                print("You've left the Dark Side, see you in another strikes!")
                break
            else:
                print(f"Error: Command '{cmd}' not recognized")
        except IndexError:
            print("Error: Arguments are not enough for this command")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
