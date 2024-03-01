from setuptools import setup, find_packages

setup(
    name='quantscripts',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        # 在这里列出你的包的依赖项
        'pandas',
        'numpy',
        'statsmodels',
        'matplotlib',
        'scipy',
    ],
    
    author='tonyyang1223',
    author_email='tonyyang1223@gmail.com',
    long_description=open('README.md').read(),
    description='A package for calculating statistical data in finance',
    license='MIT',
    url="https://github.com/tonyyang1223/quantscripts",
    project_urls={
        'Source': 'https://github.com/tonyyang1223/quantscripts',
    },
)
