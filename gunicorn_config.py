import multiprocessing

# Number of workers = (2 x CPU cores) + 1
workers = multiprocessing.cpu_count() * 2 + 1
# Use sync worker for WSGI
worker_class = 'sync'
# Maximum number of requests a worker will process before restarting
max_requests = 1000
# Maximum number of requests a worker will process before restarting
max_requests_jitter = 50
# Timeout for worker processes
timeout = 120
# Keep-alive connections
keepalive = 5
# Maximum number of pending connections
backlog = 2048
# Maximum number of clients a single process can handle
worker_connections = 1000
# Preload the application
preload_app = True 