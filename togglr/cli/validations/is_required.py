def is_required(message):
    def validation(token):
        if len(token) == 0:
            return message
        else:
            return True

    return validation
