import os
import shutil

# Set the directory where the files are located
directory = '/path/to/directory'

# Get a list of all the files in the directory
files = os.listdir(directory)

# Iterate through the list of files
for file in files:
  # Extract the relevant information from the file name
  info = file.split('_')
  
  # Create a folder for each set of files
  folder = info[0]
  if not os.path.exists(folder):
    os.mkdir(folder)
  
  # Move the file into the appropriate folder
  shutil.move(os.path.join(directory, file), os.path.join(folder, file))
This is just one way to divide files based on their names and place them into separate folders. You can modify the script to fit your specific needs and use different techniques to extract the relevant information from the file names.




Regenerate response