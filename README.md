# formal logic evaluator
> A small evaluator for simple expressions of formal logic written in Python

# Summary
This is a small formal logic evaluator, which I wrote for fun during an introductory maths course at university. 
This program can interpret simple expressions of formal logic and evaluates the truth value for you. 

# Installation
Just download logic_parser.py and have a fitting Python version on your PC. No other modules are needed (this is supposed to stay so in future).
All code was written and tested in version ```Python 3.8.10``` and will definitely not work in some older versions because of the type annotations.

# Usage
You have two possible ways of using my code:

1. From the CLI:
   Just call the following command in the same directory as logic_parser.py:
   ```
   python3 logic_evaluator.py
   ```
   Then the following response will come:
   ```
   Input a logic expression, the program will decide if the expression is true or false: 
   ```
   Now type in your expression, and the program will respond with the solution.

2. From another python file:
   Import the file as follows:
   ```
   from logic_evaluator import evaluate
   ```
   Now you can use the ```evaluate()``` method in your code as follows:
   ```
   evaluate(string_expression)
   ```

# Currently supported logic
I currently accept only propositional logic without any variables, which implies only this kind of expression:
``` true or (false and true => true) <=> false  ```
but not something like:
``` A or (B and C => D) <=> E  ```

**uppercase and lowercase are treated equally (not case-sensitive)*'

## Currently supported values
The only supported values for the logical expressions:
| Value | accepted representations |
| :---: | :----------------------: |
| true  | true, t, w, 1            |
| false | false, f, 0              |


## Currently supported logical operators and their precedence
I currently only support the standard operators:
| Operators       | precedence | accepted representations    |
| :-------------: | :--------: | :-------------------------: |
| not             | 1          | not, ~, -                   |
| and             | 2          | and, ^, &                   |
| or              | 3          | or, v                       |
| if ... then ... | 4          | =>, ->                      |
| if and only if  | 5          | <=>, <->, iff               |

These precedence rules are "usual" for many compilers, but not every compiler treats them the same. 
(Source: ![Wikipedia: Logical connectives](https://en.wikipedia.org/wiki/Logical_connective/))

# Found a bug? Want to add functionallity? Want to add other implementations?
If you would like to contribute to this small project in one or more of the following ways:
- Correct errors and fix bugs
- Implement further functionality and add functions
- Contribute another implementation in another programming language

If you want to contribute but don't know what to do, take a look at the issues; maybe you will find something fitting over there.

## How to contribute
Follow these steps to contribute to the project:
1. Fork the project
2. Make the changes
3. Set up a PR
4. Then wait until I or maybe others check and review the changes (this could take a while) 

## Read before contributing
Some things for writing code:
- this project is supposed to not need anything else then bare-bone python. So don't use any other packages. 
- Instead of writing large commands in code make your code readable by using descriptive naming, separation by using functions and not using hard to read shortings, oneliners and other "tricks"
- Describe what functions do by using Docstrings, take a look at the ```logic-evaluator.py```  file for example.

I'm open for new additions and changes to these standards, you can propose them by writing an issue. 

# License
All code is licensed under the MIT license; please read the ![LICENSE file](LICENSE) for more information.
