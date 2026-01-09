import os

def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
            except:
                pass
    return total_size

def analyze_path(path):
    if not os.path.exists(path):
        print("❌ Path does not exist.")
        return

    print("\n📁 Folder Size Analyzer Report")
    print("-" * 65)
    print("{:<40} {:>15}".format("Name", "Size (KB)"))
    print("-" * 65)

    # MAIN FOLDER SIZE
    main_size = get_folder_size(path)
    print("{:<40} {:>15.2f}".format("MAIN FOLDER", main_size / 1024))

    print("\n🔹 Subfolders:")
    has_subfolders = False

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            has_subfolders = True
            size = get_folder_size(full_path)
            print("{:<40} {:>15.2f}".format(item, size / 1024))

    if not has_subfolders:
        print("No subfolders found.")

    print("\n🔹 Files:")
    has_files = False

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            has_files = True
            size = os.path.getsize(full_path)
            print("{:<40} {:>15.2f}".format(item, size / 1024))

    if not has_files:
        print("No files found.")

def main():
    print("🗂 Folder Size Analyzer")
    path = input("Enter folder path: ").strip()
    analyze_path(path)

if __name__ == "__main__":
    main()