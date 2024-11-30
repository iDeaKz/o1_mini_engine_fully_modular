from celery import Celery, Task
import logging
from typing import Dict

app = Celery('tasks', broker='redis://localhost:6379/0')

class DataProcessingTask(Task):
    def on_failure(self, exc: Exception, task_id: str, args: tuple, kwargs: dict, einfo) -> None:
        logging.error(f"Task {task_id} failed due to {exc}")

@app.task(bind=True, base=DataProcessingTask, max_retries=3, default_retry_delay=5)
def process_data(self, data: Dict[str, str]) -> str:
    try:
        input_data = data['input']
        output_data = data['output']
        result = f"Processed {input_data} into {output_data}"
        return result
    except KeyError as e:
        raise self.retry(exc=e)
