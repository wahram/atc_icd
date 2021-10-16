# Identification of diagnosis-related contraindications from prescription data alone

Collection scripts for data analysis and classification algorithms described in 'Use of medication data alone to identify diagnoses and related contraindications: application of algorithms to close a common documentation gap' by Andrikyan et al. (under review)

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