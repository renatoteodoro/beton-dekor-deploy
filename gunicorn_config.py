import multiprocessing
import os
from pathlib import Path

# Diretório base do projeto dentro do container
BASE_DIR = Path(__file__).resolve().parent
chdir = "/app" # é onde o Dockerfile define WORKDIR

# WSGI app (pelo seu projeto: config/wsgi.py)
wsgi_app = "config.wsgi:application"

# Bind na porta interna do container (mapeada para 8000 no host)
bind = "0.0.0.0:8000"

# Cálculo de workers (2 x cores + 1) – sua VPS tem 1 vCPU
workers = 3

worker_class = "sync"
backlog = 2048

timeout = 30
graceful_timeout = 30

max_requests = 1000
max_requests_jitter = 100

accesslog = "-"
errorlog = "-"
loglevel = "info"

keepalive = 5
reload = False # manter False em produção
