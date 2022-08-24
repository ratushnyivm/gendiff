# Gendiff

[![Actions Status](https://github.com/ratushnyyvm/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/ratushnyyvm/python-project-lvl2/actions)
[![lint and test](https://github.com/ratushnyyvm/python-project-lvl2/actions/workflows/gendiff-CI.yml/badge.svg)](https://github.com/ratushnyyvm/python-project-lvl2/actions/workflows/gendiff-CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/80bb23f69bdce8f4bb02/maintainability)](https://codeclimate.com/github/ratushnyyvm/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/80bb23f69bdce8f4bb02/test_coverage)](https://codeclimate.com/github/ratushnyyvm/python-project-lvl2/test_coverage)

---

## Description
Gendiff - json/yaml difference generator

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
    
  [![asciicast](https://asciinema.org/a/LTGDQ0FKulquqcR4nOFHLKJAQ.svg)](https://asciinema.org/a/LTGDQ0FKulquqcR4nOFHLKJAQ)
</details>

<details>
  <summary>brain_calc</summary>
    
  ### win
  [![asciicast](https://asciinema.org/a/wlH3YnemKkvupRP4Bk8SBgHlm.svg)](https://asciinema.org/a/wlH3YnemKkvupRP4Bk8SBgHlm)

  ### loss
  [![asciicast](https://asciinema.org/a/iSlmp2GNEEx3NOxPlGTAkwEkv.svg)](https://asciinema.org/a/iSlmp2GNEEx3NOxPlGTAkwEkv)
</details>



[![asciicast](https://asciinema.org/a/x9AZ1aUHJU9sJeP44CnOP25gY.svg)](https://asciinema.org/a/x9AZ1aUHJU9sJeP44CnOP25gY)