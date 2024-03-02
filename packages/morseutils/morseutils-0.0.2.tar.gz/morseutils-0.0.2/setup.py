import setuptools

setuptools.setup(
    name = "morseutils",
    version = "0.0.2",
    author = "Jirakit Jirapongwanich",
    author_email = "jame.jpwn@gmail.com",
    description = "A morsecode translator and player package. \nIt can translate a message to morse code and play the morse code as sound. \n Please note that player is only support on Windows",
    url = "https://github.com/jamejunj",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)