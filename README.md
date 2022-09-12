# Identification of diagnosis-related contraindications from prescription data alone

This repository contains collection scripts for data analysis and classification algorithms described in 'Use of medication data alone to identify diagnoses and related contraindications: Application of algorithms to close a common documentation gap' by Andrikyan et al.
https://doi.org/10.1111/bcp.15469

The basic idea of the described approach is to provide a proof of principle that key diagnosis-related contraindications can be identified based on medication data alone.
Therefore, expert-based and machine learning algorithms (decision trees) were developed to identify diagnoses based on highly specific medication patterns. The identification of the diagnoses using only medication data allows automated checks for drug-disease interactions in for example pharmacies, when no or limited amount of information regarding the diagnoses from patients exists.
The scripts apply the described approach for the diagnoses gout, epilepsy, coronary artery disease, congestive heart failure and bronchial obstruction.

### Dependencies
* Python 3.9.7
* NumPy 1.21.2
* Scikit-learn 1.0
* Graphviz 0.17
* statsmodels 0.13.0

### Input data
The dataset contains a csv file with the headers `patient_id`, `icd10[1-20]` and `atc[1-25]`.
Sci-kit learn 1.0 decision tree classifier is not able to handle categorical variables.
Therefore, the dataset has to be one-hot encoded (e.g. by using `onehot_encoder.py`)

### License
MIT license