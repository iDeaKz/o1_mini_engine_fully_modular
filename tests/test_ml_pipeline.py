import numpy as np
from ml_pipeline.pipeline import create_ml_pipeline

def test_ml_pipeline():
    X_sample = np.random.rand(10, 5)
    y_sample = np.random.randint(2, size=10)
    pipeline = create_ml_pipeline()
    pipeline.fit(X_sample, y_sample)
    predictions = pipeline.predict(X_sample)
    assert len(predictions) == 10
