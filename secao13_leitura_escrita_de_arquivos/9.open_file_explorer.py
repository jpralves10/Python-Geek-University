import os
import subprocess

def open_file_in_explorer(filepath):
    """Opens the specified file in Windows Explorer.

    Args:
        filepath: The path to the file to open.
    """

    try:
        # Check if the file exists
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        # Open the file using Windows Explorer
        subprocess.run(['explorer', filepath], check=True)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error opening file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_path = r"C:\# MATERIAL\PROGRAMAS\Banco de Dados\MySQL\docker-compose.yml"  # Replace with the actual file path
open_file_in_explorer(file_path)
