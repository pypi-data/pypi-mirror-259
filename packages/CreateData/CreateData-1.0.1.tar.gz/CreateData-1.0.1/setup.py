from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r', encoding="utf-8") as f:
    return f.read()
    
setup(name='CreateData',
    version='1.0.1',
    author='denis_lvov',
    author_email='dwenlvov@gmail.com',
    description='Easy data generation',
    packages=find_packages(),
    url='https://github.com/dwenlvov/',
    project_urls={
        'Documentation': 'https://github.com/dwenlvov/CreateData/'
        },
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License'
        ],
    keywords='pandas',
    python_requires='>=3.11'
    )