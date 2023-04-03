<div align="center">

# Gendiff

[![hexlet-check](https://github.com/ratushnyyvm/gendiff/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ratushnyyvm/gendiff/actions/workflows/hexlet-check.yml)
[![lint and test](https://github.com/ratushnyyvm/gendiff/actions/workflows/gendiff-CI.yml/badge.svg)](https://github.com/ratushnyyvm/gendiff/actions/workflows/gendiff-CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/3fa49b4f132527790658/maintainability)](https://codeclimate.com/github/ratushnyyvm/gendiff/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3fa49b4f132527790658/test_coverage)](https://codeclimate.com/github/ratushnyyvm/gendiff/test_coverage)

</div>

---

## Description

"Gendiff" is a program that determines the difference between two data structures.  

Features of the utility:

* Supports different input formats: yaml (yml), json
* Report generation as plain text, stylish and json

---

## Dependencies

| Tool       | Version         |
|------------|-----------------|
| python     | "^3.8.1"        |
| PyYAML     | "^6.0"          |

---

## Installation

1. Clone the repository to your computer `git clone https://github.com/ratushnyyvm/gendiff.git`
2. Go to the project folder `cd gendiff`
3. Install the program `make setup`

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
