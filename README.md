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
(venv) foo@bar:~/dots$ pip install -r requirements.txt
```

## Usage

Run the program with:
```console
(venv) foo@bar:~/dots$ python -m dots.cli path/to/image.jpg
```

It will output the braille representation to stdout.

## Example

### Original:
![Original image](/img/image.png)

### Text version:

Generated with:
```console
(venv) foo@bar:~/dots$ python -m dots.cli img/image.png --output braille_4x2 --invert --resize-factor 0.4
```

![Text version](/img/image_dots.png)
