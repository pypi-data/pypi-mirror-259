from setuptools import setup


setup(
    name="common_flask_utils",
    version="0.1.0",
    author="Evanston Law",
    author_email="evanstonlaw555@gmail.com",
    url="https://github.com/Evan-acg/common_flask",
    description="Common Flask Utilities",
    packages=["packages"],
    install_requires=["Flask", "Flask-SQLAlchemy", "python-i18n"],
)
