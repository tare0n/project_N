def do_multiplication(string):
    out_string = ""
    was_asterisk = False
    buffer_number = 0
    for symbol in string:
        if not was_asterisk:
            if symbol != "*":
                out_string += symbol
            else:
                buffer_number = int(out_string[-1])
                out_string = out_string[:-1]
                was_asterisk = True
        else:
            out_string += str(buffer_number * int(symbol))
    return out_string

def do_addition(string):
    out_string = ""
    was_plus = False
    buffer_number = 0
    for symbol in string:
        if not was_plus:
            if symbol != "+":
                out_string += symbol
            else:
                buffer_number = int(out_string[-1])
                out_string = out_string[:-1]
                was_plus = True
        else:
            out_string += str(buffer_number + int(symbol))
    return out_string

def calculate(string):
    return do_addition(do_multiplication(string))
