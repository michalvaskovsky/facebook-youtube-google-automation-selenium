# -*- coding: utf-8 -*-

import traceback
import sys
import os

def func_name():
    "Return name of callee function"
    return traceback.extract_stack(None, 2)[0][2]

# exception_handler.generic_exception_handler_s(e, exception_handler.func_name())
def generic_exception_handler_s(e, func):
    "Function to print details of exception. Return string"
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return "Exception. handled in={} type={} file={} line={} detail={}"\
           .format(func, exc_type, fname, exc_tb.tb_lineno, e)

# exception_handler.generic_exception_handler(e, exception_handler.func_name())
def generic_exception_handler(e, func):
    "Function to print details of exception"
    print (generic_exception_handler_s(e, func))





