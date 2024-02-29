from setuptools import setup, find_packages

setup(
    name='arslaanhttp',
    version='0.0.3',
    description='A simple HTTP server.',
    long_description="ArslaanHTTP is a simple HTTP server based on Python's http.server module." + '\n\n' + """
Changelog
=========

0.0.1 (29/02/2024)
------------------
- First Release

0.0.2 (29/02/2024)
------------------
- Fixed install error

0.0.3 (29/02/2024)
- Updated changelog and description
""",
    url='',
    author='Arslaan Pathan',
    author_email='xminecrafterfun@gmail.com',
    license='MIT',
    keywords='http',
    packages=find_packages(),
    install_requires=['']
)