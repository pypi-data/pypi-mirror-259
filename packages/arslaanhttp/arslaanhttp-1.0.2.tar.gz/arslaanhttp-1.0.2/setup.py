from setuptools import setup, find_packages

setup(
    name='arslaanhttp',
    version='1.0.2',
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
------------------
- Updated changelog and description

1.0.0 (29/02/2024)
------------------
- Updated changelog and changed version number to 1.0.0

1.0.1 (29/02/2024)
------------------
- Moved ERRHandler_404 function inside the ArslaanHTTP class to make it definable

1.0.2 (29/02/2024)
------------------
- Fixed bug where DEFAULTS_INDEX is defined in the write_html function
""",
    url='',
    author='Arslaan Pathan',
    author_email='xminecrafterfun@gmail.com',
    license='MIT',
    keywords='http',
    packages=find_packages(),
    install_requires=['']
)