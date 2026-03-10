import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        # debug
        #if directory == ".": print("Result for current directory:")
        #else:
        #    print(f"Result for {directory} directory:")
        
        working_dir_abs = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(working_dir_abs, directory))
        if not os.path.exists(abs_file_path):
            return(f"Error: Directory '{abs_file_path}' does not exist.")
    
        valid_target_path = os.path.commonpath([working_dir_abs, abs_file_path]) == working_dir_abs
        if not valid_target_path:
            return(f"Error: Cannot list '{directory}' as it is outside the permitted working directory.")
    
        contents = os.listdir(abs_file_path)
    
    
        for(i, item) in enumerate(contents):
            item_path = os.path.join(abs_file_path, item)
            size = os.path.getsize(item_path)
            if os.path.isdir(item_path):
                contents[i] = f"    - {item}: file_size={size} bytes, is_dir=True"
            else:
                contents[i] = f"    - {item}: file_size={size} bytes, is_dir=False"

        return "\n".join(contents)
    except Exception as e:
        return f"Error listing files: {(e)}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="List information about files in a specified directory relative to the working directory, providing file size and directory status.",
    parameters=types.Schema(
        required=["directory"],
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The target directory to list files from. It must be within the working directory. Use '.' for the current working directory."
            ),
        },
    ),
)