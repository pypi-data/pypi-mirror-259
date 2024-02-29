from setuptools import find_packages, setup

# https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications

setup(
    name="dateroll",
    version="0.0.14",
    description="""dateroll makes working with dates less painful.""",
    author="Anthony Malizzio",
    author_email="anthony.malizzio@disent.com",
    url="https://github.com/disentcorp/dateroll",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Utilities"
    ),
    packages=find_packages(),
    package_data={
        "dateroll": ["README.md", "LICENSE", "DOCS.md"],
        "dateroll": ["calendars/sampledata.pkl"],
    },
    include_package_data=True,
    install_requires=[
    ],
)
