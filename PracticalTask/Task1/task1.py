import os

KNOWN_EXTENSIONS = {
    '.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.csv',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg',
    '.py', '.java', '.c', '.cpp', '.html', '.css', '.js',
    '.mp3', '.wav', '.mp4', '.avi', '.mkv', '.mov',
    '.zip', '.rar', '.7z', '.tar', '.gz',
    '.json', '.xml', '.yml', '.ini', '.log'
}

def get_file_extension(filename):
    name, extension = os.path.splitext(filename)
    if extension == '':
        raise ValueError("The file has no extension.")
    return extension

if __name__ == "__main__":
    print("File Extension Checker")

    filename = input("Enter the file name (e.g., document.txt): ").strip()

    try:
        ext = get_file_extension(filename)
        print(f"File extension: {ext}")
        
        if ext.lower() not in KNOWN_EXTENSIONS:
            print("Warning: This file extension is not commonly recognized.")
    except ValueError as e:
        print(f"Error: {e}")
