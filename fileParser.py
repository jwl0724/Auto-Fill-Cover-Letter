import docx
import re


REGEX_EXPRESSION = "\[.*?\]"


def create_document_object(filename: str):
    try: 
        return docx.Document(f"testFiles/{filename}")
    except docx.opc.exceptions.PackageNotFoundError: 
        return None


# will replace replacement_text with *replacement_text later on
def replace_marked_fields(doc_object: docx.Document, replacement_text: str):
    for paragraph in doc_object.paragraphs:
        paragraph.text = re.sub(REGEX_EXPRESSION, replacement_text, paragraph.text)


def save_document_object(doc_object: docx.Document, filename: str):
    try:
        doc_object.save(f"output/{filename}")
        print(f"{filename} succesfully saved")
    except PermissionError:
        print("Permission error, perhaps the file is already opened?")