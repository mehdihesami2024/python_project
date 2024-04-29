# python password generator with approach oop
welcome to the python password generator.
this program generates three types of passwords:
 1. Pin_code
 2. Random_password
 3. Memorable_password

## how to works
the password generator uses pythons `random`, `string` moduls to generate passwords on base user preferences.

1. `generate_pin` produces a numeric pin code of a desired length.
2. `generate random_password` create a random password with desired lengt contain numbers and special characters on base user preferences.
3. `generate Memorable_password` create a password on base number of words selected of an english language corpus. you can specify the seprator and whether the words should be capitalized.

## Requirement
- python 3.7+
- NLTK (Ntural language ToolKit)
 to instal NLTK, use pip:
 ```bash
 pip instal nltk
 ```
  After install NLTK yiu need to download the "words" corpus.
 run python and type these comands:
 
 ```python
import nltk
nltk.download("words")
```

## Running the project
Ensure that you have all required dependencies installed.
you can set your `PYTHONPATH`, 
navigate to the "src" directory and run project using the following comands:

```bash
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory/src"
python pass_generator.py
```
(Be sure o replace `/your/path/to/main/directory/` with actual pass to your srcdirectory)


## user inputs
By editing the values in the main function, you can specify the length of the password for each type of password to generate. You can also decide whether to include numbers or symbols for the random password generator, or the number of words and if words should be capitalized for the memorable password generator. 

