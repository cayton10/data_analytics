# Health Insurance Data Analysis

## Purpose
This project is the culmination of part I of the Data Science Foundations module; Data Science career path from Codecademy. This is a free form project where the requirements are given, but very little instruction or direction is offered. The results of my work are within this directory.

## Results
The results of the analysis can be seen by navigating [here](src/us-medical-insurance-costs.ipynb) and viewing the Jupyter notebook kept for processing and experimenting with data. Notes have been added about scope of work, hypotheses, arithmetic outputs, etc.

## Project Structure
The directories are structured such that the meat and potatoes of the project are pressented up front within the src directory. The results of analysis are most likely what we care about, so that document is stored in the root of the code (src) file. In order to practice writing my own modules and importing them, a [functions directory](src/functions/) was made to store pure functions which are used in the analysis of this project. This serves two purposes:
1. Cleans up the Jupyter NB, so logic does not crowd the reading space for analysis. The notebook should present simple calculations and final results. The goal is to abstract most of the code away for presentation purposes.
2. This allows unit tests to be run against the pure functions to ensure our analysis is not error prone.

## Unit Testing
If pulling the project for yourself is desired and you would like to run unittests, some extensions will be required locally in order to 
- Run the tests themselves
- Inspect code coverage.
The unittest.py module was used to conduct tests. Ensure this is installed locally. Additionally, test coverage was analyzed using the [Coverage Gutters](https://github.com/ryanluker/vscode-coverage-gutters/blob/HEAD/example/python) VSCode extension. An example for setting up coverage for Python projects is linked to the extension name. The extension ID for Coverage Gutters is: 
ryanluker.vscode-coverage-gutters