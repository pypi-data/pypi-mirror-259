import subprocess
import glob

def get_interpreter_path():
    for virtual_name in ['venv', '.venv', 'myenv']:
        intepreters_paths = glob.glob(f'./{virtual_name}/bin/python*')
        if intepreters_paths:
            # found the virtual environment
            # TODO: have better logic for selecting interpreter path
            interpreter_path = intepreters_paths[0]
            break
    else:
        print("Virtual environment not found")  # Debugging
        interpreter_path = None
    return interpreter_path

def main():
    interpreter_path = get_interpreter_path()
    # Define the bash command
    bash_command = "pipdeptree --python " + interpreter_path + " | grep -E '^\w+' | awk '{print $1}'"

    # Execute the bash command
    process = subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Read the output and error, if any
    output, error = process.communicate()

    # Decode the output from bytes to string
    output = output.decode('utf-8')

    # Check for errors
    if error:
        print("Error:", error.decode('utf-8'))
    else:
        print(output)
        # Print or handle the output as needed
        # Optionally, save the output to a file
        with open('requirements.txt', 'w') as file:
            file.write(output)

if __name__ == "__main__":
    main()