import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if not os.path.exists(abs_file_path):
            return(f"Error: File '{abs_file_path}' is not found.")
    
        valid_target_path = os.path.commonpath([working_dir_abs, abs_file_path]) == working_dir_abs
        if not valid_target_path:
            return(f"Error: Cannot read '{file_path}' as it is outside the permitted working directory.")
        if os.path.isdir(abs_file_path):
            return(f"Error: File is not found or is not a regular file: '{file_path}'.")
        
        with open(abs_file_path, 'r') as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f"[...File '{file_path}' truncated at {MAX_CHARS} characters.]"
            return file_content
        
    except Exception as e:
        return f"Error reading file: {(e)}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieve the content of a specified file relative to the working directory. The content is truncated if it exceeds the maximum character limit 'MAX_CHARS' from config.py.",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The target directory to list files from. It must be within the working directory. Use '.' for the current working directory."
            ),
        },
    ),
)