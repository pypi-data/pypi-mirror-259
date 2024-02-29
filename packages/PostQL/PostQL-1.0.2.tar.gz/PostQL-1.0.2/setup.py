from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PostQL",
    version="1.0.2",
    description="Python wrapper for Postgres",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Abel Tavares",
    url="https://github.com/abeltavares/postql",
    author_email="abelst9@gmail.com",
    project_urls={
        "Homepage": "https://abeltavares.github.io/PostQL/",
        "Repository": "https://github.com/abeltavares/postql",
    },
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "postql=postql.cli:main",
        ],
    },
    install_requires=[
        "psycopg2-binary",
        "tabulate",
        "prompt_toolkit",
        "termcolor",
        "boto3",
        "openpyxl",
        "pyarrow",
    ],
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Database",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
