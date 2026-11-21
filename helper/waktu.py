from datetime import datetime

def time(format):
    wkt =datetime.now().strftime(format)
    return wkt