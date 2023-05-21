import sys
import logging


def error_msg_Detail(error, error_Detail: sys):
    __, __, exc_tb = error_Detail.exc_info()

    # the exc_info exception information returns 3 things actually. Out of which we need 3rd as it contains the details of the error

    # Now get the file name and line where the error has occured

    file_name = exc_tb.tb_frame.f_code.co_filename
    line = exc_tb.tb_lineno

    # Set the format of error message we want to pass
    error_msg = " Error has occured in python script named {0}, in the line number {1}, error message is {2}".format(
        file_name, line, str(error)
    )

    return error_msg


# Now define a custom class inherited from Exception class


class CustomException(Exception):
    def __init__(self, error_msg, error_Detail: sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_Detail(error_msg, error_Detail=error_Detail)

    def __str__(self):
        return self.error_msg


# Checking if the exception handling started

# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e, sys)
