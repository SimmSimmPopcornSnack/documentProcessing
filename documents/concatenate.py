# https://qiita.com/c00lkid/items/e5979f7a68398ff3cce2

import os
import pathlib
from google.cloud import vision
import fitz
output_directory = ".\\documents\\output_summary\\"

directory = ".\documents\output"
# os.chdir(directory)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
with open(output_directory + "output_concatenated_filename.txt", "w+", encoding="utf-8") as f_out:
    for filename in os.listdir(directory):
        with open(directory + "\\" + filename, "r", encoding="utf-8") as f_in:
            in_text = f_in.read() # read a whole file
            f_out.write(f"-[ファイル名:{filename}]---------------------------------------\n")
            f_out.write(in_text)
            f_out.write("\n")

