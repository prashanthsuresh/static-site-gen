import os
import shutil

def copy_directory(src, dest):
    """Recursively copies all contents from the source directory to the destination directory."""
    
    # Ensure destination is clean
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

    # Iterate through all items in the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):  # Copy files
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {dest_path}")
        else:  # Recursively copy directories
            os.mkdir(dest_path)
            copy_directory(src_path, dest_path)
            print(f"Copied directory: {dest_path}")

# Hook it up to the main function
if __name__ == "__main__":
    copy_directory("static", "public")
