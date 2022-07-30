import setuptools

setuptools.setup(
    name="scriptlab",
    version="0.0.1",
    author="Alexander Gutierrez",
    description="scriptlab python library to interact with the scriptlab exec",
        # package_dir={
        #     "": "scriptlab"
        # },
    packages=setuptools.find_packages(where="scriptlab")
)