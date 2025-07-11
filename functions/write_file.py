import os


def write_file(working_directory, file_path, content):
    """
    Write content to a file, ensuring it's within the working directory.

    Args:
        working_directory (str): The permitted working directory
        file_path (str): The path to the file to write
        content (str): The content to write to the file

    Returns:
        str: Success message or error message
    """
    try:
        working_dir = os.path.abspath(working_directory)

        # If file_path is relative, join it with working_directory
        if not os.path.isabs(file_path):
            target_file = os.path.abspath(os.path.join(working_directory, file_path))
        else:
            target_file = os.path.abspath(file_path)

        if (
            not target_file.startswith(working_dir + os.sep)
            and target_file != working_dir
        ):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        target_dir = os.path.dirname(target_file)
        if target_dir and not os.path.exists(target_dir):
            os.makedirs(target_dir)

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except PermissionError:
        return f'Error: Permission denied when writing to "{file_path}"'
    except OSError as e:
        return f'Error: OS error when writing to "{file_path}": {str(e)}'
    except Exception as e:
        return f'Error: Unexpected error when writing to "{file_path}": {str(e)}'
