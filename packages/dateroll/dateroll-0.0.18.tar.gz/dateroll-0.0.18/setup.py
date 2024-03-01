from setuptools import find_packages, setup

setup(
    name="dateroll",
    version="0.0.18",
    description="""dateroll makes working with dates less painful.""",
    author="Anthony Malizzio",
    author_email="anthony.malizzio@disent.com",
    url="https://github.com/disentcorp/dateroll",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Utilities",
    ],
    packages=['.'],
    include_package_data=True,
    install_requires=["python-dateutil"],
    license_files = ('LICENSE',),
    zip_safe=False
)
