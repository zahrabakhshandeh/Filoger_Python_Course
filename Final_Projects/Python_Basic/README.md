
# PyCommander: A CLI File Management Tool

PyCommander is a versatile command-line interface (CLI) tool designed for efficient file manipulation and directory navigation in Python. It provides a range of functions from basic file operations to more complex directory handling, all accessible through simple commands.

## Features

- **File Operations**: Easily list, copy, move, remove, and view files.
- **Directory Navigation**: Change, create, or remove directories with ease.
- **Pattern Searching**: Find files and directories based on patterns.
- **Log Tracking**: Maintain logs of operations for tracking and debugging.
- **Interactive Mode**: Use an interactive shell-like environment for operations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zahrabakhshandeh/Filoger_Python_Course
   ```
2. Navigate to the cloned directory:
   ```bash
   cd pycommander
   ```

## Usage

To start using PyCommander, run the script with Python:

```bash
python pycommander.py
```

### Commands

- `ls`: List the contents of a directory.
- `cd`: Change the current working directory.
- `mkdir`: Create a new directory.
- `rmdir`: Remove an empty directory.
- `rm`: Remove a file or directory.
- `cp`: Copy files or directories.
- `mv`: Move files or directories.
- `find`: Find files or directories matching a pattern.
- `cat`: View the contents of a file.
- `pwd`: Print the current working directory.
- `logs`: View the logs of previous operations.

### Options

- `-p`, `--pattern`: Specify a pattern for the find command.
- `-r`, `--recursive`: Enable recursive removal for the rm command.
- `-f`, `--file`: Specify a file name for the cat command.
- `-a`, `--all`: Show all files and directories, including hidden ones.

## Customization

You can modify the `path.json` and `logs.log` files to customize the working directory and log preferences.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your features or fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Thank you to all the contributors and users of PyCommander. Your feedback and contributions make this tool better for everyone!

## Running the Tool

PyCommander is an intuitive command-line interface tool designed for a wide range of file and directory operations. Below are detailed instructions on how to use each available command.

### Basic Command Structure

Execute PyCommander with the following syntax:

```bash
python3 projectname.py [command] [options]
```

Replace `projectname.py` with the actual script name. The `[command]` is the action you want to perform, and `[options]` are additional parameters specific to the command.

### Available Commands

#### 1. List Directory Contents (`ls`)

- **Command**: `ls`
- **Description**: Lists all files and directories in the specified path.
- **Usage**: 
  ```bash
  python3 projectname.py ls [path]
  ```
  If no path is specified, it defaults to the current directory.

#### 2. Change Directory (`cd`)

- **Command**: `cd`
- **Description**: Changes the current working directory to the specified path.
- **Usage**:
  ```bash
  python3 projectname.py cd /path/to/directory
  ```

#### 3. Create Directory (`mkdir`)

- **Command**: `mkdir`
- **Description**: Creates a new directory with the specified name.
- **Usage**:
  ```bash
  python3 projectname.py mkdir new_directory_name
  ```

#### 4. Remove Empty Directory (`rmdir`)

- **Command**: `rmdir`
- **Description**: Removes an empty directory.
- **Usage**:
  ```bash
  python3 projectname.py rmdir /path/to/directory
  ```

#### 5. Remove File or Directory (`rm`)

- **Command**: `rm`
- **Description**: Removes a file or directory. Use the `-r` option for recursive deletion.
- **Usage**:
  ```bash
  python3 projectname.py rm /path/to/file_or_directory
  python3 projectname.py rm -r /path/to/directory  # Recursive removal
  ```

#### 6. Copy Files or Directories (`cp`)

- **Command**: `cp`
- **Description**: Copies files or directories from one location to another.
- **Usage**:
  ```bash
  python3 projectname.py cp /source/path /destination/path
  ```

#### 7. Move Files or Directories (`mv`)

- **Command**: `mv`
- **Description**: Moves files or directories from one location to another.
- **Usage**:
  ```bash
  python3 projectname.py mv /source/path /destination/path
  ```

#### 8. Find Files or Directories (`find`)

- **Command**: `find`
- **Description**: Finds files or directories that match a given pattern.
- **Usage**:
  ```bash
  python3 projectname.py find /search/directory -p "pattern"
  ```

#### 9. View File Contents (`cat`)

- **Command**: `cat`
- **Description**: Displays the contents of a file.
- **Usage**:
  ```bash
  python3 projectname.py cat /path/to/file
  ```

#### 10. Print Working Directory (`pwd`)

- **Command**: `pwd`
- **Description**: Prints the current working directory.
- **Usage**:
  ```bash
  python3 projectname.py pwd
  ```

#### 11. View Logs (`logs`)

- **Command**: `logs`
- **Description**: Displays the logs of the operations performed.
- **Usage**:
  ```bash
  python3 projectname.py logs
  ```