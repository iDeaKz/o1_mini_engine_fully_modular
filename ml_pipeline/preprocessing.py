from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.decomposition import PCA

def create_preprocessing_pipeline():
    return Pipeline([
        ("scaler", StandardScaler()),
        ("poly_features", PolynomialFeatures(degree=2)),
        ("pca", PCA(n_components=3))
    ])
