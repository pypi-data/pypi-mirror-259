from setuptools import setup, find_packages

setup(
    name='XGeoML',
    version='0.1.1',
    packages=find_packages(),
    description='A ensemble framework for explainable geospatial machine Learning models',
    author='Lingbo Liu',
    author_email='lingbo.liu@whu.edu.cn',
    license="MIT",
    install_requires=[
        'scikit-learn',
        'numpy',
        'scipy',
        'joblib',
        'pandas',
        'lime',
        'shap',
        'tqdm', 
    ],
)
