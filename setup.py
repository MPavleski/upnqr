from setuptools import setup, find_packages

setup(
    name="upnqr",
    version="0.1.0",
    description="A module for generating UPN QR codes.",
    author="shrx",
    author_email="differenxe@gmail.com",
    license="GPL3",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "qrcodegen",
        "Pillow",
    ],
    python_requires=">=3.7",
)
