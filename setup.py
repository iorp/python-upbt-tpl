from setuptools import setup, find_packages

setup(
    name="mylibrary",
    version="1.0.0",
    description="Your package description",
    author="Iorp",
    author_email="your@email.com",
    packages=find_packages(),
    install_requires=[],
    zip_safe=True,  # Set zip_safe to True
)