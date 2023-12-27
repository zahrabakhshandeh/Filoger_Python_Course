import argparse
import os
import json
import shutil
import datetime


WHITE = '\033[97m'
BLUE = '\033[94m'
RESET = '\033[0m'

WORKING_DIR_FILE = 'path.json'
LOG_FILE = 'logs.log'

def setup():
    """
    Initialize and configure the argument parser for the CLI tool.

    This function sets up an argument parser with various options for
    file manipulation and directory navigation commands. It defines 
    required and optional command-line arguments for the tool.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(
        description="File manipulation and directory navigation CLI tool"
    )
    parser.add_argument(
        "command", 
        help="Command to execute (ls, cd, mkdir, rmdir, rm, cp, mv, find, cat)"
    )
    parser.add_argument(
        "path", nargs='?', default='.', 
        help="Path for the command, defaults to current directory"
    )
    parser.add_argument(
        "destination", nargs='?', 
        help="Destination path for cp, mv commands"
    )
    parser.add_argument("-p", "--pattern", help="Pattern for the find command")
    parser.add_argument("-r", "--recursive", help="Recursive option for rm command")
    parser.add_argument("-f", "--file", help="File name for cat command")
    parser.add_argument("-a", "--all", action="store_true", help="Show all files and dirs.")

    return parser


def is_valid_path(path):
    """
    Check if the given path exists and is accessible.

    This function verifies the existence and readability of the specified file
    or directory path. It raises a ValueError with an appropriate message if 
    the path does not exist or is not accessible.

    Args:
        path (str): The file or directory path to check.

    Returns:
        bool: True if the path exists and is accessible, False otherwise.

    Raises:
        ValueError: If the path does not exist or is not accessible.
    """
    if not os.path.exists(path):
        raise ValueError(f"Error: The path '{path}' does not exist.")
    
    if not os.access(path, os.R_OK):
        raise ValueError(f"Error: The path '{path}' is not accessible.")

    return True


def log_command(command, status, error_message=None):
    """
    Log the execution details of a command to a log file.

    This function writes a log entry to a file, detailing the command executed,
    its status, and an optional error message if provided.

    Args:
        command (str): The executed command.
        status (str): The status of the command execution (e.g., 'Success', 'Error').
        error_message (str, optional): Additional error information if the command failed.
    """
    with open(LOG_FILE, 'a') as log:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - Command: {command}, Status: {status}"
        if error_message:
            log_entry += f", Error: {error_message}"
        log_entry += '\n'
        log.write(log_entry)


def load_working_directory():
    """
    Load the working directory from a JSON file, or default to the script's current directory.

    Returns:
        str: The working directory path.
    """
    if os.path.exists(WORKING_DIR_FILE):
        with open(WORKING_DIR_FILE, 'r') as file:
            data = json.load(file)
            return data.get('cwd', os.getcwd())

    return os.getcwd()


def save_working_directory(path):
    """
    Save the given path as the working directory in a JSON file.

    Args:
        path (str): The path to be saved as the working directory.
    """
    with open(WORKING_DIR_FILE, 'w') as file:
        json.dump({'cwd': path}, file)


def list_directory(path, show_hidden=False):
    """
    List the contents of a directory.

    This function prints each item in the specified directory. If 'show_hidden'
    is True, hidden files (those starting with '.') are also shown.

    Args:
        path (str): Path to the directory whose contents are to be listed.
        show_hidden (bool): Whether to show hidden files. Defaults to False.
    """
    cwd = load_working_directory()
    full_path = os.path.join(cwd, path)

    is_valid_path(full_path)

    try:
        for item in os.listdir(full_path):
            if show_hidden or not item.startswith('.'):
                item_path = os.path.join(full_path, item)
                color = BLUE if os.path.isdir(item_path) else WHITE
                print(f"{color}{item}{RESET}")
    except FileNotFoundError:
        print(f"Error: The directory '{cwd}' was not found.")


def change_directory(path):
    """
    Change the saved working directory to the specified path.

    This function updates the working directory in the configuration file
    to the specified path if it is valid.

    Args:
        path (str): The path to set as the new working directory.
    """
    cwd = load_working_directory()
    full_path = os.path.join(cwd, path)
    print("Current working directory:", cwd)
    print("Requested path:", path)
    print("Full path:", full_path)

    is_valid_path(full_path)

    save_working_directory(full_path)


def create_directory(name):
    """
    Create a new directory with the specified name in the current working directory.

    This function attempts to create a new directory. If the directory
    already exists, no action is taken.

    Args:
        name (str): The name of the directory to create.
    """
    cwd = load_working_directory()
    full_path = os.path.join(cwd, name)

    is_valid_path(full_path)
        
    os.makedirs(full_path, exist_ok=True)


def remove_empty_directory(path):
    """
    Remove an empty directory at the specified path.

    This function removes a directory only if it is empty. If the directory
    does not exist or is not empty, an error is printed.

    Args:
        path (str): The path of the directory to be removed.
    """
    cwd = load_working_directory()
    full_path = os.path.join(cwd, path)

    is_valid_path(full_path)
    os.rmdir(full_path)
    print(f"Empty directory '{full_path}' removed successfully.")
    

def remove_directory(path):
    """
    Remove a directory and its contents at the specified path.

    This function recursively removes a directory and all its contents.
    If the directory does not exist, an error is printed.

    Args:
        path (str): The path of the directory to be removed.
    """
    cwd = load_working_directory()
    full_path = os.path.join(cwd, path)

    is_valid_path(full_path)
    shutil.rmtree(full_path)
    print(f"Directory '{full_path}' and its contents removed recursively.")


def copy_file(source, destination):
    """
    Copy a file or directory from source to destination.

    This function copies either a file or a directory from a source path to a
    destination path. If the source is a directory, it is copied recursively.
    It checks if both source and destination paths are valid before proceeding
    with the copy operation.

    Args:
        source (str): The path of the source file or directory.
        destination (str): The path where the file or directory should be copied.

    Raises:
        ValueError: If the source or destination path is invalid.
    """
    cwd = load_working_directory()
    source_path = os.path.join(cwd, source)
    destination_path = os.path.join(cwd, destination)

    is_valid_path(source_path)
    is_valid_path(destination_path)

    if os.path.isdir(source_path):
        shutil.copytree(source_path, destination_path)
        print(f"Directory '{source_path}' copied to '{destination_path}'.")
    else:
        shutil.copy2(source_path, destination_path)
        print(f"File '{source_path}' copied to '{destination_path}'.")


def remove_file(path):
    """
    Remove a file located at the specified path.

    This function deletes a file located at the given path. It checks if the
    path is valid before attempting to remove the file. An error is raised if
    the path is invalid.

    Args:
        path (str): The path of the file to be removed.

    Raises:
        ValueError: If the path is invalid.
    """
    cwd = load_working_directory()
    full_path = os.path.join(cwd, path)
    is_valid_path(full_path)
    os.remove(full_path)
    print(f"File '{full_path}' removed successfully.")


def move_file(source, destination):
    """
    Move a file or directory from source to destination.

    Attempts to move a file or directory from the source path to the destination path.
    If an error occurs during the move, an appropriate message is printed.

    Args:
        source (str): The path of the source file or directory.
        destination (str): The path to where the file or directory will be moved.
    """
    cwd = load_working_directory()
    source_path = os.path.join(cwd, source)
    destination_path = os.path.join(cwd, destination)

    is_valid_path(source_path) 
    is_valid_path(destination_path)

    shutil.move(source_path, destination_path)
    print(f"Moved '{source_path}' to '{destination_path}'.")
    

def find_matching_files(full_path, pattern):
    """
    Find files matching a given pattern in a directory.

    This function searches for files in the specified directory and its subdirectories
    that contain the given pattern in their names.

    Args:
        full_path (str): The path of the directory to search within.
        pattern (str): The pattern to search for in file names.

    Returns:
        list: A list of paths to files that match the given pattern.
    """
    matching_files = []
    for root, _, filenames in os.walk(full_path):
        for filename in filenames:
            if pattern in filename:
                matching_files.append(os.path.join(root, filename))
    
    return matching_files


def find_files(path, pattern):
    """
    Search for files matching a specific pattern within a directory.

    Lists all files and directories in the specified path that match the given
    pattern. If no matches are found, it prints a message indicating so.

    Args:
        path (str): The directory path to search in.
        pattern (str): The pattern to match in file names.
    """
    cwd = load_working_directory()
    full_path = os.path.join(cwd, path)

    is_valid_path(full_path)

    os.path.exists(full_path)
    os.path.isdir(full_path)

    matches = find_matching_files(full_path, pattern)

    if matches:
        print("Matching files/directories:")
        for match in matches:
            print(match)
    else:
        print(f"No files/directories matching the pattern '{pattern}' found.")


def view_logs():
    """
    Display the contents of the log file.
    
    Reads and prints the contents of the log file. If the log file does not exist,
    a message indicating so is printed.
    """
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as log:
            print(log.read())
    else:
        print("No logs available.")

def cat_file(file_path):
    """
    Display the contents of a specified file.

    Reads and prints the contents of the file at the given path. If the file
    is not found or cannot be read, an error message is printed.

    Args:
        file_path (str): The path of the file to be read.
    """
    cwd = load_working_directory()
    full_path = os.path.join(cwd, file_path)

    is_valid_path(full_path)

    with open(full_path, 'r') as file:
        print(file.read())
    
    
def print_working_dir():
    """
    Print the current working directory.
    
    Displays the path of the current working directory.
    """
    cwd = load_working_directory()
    print(cwd)


def main():
    """
    The main function of the CLI tool.

    Parses command-line arguments and invokes corresponding functions
    based on the specified command. It handles various file and directory
    operations like listing, creating, removing, copying, and moving files or directories.
    """
    parser = setup()
    args = parser.parse_args()

    try:
        if args.command == 'ls':
            list_directory(args.path, show_hidden=args.all)

        elif args.command == 'mkdir':
            create_directory(args.path)

        elif args.command == "pwd":
            print_working_dir()

        elif args.command == 'cd':
            change_directory(args.path)

        elif args.command == 'rmdir':
            remove_empty_directory(args.path)

        elif args.command == 'rm':
            if args.recursive:
                remove_directory(args.recursive)
            else:
                remove_file(args.path)

        elif args.command == 'cp':
            copy_file(args.path, args.destination)

        elif args.command == 'mv':
            move_file(args.path, args.destination)

        elif args.command == 'find':
            find_files(args.path, args.pattern)

        elif args.command == "logs":
            view_logs()

        elif args.command == "cat":
            cat_file(args.file)

        else:
            print("Invalid Command!")
            log_command(args.command, "Error", "Invalid command")
            return

        log_command(args.command, "Success")

    except Exception as e:
        print(f"Error: {e}")
        log_command(args.command, "Error", str(e))

if __name__ == "__main__":
    main()