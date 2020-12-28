# Main File

def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err
    except TypeError as err:
        return err


