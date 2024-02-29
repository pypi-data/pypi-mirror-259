import tempfile
import subprocess
import os

def flatbuffers_to_json_with_flatc(flatbuffers_binary, schema_file):
    # Write the binary data to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_binary_file:
        temp_binary_file.write(flatbuffers_binary)
        temp_binary_file_path = temp_binary_file.name

    # Prepare the command to convert the binary data to JSON using flatc
    # Added the --raw-binary option to bypass the file identifier check
    command = ["flatc", "-t", "--strict-json", "--raw-binary", schema_file, "--", temp_binary_file_path]

    try:
        # Execute the command and capture the output
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE)
        json_output = result.stdout.decode('utf-8')

        return json_output
    finally:
        # Cleanup the temporary binary file
        os.remove(temp_binary_file_path)
