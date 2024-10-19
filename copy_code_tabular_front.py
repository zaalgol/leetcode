import os

def aggregate_files(folder_path, output_file):
    allowed_extensions = ['.jsx']
    ignore_folders = {'node_modules', 'public', 'icons', 'tests'}

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
    folder_path = "C:/code/tabular-wizard-front" # input("Enter the folder path: ") 
    output_file = 'tabular-wizard-front.txt'
    aggregate_files(folder_path, output_file)
    print(f"Aggregated content saved to {output_file}")