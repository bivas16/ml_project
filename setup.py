from setuptools import find_packages, setup

HYPHEN_E = "-e ."

def get_requirements(file_path:str):
    requirements = []
    with open(file_path) as fileobj:
        requirements=fileobj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)

    return requirements



setup(
    name="ml_project",
    version="0.0.1",
    author="bivas",
    author_email="bivasbsht4@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements("requirements.txt")
    )