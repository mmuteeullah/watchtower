from fastapi import FastAPI, BackgroundTasks
from prometheus_client import start_http_server, Gauge, REGISTRY, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import Summary, Counter
from starlette.responses import Response
import psutil
import threading
import time

app = FastAPI()

# Prometheus metrics
MEMORY_USAGE = Gauge('memory_usage', 'Memory usage of the application')
CPU_USAGE = Gauge('cpu_usage', 'CPU usage of the application')
OOM_KILL = Gauge('oom_kill', 'Out of memory kill signal')

def monitor_system():
    while True:
        process = psutil.Process()
        MEMORY_USAGE.set(process.memory_info().rss / (1024 * 1024))
        CPU_USAGE.set(process.cpu_percent(interval=1))
        time.sleep(1)

def consume_memory(target_mb):
    block_size = 1024 * 1024  # 1 MB
    memory_blocks = []
    while True:
        memory_blocks.append(bytearray(block_size))
        if (len(memory_blocks) * block_size) / (1024 * 1024) >= target_mb:
            break
        time.sleep(0.1)


def consume_cpu(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        _ = [x**2 for x in range(10000)]

@app.on_event("startup")
def startup_event():
    threading.Thread(target=monitor_system, daemon=True).start()

@app.post("/trigger/high-memory/")
async def trigger_high_memory(background_tasks: BackgroundTasks, target_mb: int = 200):
    background_tasks.add_task(consume_memory, target_mb)
    return {"status": "High memory usage simulation started"}

@app.post("/trigger/high-cpu/")
async def trigger_high_cpu(background_tasks: BackgroundTasks, duration: int = 60):
    background_tasks.add_task(consume_cpu, duration)
    return {"status": "High CPU usage simulation started"}


@app.get("/")
def healthCheck():
    return {"message": "Hello, Prometheus!"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(REGISTRY), media_type=CONTENT_TYPE_LATEST)
