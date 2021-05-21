from install37 import setup
from python_generator.__meta__ import __version__

if __name__ == "__main__":
    setup(
        name="python_generator",
        version=__version__,
        author="Gabriel Amare", 
        author_email="gabriel.amare.dev@gmail.com",
        description="tool to generate python code", 
        url="https://github.com/GabrielAmare/PythonGenerator", 
        packages=["python_generator"], 
        classifiers=[], 
        python_requires=">=3.7"
    )
