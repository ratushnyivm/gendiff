# Gendiff

[![Actions Status](https://github.com/ratushnyyvm/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/ratushnyyvm/python-project-lvl2/actions)
[![lint and test](https://github.com/ratushnyyvm/python-project-lvl2/actions/workflows/gendiff-CI.yml/badge.svg)](https://github.com/ratushnyyvm/python-project-lvl2/actions/workflows/gendiff-CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/80bb23f69bdce8f4bb02/maintainability)](https://codeclimate.com/github/ratushnyyvm/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/80bb23f69bdce8f4bb02/test_coverage)](https://codeclimate.com/github/ratushnyyvm/python-project-lvl2/test_coverage)

---

## Description
"Gendiff" is a program that determines the difference between two data structures.  

Features of the utility:
* Supports different input formats: yaml (yml), json
* Report generation as plain text, stylish and json

---

## Installation
1. Clone the repository to your computer `git clone https://github.com/ratushnyyvm/python-project-lvl2.git`
2. Go to the project folder `cd python-project-lvl2`
3. Install the game package `make setup`

---

## Usage

### Cli-utility
``` bash
$ gendiff -h
usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output (default: "stylish")
```

### Library
``` python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)
```

---

## Demonstration

<details>
  <summary>installation</summary>
    
  [![asciicast](https://asciinema.org/a/xHt6q1X0X2URwYCatpP1HIrrk.svg)](https://asciinema.org/a/xHt6q1X0X2URwYCatpP1HIrrk)
</details>

<details>
  <summary>stylish</summary>
    
  `gendiff path/to/file1 path/to/file2`  
  `gendiff path/to/file1 path/to/file2 -f stylish`  
  `gendiff path/to/file1 path/to/file2 --format stylish`  
  
  [![asciicast](https://asciinema.org/a/B6rfKW2tijgqN6OtvI5mhQXic.svg)](https://asciinema.org/a/B6rfKW2tijgqN6OtvI5mhQXic)
</details>

<details>
  <summary>plain</summary>
    
  `gendiff path/to/file1 path/to/file2 -f plain`  
  `gendiff path/to/file1 path/to/file2 --format plain`  
  
  [![asciicast](https://asciinema.org/a/MqsaUpAxjLWFlVutmqVsCwOLH.svg)](https://asciinema.org/a/MqsaUpAxjLWFlVutmqVsCwOLH)
</details>

<details>
  <summary>json</summary>
    
  `gendiff path/to/file1 path/to/file2 -f json`  
  `gendiff path/to/file1 path/to/file2 --format json`  
  
  [![asciicast](https://asciinema.org/a/aReCTWQHTiz3uFREkIgiaBmHf.svg)](https://asciinema.org/a/aReCTWQHTiz3uFREkIgiaBmHf)
</details>

---

The second training project from ["Python developer" course](https://ru.hexlet.io/programs/python)