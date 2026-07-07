import os

from setuptools import setup, find_packages


def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    with open(requirements_path, encoding="utf-8") as requirements_file:
        return [
            line.strip()
            for line in requirements_file
            if line.strip() and not line.lstrip().startswith("#")
        ]

setup(
    name="alpha_clip",
    py_modules=["alpha_clip"],
    version="1.0",
    description="",
    author="OpenAI&ZeyiSun",
    packages=find_packages(exclude=["tests*"]),
    install_requires=read_requirements(),
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
