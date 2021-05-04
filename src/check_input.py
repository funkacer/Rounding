def check_input(inp, lst):
    """
    Check if input is in the list of options.

    Args:
        (str) inp - user input to check
        (list) lst - list of options to choose from
    Returns:
        (str) out - selected option from list or None
    """
    found = 0
    for inp_check in lst:
        #print(inp_check)
        if inp_check.startswith(inp):
            out = inp_check
            found += 1
    if found == 1:
        print('OK, you have chosen ' +  out.title() + '.\n')
    else:
        out = None
        print('Your answer fits to {} possible options. Please try again.'.format(found))
    return out
