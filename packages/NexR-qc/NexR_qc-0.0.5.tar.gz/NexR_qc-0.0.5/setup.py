from setuptools import find_packages, setup

setup(
    name="NexR_qc",
    version="0.0.5",
    description="PYPI tutorial package creation written by NexR-qc",
    author="mata.lee",
    author_email="ldh3810@gmail.com",
    url="https://github.com/mata-1223/NexR_qc",
    install_requires=[
        "numpy",
        "pandas",
        "openpyxl",
    ],
    packages=find_packages(exclude=[]),
    keywords=["qc", "NexR", "mata.lee", "NexR_qc", "python", "python tutorial", "pypi"],
    python_requires=">=3.7",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
