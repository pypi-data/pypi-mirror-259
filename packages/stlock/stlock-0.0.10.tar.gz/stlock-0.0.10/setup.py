from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(name='stlock',
      version='0.0.10',
      description='Python auth lib for https://iam.stlcode.ru service',
      packages=['stlock'],
      author="Smart Techno Lab",
      author_email='office@stl.im',
      zip_safe=False,
      install_requires=["requests", "pyjwt"],
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Development Status :: 3 - Alpha",
          ],
      )

