def detect_fault(temp, vib):
    if temp > 75 or vib > 4.5:
        return "ALERT"
    elif temp > 60:
        return "WARNING"
    else:
        return "NORMAL"
