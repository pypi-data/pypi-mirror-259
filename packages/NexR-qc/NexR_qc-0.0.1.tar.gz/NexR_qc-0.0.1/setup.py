from setuptools import find_packages, setup

setup(
    name="NexR_qc",
    version="0.0.1",
    description="PYPI tutorial package creation written by NexR-qc",
    author="mata.lee",
    author_email="ldh3810@gmail.com",
    url="https://github.com/mata-1223/Quality-Check-Module",
    install_requires=[
        "tqdm",
        "pandas",
        "scikit-learn",
    ],
    packages=find_packages(exclude=[]),
    keywords=["qc", "NexR", "mata.lee", "QualityCheck", "python", "python tutorial", "pypi"],
    python_requires=">=3.6",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
