import re


def validate_email_pattern(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def validate_email_domain(email):
    domains = ("@student.wethinkcode.co.za", "@wethinkcode.co.za")
    return email.endswith(domains)


def validate_email(email):
    return validate_email_pattern(email) and validate_email_domain(email)


def validate_time(time):
    try:
        hours, minutes = map(int, time.split(":"))
        if 0 <= hours < 24 and 0 <= minutes < 60:
            return True
        else:
            return False
    except (ValueError, AttributeError):
        return False
