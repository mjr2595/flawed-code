import os

from google.genai import types


def get_files_info(working_directory, directory=None):
    """
    Get a formatted string representing the contents of the specified directory.

    Args:
        working_directory (str): The base directory to start from.
        directory (str, optional): The specific directory to get file info from. Defaults to None.

    Returns:
        str: A formatted string listing files and directories with their sizes and type.
    """

    # Use working_directory if directory isn't specified
    if not directory:
        directory = "."

    # Resolve absolute paths
    base_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))

    # Only allow listing inside the working_directory
    if not os.path.commonpath([base_dir, target_dir]) == base_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    entries = []
    try:
        for entry in os.scandir(target_dir):
            name = entry.name
            is_dir = entry.is_dir()
            if is_dir:
                # Recursively sum file sizes in the directory
                total_size = 0
                try:
                    for root, _, files in os.walk(entry.path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            try:
                                total_size += os.path.getsize(file_path)
                            except Exception as e:
                                return f"Error: {str(e)}"
                    size = total_size
                except Exception as e:
                    return f"Error: {str(e)}"
            else:
                try:
                    size = os.path.getsize(entry.path)
                except Exception as e:
                    return f"Error: {str(e)}"
            entries.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
    except Exception as e:
        return f"Error: {str(e)}"

    return "\n".join(entries)


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
