import setuptools

with open("Readme.md","r",encoding="utf-8") as f:
    long_description=f.read()
    
__version__="0.0.0"

REPO_NAME="KIDNEY-DISEASE-CLASSIFICATION-MLFLOW-DVC"
AUTHOR_USER_NAME="deepakrajbhar15"
SRC_REPO="CNNCLASSIFIER"
AUTHOR_EMAIL="deepakrajbhar363@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "bug tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
                )
