# print_t
Print Function with logging I use to debug



To run:

from print_t import *

start_logging(log_file_name)



Then just use print_t() instead of print()

print_t(message, type_m='none')

For type_m the choices are:
'hard pass'
'pass
'hard fail'
'fail'
'blue'
'warn'
'none'



Works on linux, seems to have stopped working on Windows after latest update.

