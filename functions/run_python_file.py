import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_path = os.path.commonpath([working_dir_abs, abs_file_path]) == working_dir_abs
        if not valid_target_path:
            return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.')
        if not os.path.isfile(abs_file_path):
            return(f'Error: File "{file_path}" does not exist or is not a regular file.')
        if not file_path.endswith(".py"):
            return f'Error: File "{file_path}" is not a Python file.'
        
        command = ["python", abs_file_path]
        if args:
            command.extend(args)

        process = subprocess.run(command, text=True, timeout = 30, capture_output=True)
        output = ""
        if process.returncode != 0: output += f"Process exited with code {process.returncode}\n"
        if not process.stdout and not process.stderr: output += "No output produced\n"
        else:
            output += f"STDOUT:{process.stdout}\n"
            output += f"STDERR:{process.stderr}\n"
        return output
        
    except Exception as e:
        return f'Error executing Python file: {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file relative to the working directory. Can take array of args as parameter",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The target directory to list files from. It must be within the working directory. Use '.' for the current working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="The arguments to pass to the Python file."
            )
        },
    ),
)