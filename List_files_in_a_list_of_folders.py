import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"
    except Exception as e:
        return None, str(e)

def main():
    folder_paths = input("Enter folder paths (separated by spaces): ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        
        print(f"\n📁 Folder: {folder_path}")
        
        if error_message:
            print(f" ❌ Error: {error_message}")
        else:
            if files:
                print(" ✅ Files found:")
                for file in files:
                    print(f"   - {file}")
            else:
                print(" 🔍 Folder exists but contains no files.")

if __name__ == "__main__":
    main()