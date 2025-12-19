import os
import shutil


base_dir = os.getenv('SYSTEM_TESTS', os.sep)

file_ext = '.out'
line_contains = 'absorp('

#loop over dirs and input files
for subdir, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(file_ext) and 'windows_10_ifort_text' in subdir:
            print("File: {}".format(os.path.join(subdir, file)))

            f = open(os.path.join(subdir, file), 'r')
            lines = f.readlines()
            f.close()

            f = open(os.path.join(subdir, file), 'w')
            for line in lines:
                if line_contains not in line:
                    f.write(line)

            f.close()

