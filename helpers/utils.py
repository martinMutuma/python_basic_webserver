import phonenumbers


def validate_not_empty(data):
    status = True
    if len(data) == 0:
        status = False
    return status


def validate_data(data, keys=["message", "phone"]):
    errors = {}
    for x in keys:
        try:
            data[x]

            if type(data[x]) == str and len(data[x].rstrip()) < 3:
                errors[x] = "{} did not meet length requirement".format(x)
        except:
            errors[x] = "{} required and Not found".format(x)
    return errors


def validate_phones(phones=[]):
    cphones = []
    errors = []
    for phone in phones:
        x = phone
        if x.startswith('0'):
            x = '+254'+x
        try:
            ph = phonenumbers.parse(
                x, phonenumbers.region_code_for_country_code('KE'))
        except:
            pass

        if phonenumbers.is_valid_number(ph):
            cphones.append(phonenumbers.format_number(
                ph, phonenumbers.PhoneNumberFormat.E164))
        else:
            errors.append(phone)

    return dict(phones=cphones, errors=errors)
