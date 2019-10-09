
def validate_not_empty(data):
    status = True
    if len(data) == 0:
        status = False
    return status


def validate_data(data, keys=["message", "phone"]):
    status = validate_not_empty(data)
    errors = {}
    if status:
        for x in keys:
            if not data.get(x, False):
                errors[x] = "{} required and Not found".format(x)
    return errors
