# dots [![Build Status](https://travis-ci.com/ekisu/dots.svg?branch=master)](https://travis-ci.com/ekisu/dots)

A simple utility to convert an image into a braille text representation.

## Installation

Create a virtualenv, if you wish:
```console
foo@bar:~$ virtualenv venv
foo@bar:~$ venv/bin/activate
```

Install the project requirements:
```console
(venv) foo@bar:~$ pip install -r requirements.txt
```

## Usage

Run the program with:
```console
(venv) foo@bar:~$ python -m dots.main path/to/image.jpg
```

It will output the braille representation to stdout.