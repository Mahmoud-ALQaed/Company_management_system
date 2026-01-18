import time

def pause():
    time.sleep(3)

def validate_positive_int(value):
    if not value.isdigit():
        return False
    if int(value) <= 0:
        return False
    return True

def validate_name(value):
    return bool(value)

def validate_age(value):
    if not value.isdigit():
        return False
    if int(value) < 18:
        return False
    return True

def validate_bonus(value):
    if not value.isdigit():
        return False
    if int(value) < 0:
        return False
    return True

def Check_data(departments, data=None):
    found = False
    if data:
        for dept in departments:
            if dept.employees:
                found = True
                break
    else:
        for dept in departments:
            if not dept.employees:
                found = True
                break
    return found
