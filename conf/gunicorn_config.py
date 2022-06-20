#command='/home/jitendra/.local/bin/gunicorn'
##pythonpath='/usr/bin/python3'
#pythonpath='/home/jitendra/website-project'
#bind='127.0.0.1:8000'
#workers = 3


import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
