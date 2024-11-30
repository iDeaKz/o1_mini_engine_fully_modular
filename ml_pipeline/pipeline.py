from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.decomposition import PCA
from xgboost import XGBClassifier
import numpy as np

def create_ml_pipeline() -> Pipeline:
    pipeline = Pipeline([
        ('features', FeatureUnion([
            ('poly', PolynomialFeatures(degree=2, include_bias=False)),
            ('scaler', StandardScaler()),
            ('pca', PCA(n_components=5))
        ])),
        ('classifier', XGBClassifier(use_label_encoder=False, eval_metric='logloss'))
    ])
    return pipeline
