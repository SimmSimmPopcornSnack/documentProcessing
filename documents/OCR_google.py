# https://qiita.com/c00lkid/items/e5979f7a68398ff3cce2

import os
import pathlib
from google.cloud import vision
import fitz
output_directory = ".\\documents\\output\\"

def extract_text(filename):
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./secret/focused-heading-452613-m6-553d63df6c63.json"
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./secret/client_secret_813796996886-u9622f69a9tqt6vcfotvfbia11luehof.apps.googleusercontent.com"
    client = vision.ImageAnnotatorClient()
    # with open(filename, "rb") as file:
    #     content = file.read()
    with fitz.open(filename) as doc:
        outputText = ""
        for i in range(doc.page_count):
            page = doc.load_page(i)
            pixmap = page.get_pixmap(dpi=300)
            img = pixmap.tobytes()
            image = vision.Image(content=img)
            response = client.text_detection(image=image)
            texts = response.text_annotations
            result = texts[0].description if texts else None

            if response.error.message:
                raise Exception(
                    "{}\nFor more info on error message, check:"
                    "https://cloud.google.com/apis/design/errors".format(response.error.message)
                )
            # add new-line character if not the first page (index starts with 0)
            if i > 0:
                outputText += "\n"
            outputText += result
            # print(f"Text: {result}")
        # output to file
        outputFile = pathlib.Path(filename).stem + ".txt"
        fullpath = output_directory + outputFile
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        with open(fullpath, "w+", encoding="utf-8") as f:
            f.write(outputText)

# directory = ".\documents\input"
# for filename in os.listdir(directory):
#     extract_text(directory + "\\" + filename)
    
extract_text(".\documents\input\\20250418\７年４月１８日　準備書面1.pdf")
