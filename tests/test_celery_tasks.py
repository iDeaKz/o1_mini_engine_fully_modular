from celery.result import AsyncResult
from celery_tasks.tasks import process_data

def test_process_data():
    task = process_data.apply_async(args=[{"input": "raw_data", "output": "processed_data"}])
    result = AsyncResult(task.id).get(timeout=10)
    assert result == "Processed raw_data into processed_data"
