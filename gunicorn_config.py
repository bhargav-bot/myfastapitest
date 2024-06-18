import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:8006"
worker_class = "uvicorn.workers.UvicornWorker"
