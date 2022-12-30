import os
import shutil


def main():
  # Set the directory where the files are located
  directory = './files'
  folder_directory = './folders/'

  # Get a list of all the files in the directory
  files = os.listdir(directory)


  # Open the text file containing the folder names
  with open('folder_names.txt', 'r') as f:
    folder_names = f.readlines()

  # Iterate through the list of files
  for file in files:
    # Extract the relevant information from the file name

    info = file.split('-')[0] + "_" + file.split('-')[1]

    # Determine which folder the file should be placed in
    for folder_name in folder_names:
      tmp_folder = folder_name.replace('-', '_').replace('\n', '').strip()

      if info == tmp_folder: #.replace('_', '-')

        folder_path = folder_directory + folder_name.replace('\n', '').strip()
        # Create the folder if it does not already exist
        if not os.path.exists(folder_path):
          os.mkdir(folder_path)

        # Move the file into the folder
        shutil.move(os.path.join(directory, file), os.path.join(folder_path, file))


if __name__ == "__main__":
    main()
