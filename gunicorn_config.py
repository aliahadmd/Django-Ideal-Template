import multiprocessing

bind = "127.0.0.1:8001"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "/home/dev/app/Django-Ideal-Template/gunicorn-access.log"
errorlog = "/home/dev/app/Django-Ideal-Template/gunicorn-error.log"