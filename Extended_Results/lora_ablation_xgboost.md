# Impact of Different Fine-Tuning Strategies on Embedding Models over the XGBoost Classifier
*(Java)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 70.9 | 70.2 | **73.0** |
| BAAI BGE             | 72.0 | 71.3 | **74.1** |
| InstructorXL         | 71.4 | 70.7 | **72.7** |
| CodeBERT             | 68.1 | 67.3 | **69.7** |
| BERT                 | 67.6 | 66.3 | **68.0** |

*(JavaScript)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 68.0 | 67.5 | **70.5** |
| BAAI BGE             | 68.8 | 68.2 | **71.3** |
| InstructorXL         | 68.3 | 67.8 | **70.1** |
| CodeBERT             | 65.5 | 64.8 | **67.5** |
| BERT                 | 63.9 | 63.3 | **65.5** |

*(C++)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 67.6 | 67.1 | **69.1** |
| BAAI BGE             | 68.4 | 67.7 | **70.6** |
| InstructorXL         | 67.5 | 66.9 | **68.4** |
| CodeBERT             | 64.8 | 64.1 | **65.9** |
| BERT                 | 63.4 | 62.8 | **64.1** |

*(Python)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 62.0 | 61.3 | **63.9** |
| BAAI BGE             | 62.7 | 61.8 | **64.4** |
| InstructorXL         | 62.3 | 61.5 | **63.1** |
| CodeBERT             | 60.0 | 59.4 | **61.0** |
| BERT                 | 58.5 | 57.8 | **59.2** |

*(Merged Dataset)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 67.5 | 66.9 | **68.7** |
| BAAI BGE             | 68.1 | 67.4 | **69.1** |
| InstructorXL         | 67.2 | 66.6 | **68.2** |
| CodeBERT             | 64.7 | 64.0 | **65.9** |
| BERT                 | 63.2 | 62.5 | **64.1** |
