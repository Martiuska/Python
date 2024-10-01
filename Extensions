import difflib

def main():
    # Ask the user for the file name
    file_name = input("Enter the file name: ").strip().lower()

    # Dictionary that maps file extensions to MIME types
    mime_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".pgn": "image/png",  # Intentional typo for ".png"
        ".png": "image/png",
        ".gif": "image/gif",
        ".pdf": "application/pdf",
        ".pfd": "application/pdf",  # Intentional typo for ".pdf"
        ".txt": "text/plain",
        ".text": "text/plain",  # Intentional typo for ".txt"
        ".zip": "application/zip",
        ".py": "text/x-python", # Add Python extension ".py"
    }

    # Extract the file extension from the user's input
    ext = file_name[file_name.rfind("."):]

    # Check if the extension is in the dictionary
    if ext in mime_types:
        print(mime_types[ext])
    else:
        # Suggest a similar extension if the user made a typo
        similar_ext = difflib.get_close_matches(ext, mime_types.keys(), n=1)
        if similar_ext:
            print(f"Did you mean '{similar_ext[0]}'? MIME type: {mime_types[similar_ext[0]]}")
        else:
            print("application/octet-stream")  # Generic type for unknown files

# Start the program
if __name__ == "__main__":
    main()
