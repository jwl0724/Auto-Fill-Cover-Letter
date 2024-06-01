import sys
import fileParser as fp


def main():
    docx_file = fp.create_document_object(sys.argv[1])
    if not docx_file:
        print("Could not open file")
        return
    
    fp.replace_marked_fields(docx_file, "test")
    fp.save_document_object(docx_file, f"copy_{sys.argv[1]}")
    

if __name__ == "__main__":
    main()
