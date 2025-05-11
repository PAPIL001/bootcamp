def route_line(line):
    """ Routes the line based on tags """
    if "Error" in line:
        return "error"
    elif "Debug" in line:
        return "debug"
    return "info"
