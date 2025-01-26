class FileHandler:
    
    def __init__(self):
        # Constructor for any initialization, if needed
        pass

    def read_file(self):
        """Method to read a file specified by the user."""
        filename = input("Enter the path of the file to read: ")

        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile Content:")
                print(content)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found. Please check the filename and try again.")

# Create an instance of the class and call the method
if __name__ == "__main__":
    file_handler = FileHandler()
    file_handler.read_file()
