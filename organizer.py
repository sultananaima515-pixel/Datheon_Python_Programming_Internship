
import os
import shutil
from pathlib import Path

file_categories = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".c":"code",
    ".pptx":"Documents"
}


source_folder = Path("testdownloads")


moved_count = 0
skipped_count = 0
error_count = 0


if not source_folder.exists():
    print("Source folder does not exist.")

elif not source_folder.is_dir():
    print("Selected path is not a directory.")

else:
    
    with os.scandir(source_folder) as scan:
        entries = list(scan)

    
    for entry in entries:

        if not entry.is_file(follow_symlinks=False):
            continue

        file_path = Path(entry.path)
        extension = file_path.suffix.lower()

        
        category = file_categories.get(extension, "Others")

        
        destination_folder = source_folder / category

        try:
            destination_folder.mkdir(exist_ok=True)

            
            destination_path = destination_folder / file_path.name

            
            if destination_path.exists():
                counter = 1

                while destination_path.exists():
                    new_name = (
                        f"{file_path.stem} ({counter})"
                        f"{file_path.suffix}"
                    )
                    destination_path = destination_folder / new_name
                    counter += 1

            
            shutil.move(str(file_path), str(destination_path))

            moved_count += 1
            print(f"Moved: {file_path.name} -> {category}")

        except PermissionError:
            error_count += 1
            print(f"Permission denied: {file_path.name}")

        except FileNotFoundError:
            error_count += 1
            print(f"File not found: {file_path.name}")

        except OSError as e:
            error_count += 1
            print(f"Error: {file_path.name} - {e}")

    
    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Successfully moved: {moved_count}")
    print(f"Skipped files: {skipped_count}")
    print(f"Failed operations: {error_count}")
    print("==========================================")
