from setuptools import setup, find_packages


setup(
    name="python_guide",
    py_modules=["flask"],
    packages=find_packages("src"),
    package_dir={"": "src"},
)
