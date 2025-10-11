# Hyperparameter Search and Optimization Details

This document summarizes the hyperparameter search space explored for all model components using **Grid Search** and the **best configurations** obtained. All experiments were conducted with five random seeds, and early stopping was applied to ensure convergence stability. 

---

## 🔹 LoRA Fine-Tuning (Embedding Models)

| Parameter | Search Space | Optimal Value |
|------------|---------------|----------------|
| r (rank) | [4, 8] | 8 |
| α (scaling factor) | [8, 16, 32] | 32 |
| Dropout | [0.05, 0.1, 0.2] | 0.1 |
| Target Modules | [["query", "value"], ["key", "value"], ["query", "key"], ["query", "key", "value"]] | ["key", "value"] |

---

## 🔹 Classifier-Level Grid Search

### Random Forest
| Parameter | Search Space | Optimal Value |
|------------|---------------|----------------|
| n_estimators | [100, 200, 300, 400] | 400 |
| max_depth | [10, 20, 30, None] | 20 |
| min_samples_split | [2, 5, 10] | 5 |
| min_samples_leaf | [1, 2, 4] | 1 |
| max_features | ['sqrt', 'log2'] | 'sqrt' |
| bootstrap | [True, False] | True |

---

### Extra Trees
| Parameter | Search Space | Optimal Value |
|------------|---------------|----------------|
| n_estimators | [100, 200, 300, 400] | 400 |
| max_depth | [10, 20, 30, None] | 20 |
| min_samples_split | [2, 5, 10] | 5 |
| min_samples_leaf | [1, 2, 4] | 1 |
| max_features | ['sqrt', 'log2'] | 'sqrt' |

---

### XGBoost
| Parameter | Search Space | Optimal Value |
|------------|---------------|----------------|
| n_estimators | [100, 200, 300] | 200 |
| learning_rate | [0.01, 0.05, 0.1] | 0.1 |
| max_depth | [3, 6, 10] | 6 |
| subsample | [0.7, 0.8, 1.0] | 0.8 |
| colsample_bytree | [0.7, 0.8, 1.0] | 0.8 |
| gamma | [0, 1, 5] | 0 |
| reg_alpha | [0, 0.5, 1] | 0 |
| reg_lambda | [1, 1.5, 2] | 1 |

---

### LightGBM
| Parameter | Search Space | Optimal Value |
|------------|---------------|----------------|
| n_estimators | [100, 200, 300, 400] | 400 |
| learning_rate | [0.01, 0.05, 0.1] | 0.1 |
| max_depth | [-1, 10, 20, 30] | -1 |
| num_leaves | [31, 50, 100] | 31 |
| min_child_samples | [20, 40, 60] | 20 |
| subsample | [0.8, 1.0] | 1.0 |
| colsample_bytree | [0.8, 1.0] | 1.0 |

---

## 🔹 Feed-Forward Neural Network (FFNN)

| Parameter | Search Space | Optimal Value |
|------------|---------------|----------------|
| hidden_dim | [64, 128, 256] | 256 |
| dropout | [0.1, 0.2, 0.3, 0.5] | 0.3 |
| learning_rate | [1e-3, 1e-4, 1e-5] | 1e-3 |
| batch_size | [16, 32, 64] | 64 |
| num_hidden_layers | [1, 2, 3, 5] | 5 |
| epochs | [5, 10, 20, 50] | 5 |

**Best FFNN Accuracy:** 0.7368

---

### Notes

- All searches were performed using **GridSearchCV** (or equivalent manual loops for non-Sklearn models).
- LoRA fine-tuning and embedding generation were performed solely on the **training split** to prevent data leakage.
- Model selection and reporting were based on **mean performance across 5 random seeds**.
- Convergence stability was verified through early stopping on validation loss.
