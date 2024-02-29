import setuptools

with open("README.md", "r", encoding = 'utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="darkskyutils", # Replace with your own username
    version="0.1.0",
    author="Darksky",
    author_email="2290168728@qq.com",
    description="Useful tool classes including log, config, tcp, etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DarkskyX15/darkskyutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    license = 'BSD License',
    requires= ['pycryptodome'],
    python_requires='>=3.9',
)