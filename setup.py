from setuptools import find_packages, setup


install_requires = ("jsonschema", "strict-rfc3339", "rfc3987", "webcolors")
dependency_links = ["git+https://github.com/julian/jsonschema.git#egg=jsonschema-3"]


setup(
    name="json-schema-checker",
    description="Strictly checks that a json schema is valid",
    author="manycoding",
    license="MIT",
    url="https://github.com/manycoding/json-schema-checker",
    platforms=["Any"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    zip_safe=True,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.7",
)
