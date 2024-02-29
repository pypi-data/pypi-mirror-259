from setuptools import setup, find_packages

setup(
    name='quantscripts',
    version='0.1.3',
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
    description='A package for calculating statistical data in finance',
    long_description=open('README.md').read(),
    url='https://github.com/tonyyang1223/quantscripts.git',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/tonyyang1223/quantscripts.git',
    },
)

