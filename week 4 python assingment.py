def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes to a new file.
    Adds line numbers and converts text to uppercase as modification examples.
    """
    try:
        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()
            
        # Modify content (add line numbers and uppercase)
        modified_lines = []
        for i, line in enumerate(lines, 1):
            modified_lines.append(f"{i}: {line.upper()}")
        
        with open(output_filename, 'w') as output_file:
            output_file.writelines(modified_lines)
            
        print(f"Successfully processed {input_filename} and wrote to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing {input_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage:
modify_and_write_file('original.txt', 'modified.txt')

# error handling
def read_file_with_handling():
    """
    Asks user for filename and handles potential errors gracefully.
    """
    while True:
        filename = input("Enter the filename you want to read (or 'quit' to exit): ")
        
        if filename.lower() == 'quit':
            print("Goodbye!")
            break
            
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile content:")
                print("-" * 40)
                print(content)
                print("-" * 40)
                break
                
        except FileNotFoundError:
            print(f"Error: The file '{filename}' doesn't exist. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'. Please try another file.")
        except UnicodeDecodeError:
            print(f"Error: Couldn't decode '{filename}'. It might be a binary file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}. Please try again.")

# Example usage:
read_file_with_handling()