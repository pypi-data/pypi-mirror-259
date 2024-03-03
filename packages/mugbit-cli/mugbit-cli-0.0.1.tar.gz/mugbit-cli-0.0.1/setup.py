from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'create your document with the power of A.I.'
LONG_DESCRIPTION = """MugBit CLI involves creating a versatile document generation system with dynamic placeholders. Users can create customizable templates with placeholders, which are then extracted. The placeholders' values are obtained from the user through input prompts and used to fill the placeholders using an AI API. The resulting data is inserted into the document, and the final document is generated and saved. This allows users to dynamically tailor document content by interacting with an AI-based system through a user-friendly interface.

MugBit CLI relies on leveraging Artificial Intelligence for the creation of documents, PowerPoint presentations, and template filling. Our goal is to simplify, ease, and enhance the user experience, making their lives more convenient. MugBit CLI relies on Python as its underlying framework, with the backbone of its functionality deriving from the potent Gemini AI by Google."""

# Setting up
setup(
    name="mugbit-cli",
    version=VERSION,
    author="Harsh Kale",
    author_email="harshmkale.2004@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "Babel==2.14.0",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "colorama==0.4.6",
        "docxcompose==1.4.0",
        "docxtpl==0.16.8",
        "idna==3.6",
        "Jinja2==3.1.3",
        "lxml==5.1.0",
        "MarkupSafe==2.1.5",
        "python-docx==1.1.0",
        "requests==2.31.0",
        "setuptools==69.1.1",
        "six==1.16.0",
        "tqdm==4.66.2",
        "typing_extensions==4.10.0",
        "urllib3==2.2.1"
    ],
    keywords=['generate documents with A.I.', 'Artificial Intelligence', 'MS document with A.I.', 'MugBit CLI', 'Harsh Kale', 'A.I. Document', 'Create Documents with A.I.', "Document Template", "AI and Document"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)