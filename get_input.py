def get_input(msg, data_type='string'):
    """asks user for input with a prompt = msg and waits until user inputs
    data of the correct data_type"""
    """Returns the input data"""

    if data_type == 'int':
        while True:
            try:
                data = int(input(msg))
                if type(data)=='int':
                    break
            except ValueError:
                print("Please enter an integer value.")

    elif data_type == 'str':
           while True:
            try:
                data = input(msg)
            except ValueError:
                print("Please enter a string value.")

    elif data_type == 'float':
           while True:
            try:
                data = float(input(msg + " : "))
            except ValueError:
                print("Please enter a float value.")

    
