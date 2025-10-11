# Effect of Data Balancing Strategies on Classification Accuracy Across Programming Languages

*(Java)*

| Classifier          | Imbalanced | Weight Balancing | SMOTE    |
| ------------------- | ---------- | ---------------- | -------- |
| Random Forest       | 72.3       | 73.4             | **74.6** |
| XGBoost             | 71.8       | 72.9             | **74.1** |
| Extra Trees         | 71.5       | 72.6             | **73.9** |
| ANN                 | 70.8       | 71.9             | **73.4** |
| SVM                 | 69.9       | 71.2             | **72.8** |
| Naive Bayes         | 66.3       | 67.2             | **68.2** |
| Logistic Regression | 63.7       | 64.9             | **65.8** |

*(JavaScript)*

| Classifier          | Imbalanced | Weight Balancing | SMOTE    |
| ------------------- | ---------- | ---------------- | -------- |
| Random Forest       | 69.3       | 70.5             | **71.6** |
| XGBoost             | 68.8       | 69.9             | **70.9** |
| Extra Trees         | 68.5       | 69.6             | **70.6** |
| ANN                 | 67.8       | 68.8             | **69.8** |
| SVM                 | 66.9       | 68.0             | **68.5** |
| Naive Bayes         | 63.2       | 63.9             | **64.6** |
| Logistic Regression | 60.9       | 62.0             | **62.9** |

*(C++)*

| Classifier          | Imbalanced | Weight Balancing | SMOTE    |
| ------------------- | ---------- | ---------------- | -------- |
| Random Forest       | 68.7       | 69.8             | **70.9** |
| XGBoost             | 68.2       | 69.2             | **70.3** |
| Extra Trees         | 67.9       | 68.9             | **69.8** |
| ANN                 | 67.1       | 68.1             | **68.9** |
| SVM                 | 66.2       | 67.1             | **67.4** |
| Naive Bayes         | 62.4       | 63.0             | **63.5** |
| Logistic Regression | 60.0       | 60.9             | **61.7** |

*(Python)*

| Classifier          | Imbalanced | Weight Balancing | SMOTE    |
| ------------------- | ---------- | ---------------- | -------- |
| Random Forest       | 63.0       | 63.9             | **64.7** |
| XGBoost             | 62.5       | 63.4             | **64.1** |
| Extra Trees         | 62.1       | 63.0             | **63.6** |
| ANN                 | 61.5       | 62.1             | **62.3** |
| SVM                 | 60.2       | 60.8             | **61.1** |
| Naive Bayes         | 56.6       | 57.2             | **57.8** |
| Logistic Regression | 54.2       | 55.0             | **55.9** |

*(Merged Dataset)*

| Classifier          | Imbalanced | Weight Balancing | SMOTE    |
| ------------------- | ---------- | ---------------- | -------- |
| Random Forest       | 67.6       | 68.5             | **69.3** |
| XGBoost             | 67.1       | 68.0             | **68.7** |
| Extra Trees         | 66.8       | 67.7             | **68.2** |
| ANN                 | 65.9       | 66.7             | **67.4** |
| SVM                 | 64.1       | 65.0             | **65.8** |
| Naive Bayes         | 60.5       | 61.4             | **62.1** |
| Logistic Regression | 58.8       | 59.5             | **60.2** |
