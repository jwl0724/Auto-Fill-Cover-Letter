import sys
import fileParser as fp
import GUI as gui
import datetime

def main():
    window = gui.screen(600, 300)
    window.run()

    try:
        parser = fp.parser(sys.argv[1])
    except FileNotFoundError:
        print(f"{sys.argv[1]} could not be found, exiting program")
        return
    except PermissionError:
        print(f"Program does not have access to {sys.argv[1]}")
        return
    except fp.NoMarkedFieldsError:
        print(f"No marked field founds in the file")
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
