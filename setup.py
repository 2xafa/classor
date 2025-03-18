from setuptools import setup, find_packages

setup(
    name="classor",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'classor=classor.main:main',
        ],
    },
    author="Safa Demirdag",
    description="IP sınıfı tarayıcı - Belirtilen IP aralığındaki aktif cihazları bulur",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/2xafa/classor",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)