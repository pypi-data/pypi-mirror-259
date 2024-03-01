from setuptools import setup, find_packages

setup(
    name="odoo_restart",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fabric",
    ],
    entry_points={
        "console_scripts": [
            "odoo_restart = odoo_restart.restart:main",
        ],
    },
    author="mohamed MASSTOUR",
    author_email="masstour01@gmail.com",
    description="Script to restart Odoo inside a Docker container",
    url="https://github.com/yourusername/odoo_restart",
)
