from setuptools import setup


__project__ = "goodnightProject"
__version__ = "0.0.1"
__description__ = "to get a smile from your kid before bed"
__packages__ = ["loveInLights"]
__author__ = "Mam"
__authoremail__ = "mam@happy.com"
__classifiers__ = "classifiers" 

keywords = ["raspberry", "learning"]

setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,    
    authoremail = __authoremail__,    
    classifiers = __classifiers__,
)

"""Create a list of classifiers and pass it to the set up function"""

__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
]

