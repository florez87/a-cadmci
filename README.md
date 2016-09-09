# A-CADMCI
Computer-Aided Diagnosis Tool for Mild Cognitive Impairment based on Cognitive tests and Decision Trees.

## Motivation
A-CADMCI is built on top of [scikit-learn](https://github.com/scikit-learn/scikit-learn). It was developed to aid in the diagnosis of Mild Cognitive Impairment by analyzing the scores of different cognitive tests:
- Mini–Mental State Examination (MMSE)
- Montreal Cognitive Assessment (MoCA)
- Clinical Dementia Rating (CDR)
- Global Deterioration Scale (GDS)

A-CADMCI contains decision tree classifiers trained with different databases like [ADNI](http://adni.loni.usc.edu/) to predict the level of patient's cognitive impairment and guide the clinicians in the diagnosis of the disease.

## Dependencies
A-CADMCI is tested to work under Python 3.4
The required dependencies to run the software are:
- Scikit-learn 0.17.1
- PyQt5 5.5.1
- Numpy 1.11.1
- SciPy 0.18.0
- Working C/C++ compiler

For easy installation on Windows, download and install [WinPython 3.4.4.4Qt5](https://sourceforge.net/projects/winpython/files/WinPython_3.4/3.4.4.4/). 

## Run the code
To run the code open a console in /src and use:
```python
python main.py
```

## File Structure for Model Training and Validation
Models are already trained and validated but you can also perform those tasks if you want.

### For ADNI Database
A CSV file containing the following columns:
- CDR: {0, 0.5, 1, 2, 3}
- MMSE: {0, 1, 2,..., 30}
- Age: {50, 51, 52,..., 100}
- Education: {0, 1, 2,..., 20}
- Diagnosis: {Mild, Sane, Serious}

Example of the CSV file for ADNI database:  
CDR,MMSE,Age,Education,Diagnosis  
0,30,79,16,Sane  
0,30,89,16,Sane  
0.5,29,81,16,Mild  
0.5,26,70,20,Serious  
0.5,25,69,14,Mild  

### For Caldas Database
A CSV file containing the following columns:
- CDR: {0, 0.5, 1, 2, 3}
- MMSE: {0, 1, 2,..., 30}
- MoCA: {0, 1, 2,..., 30}
- GDS: {1, 2, 3,..., 7}
- Diagnosis: {Mild, Sane, Serious}

Example of the CSV file for Caldas database:  
CDR,MMSE,MoCA,GDS,Diagnosis  
0,30,25,1,Sane  
0.5,23,14,3,Mild  
0,27,15,2,Sane  
2,13,4,4,Serious  
0,30,24,1,Sane  
