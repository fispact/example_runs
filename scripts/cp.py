import os
import shutil


source_dir = os.path.join('/Users/tom/Dev/system_tests')
dest_dir = os.getenv('SYSTEM_TESTS', os.sep)

file_ext = '.json'

#loop over dirs and input files
for subdir, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(file_ext) and not file.endswith(".min{}".format(file_ext)):
            pd = os.path.abspath(os.path.join(os.path.join(subdir, file), os.pardir)).split(os.sep)
            print("Source file: {}, destination file: {}".format(os.path.join(subdir, file), os.path.join(dest_dir, pd[-2], pd[-1], file)))
            shutil.copyfile(os.path.join(subdir, file), os.path.join(dest_dir, pd[-2], pd[-1], file))
