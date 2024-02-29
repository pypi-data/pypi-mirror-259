import os
import random
import string
import zipfile

from .path import get_test_data_dir
  
def generate_zip_file(zip_filename, target_size_mb):
    # Create a random string to add to the zip file
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=1024))

    # Open a new zip file
    with zipfile.ZipFile(zip_filename, "w") as zip_file:
        while os.path.getsize(zip_filename) < target_size_mb * 1024 * 1024:
            # Generate a random filename
            file_name = "".join(random.choices(string.ascii_letters, k=8)) + ".txt"

            # Add a file with the random string content to the zip file
            zip_file.writestr(file_name, random_string)

def generate_server_data(output_dir=None, num_files=10, max_size=0.5):
    if output_dir is None:
        output_dir = os.path.join(
            get_test_data_dir(), "server_data"
        )

    for i in range(num_files):
        zip_filename = os.path.join(output_dir, f"file_{i}.zip")
        if not os.path.exists(zip_filename):
            generate_zip_file(zip_filename, random.random() * max_size)
