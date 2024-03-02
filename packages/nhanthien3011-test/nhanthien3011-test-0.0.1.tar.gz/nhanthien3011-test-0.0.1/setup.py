from setuptools import setup, find_packages

setup(
    name="nhanthien3011-test",
    version="0.0.1",
    author="Nguyen Thien Nhan",
    author_email="nhanthien.tnn@gmail.com",
    url="https://github.com/nhanth301",
    description="An application that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["cloudquicklabs1 = src.main:main"]},
)