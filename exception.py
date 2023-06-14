import sys


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)



def error_message_detail(error_message, error_detail=None):
    if error_detail is None:
        return error_message
    elif isinstance(error_detail, (list, tuple)):
        _, _, exc_tb = error_detail
        return f'{error_message}\n{str(exc_tb)}'
    else:
        return f'{error_message}\n{str(error_detail)}'


    def __str__(self):
        return self.error_message
