import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occured python file: " + file_name + " at line number: " + str(exc_tb.tb_lineno) + " with error message: " + str(error)
    return error_message



class SignException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: str
        :param error_detail: sys
        """
        
        super().__init__(error_message_detail(error_message, error_detail))
        
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )
        
    def __str__(self):
        return self.error_message