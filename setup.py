from setuptools import setup, find_packages

setup(
    name='blitzops',
    version='0.1.0',
    author='Ethan Chatfield',
    author_email='chatfield.ethan@gmail.com',
    description='An application to track workflows',
    url='https://github.com/cvache/BlitzOps-Core',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'fastapi',
        'pydantic',
        'motor',
        'pymongo',
        'pyyaml',
        'uvicorn',
        'python-multipart',
        'pydantic-sqlalchemy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
