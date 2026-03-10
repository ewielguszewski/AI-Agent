import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_path = os.path.commonpath([working_dir_abs, abs_file_path]) == working_dir_abs
        if not valid_target_path:
            return(f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory.")
        if os.path.isdir(abs_file_path):
            return(f"Error: File is not found or is not a regular file: '{file_path}'.")
        
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        with open(abs_file_path, 'w') as f:
            f.write(content)
            return f"Successfully wrote to '{file_path}' ({len(content)} characters written)."
        
    except Exception as e:
        return f"Error writing to file: {(e)}"
        
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a specified file relative to the working directory.",
    parameters=types.Schema(
        required=["file_path", "content"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The target directory to list files from. It must be within the working directory. Use '.' for the current working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file."
            )
        },
    ),
)