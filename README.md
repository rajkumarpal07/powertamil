# powertamil
A Python suite of Tamil NLP tools.

[![License](https://img.shields.io/:license-mit-blue.svg)](./LICENSE.md)

Powertamil NLP provides a set of natural language analysis tools written in Python. It can take raw human language tamil text input and give the base forms of words, their parts of speech,...etc.


The Powertamil NLP code is written in Python 3 and licensed under the MIT Public License.


You can also install this package from PyPI using 
>pip install powertamil

# Documentation

A list of methods and their purpose is given below.

**TChar** has the following methods. The class represents a Tamil character. 

| Method          		| Meaning                                    							                 |
| --------------------| -----------------------------------------------------------------------  |
| is_vowel_marker 		| Checks for presence of Vowel marker.        							               |
| is_agaram       		| Checks for presence of Agaram.             							                 |
| is_uyir         		| Checks for presence of Uyir.               							                 | 
| is_mei          		| Checks for presence of Mei.                 							               |
| is_uyirmei      		| Checks for presence of Uyir Mei.            							               |
| is_aytham       		| Checks for presence of Aytham.              							               |
| is_tnumeral     		| Checks if the given Code Point is an Tamil numeral. 				             | 
| is_tsymbol			    | Checks if the given Code Point is an Tamil symbol.	 		                 |
| is_grantha_agaram		| Checks if the given Code Point is an grantha agaram.					           |
| is_grantha_uyirmei	| Checks for the presence of Grantha Uyir Mei. 							               |
| is_all_grantha_uyirmei| Checks for the presence of all Grantha Uyir Mei(including kshaUyirMei).|
| is_ksha_uyirmei		  | Checks for KshaUyirMei Tamil letters.									                   |
| is_sri 				      | Checks for presence of Sri Character.									                   |
| is_ksha_agaram		  | Checks for Ksha agaram.	 											                           |
| get_TChar_type		  | Identifies character Type from CodePoints of a TamilCharacter.  	       |
| get_vmarker_name		| Returns unicode standard descriptions of the vowelMarker.				         |
| get_agaram_name		  | Returns unicode standard descriptions of the Agaram.					           |
| get_uyir_name			  | Returns unicode standard descriptions of the Uyir Eluthu.				         |
| get_graphemes  		  | Iterate on code points one by one and return graphemes.				           |


**tstring** has the following methods. 

| Method          		| Meaning                                    				    |
| ------------------- | ---------------------------------------------------   |
| reverse  		        |  Reverse a Tamil word.  								              |
| length  		        |  Get the Tamil string length.  						            |
| substring 		      |  Substring for a Tamil string.  						          |
| replace  		        |  Replace a Tamil grapheme with a new grapheme. 		    |
| tace_sort_key  		  |  Sort as per TACE order.  						                |

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

Powertamil is MIT-licensed.
