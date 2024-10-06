import setuptools


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
# def read(fname):
    # return open(os.path.join(os.path.dirname(__file__), fname)).read()


__version__ = "0.0.0"
PACKAGE_NAME = "TextSummarizer"
REPO_NAME = "Text-Summarizer-using-HF-Transformer-End-to-End"
AUTHOR_USER_NAME = "a00ayad00"
AUTHOR_EMAIL = "3bdullah3yad@gmail.com"


setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer App",
    long_description=long_description,  # read('README'),
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=setuptools.find_packages(include=['src*']),
)