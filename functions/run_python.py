import os
import subprocess


def run_python_file(working_directory, file_path):
    """
    Executes a Python file with validation and subprocess handling.

    Args:
        working_directory (str): The permitted working directory.
        file_path (str): The path to the Python file to execute.

    Returns:
        str: Formatted output or error message.
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
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if file exists
        if not os.path.isfile(file_path):
            return f'Error: File "{file_path}" not found.'

        # Check if file is a Python file
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # Run the Python file
        result = subprocess.run(
            ["python", file_path],
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        if not output:
            return "No output produced."
        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
