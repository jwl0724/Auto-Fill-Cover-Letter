import sys
import fileParser as fp
import datetime

def main():
    try:
        parser = fp.parser(sys.argv[1])
    except FileNotFoundError:
        print(f"{sys.argv[1]} could not be found, exiting program")
        return
    parser.set_marked_field("date", get_current_date())
    parser.replace_marked_fields()
    parser.save(f"filled_{sys.argv[1]}")
    

def get_current_date():
    date = datetime.datetime.now()
    month = date.strftime("%B")
    day = date.strftime("%d")
    year = date.strftime("%Y")
    return f"{month} {day}, {year}"


if __name__ == "__main__":
    main()
