# powertamil
A Python suite of Tamil NLP tools.

[![License](https://img.shields.io/:license-mit-blue.svg)](./LICENSE.md)

Powertamil NLP provides a set of natural language analysis tools written in Python. It can take raw human language tamil text input and give the base forms of words, their parts of speech,...etc.


The Powertamil NLP code is written in Python 3 and licensed under the MIT Public License.


You can also install this package from PyPI using 
>pip install powertamil

# Documentation

A list of methods and their purpose is given below.

tcharacter has the following methods. The class represents a Tamil character. 

| Method          | Meaning                                    |
| ----------      | ------------------------------------------ |
| is_vowel_marker | Checks for presence of Vowel marker        |
| is_agaram       | Checks for presence of Agaram              |
| is_uyir         | Checks for presence of Uyir                |
| is_mei          | Checks for presence of Mei                 |
| is_uyirmei      | Checks for presence of Uyir Mei            |
| is_aytham       | Checks for presence of Aytham              |







# Features
1. Processing of Tamil letters and Tamil strings.
2. Conversion of UTF8 tamil to Tace16 tamil.
3. Lexicographic sorting of tamil words.

More Features coming soon....!

# Key Goals of Powertamil
1. Provide a clear, standard API for NLP processing and analysis in Python
2. Provide a foundation library for other projects
3. Enable high performance and scalable NLP processing
4. Work with big data platforms such as Apache Spark or Hadoop

# License

powertamil is MIT-licensed.
