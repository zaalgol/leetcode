import os

def aggregate_files(folder_path, output_file):
    allowed_extensions = ['.py']
    ignore_folders = {'.venv', 'documents_final', '.vscode', '.env', 'datasets', 'temp', 'config', '.fast_api_venv',
                      '.fast_api_venv_up', 'catboost_info', 'migrations', 'saved_inferences', 'saved_models', 'tests',
                      os.path.normpath('app/playground'), os.path.normpath('app/ai'), os.path.normpath('app/temp')}

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(folder_path):
            # Convert the current directory path to a normalized path
            current_dir = os.path.normpath(os.path.relpath(root, folder_path))
            
            # Exclude ignored directories from traversal
            dirs[:] = [d for d in dirs if os.path.normpath(os.path.join(current_dir, d)) not in ignore_folders]
            
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in allowed_extensions:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, folder_path)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                        outfile.write(f"{relative_path}:\n{content}\n\n")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

if __name__ == "__main__":
    folder_path = "C:/code/tabular-wizard-server" # input("Enter the folder path: ") 
    output_file = 'tabular-wizard-server3.txt'
    aggregate_files(folder_path, output_file)
    print(f"Aggregated content saved to {output_file}")