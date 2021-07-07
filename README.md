# Identification of disease related contraindications from prescription data alone

Collection scripts for data analysis and classification algorithms.

### Dependencies
* Python 3.9.5
* NumPy 1.21.0
* Scikit-learn 0.24.2
* Graphviz 0.16
* statsmodels 0.12.2

### Input data
The dataset contains a csv file with `patient_id`, `icd10[1-20]` and `atc[1-25]`.
Sci-kit learn 0.24.2 decision tree classifier is not able to handle categorical variables.
Therefore, the dataset has to be one-hot encoded (e.g. by using `onehot_encoder.py`)

### License
MIT license