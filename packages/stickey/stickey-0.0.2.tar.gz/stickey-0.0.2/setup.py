from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Make it stick is a package that allows user to upload pdf and take quick test created by AI.'

# Setting up
setup(
    name="stickey",
    version=VERSION,
    author="Kazuha",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keyword=["python"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)