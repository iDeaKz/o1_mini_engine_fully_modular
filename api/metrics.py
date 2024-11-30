from prometheus_client import Gauge, Histogram
from fastapi import APIRouter, Depends

# Define Prometheus metrics
REQUEST_LATENCY = Histogram("request_latency_seconds", "Latency of requests")
ACTIVE_REQUESTS = Gauge("active_requests", "Number of active requests")

router = APIRouter()

@router.middleware("http")
async def add_metrics_middleware(request, call_next):
    ACTIVE_REQUESTS.inc()
    with REQUEST_LATENCY.time():
        response = await call_next(request)
    ACTIVE_REQUESTS.dec()
    return response
