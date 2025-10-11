# Impact of Different Fine-Tuning Strategies on Embedding Models over the ANN Classifier
*(Java)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 70.1 | 69.5 | **72.1** |
| BAAI BGE             | 71.5 | 70.7 | **73.4** |
| InstructorXL         | 70.8 | 70.1 | **72.0** |
| CodeBERT             | 67.7 | 66.8 | **69.1** |
| BERT                 | 67.1 | 65.9 | **67.4** |

*(JavaScript)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 67.3 | 66.8 | **69.8** |
| BAAI BGE             | 68.0 | 67.5 | **70.7** |
| InstructorXL         | 67.6 | 67.0 | **69.4** |
| CodeBERT             | 65.0 | 64.3 | **67.0** |
| BERT                 | 63.4 | 62.8 | **64.9** |

*(C++)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 66.9 | 66.3 | **68.3** |
| BAAI BGE             | 67.6 | 67.0 | **69.8** |
| InstructorXL         | 66.8 | 66.2 | **67.8** |
| CodeBERT             | 64.2 | 63.6 | **65.5** |
| BERT                 | 62.8 | 62.2 | **63.6** |

*(Python)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 61.3 | 60.6 | **63.2** |
| BAAI BGE             | 62.0 | 61.2 | **63.9** |
| InstructorXL         | 61.6 | 60.8 | **62.6** |
| CodeBERT             | 59.3 | 58.7 | **60.5** |
| BERT                 | 57.8 | 57.1 | **58.7** |

*(Merged Dataset)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 66.7 | 66.0 | **68.0** |
| BAAI BGE             | 67.3 | 66.6 | **68.7** |
| InstructorXL         | 66.4 | 65.8 | **67.5** |
| CodeBERT             | 64.0 | 63.3 | **65.2** |
| BERT                 | 62.5 | 61.9 | **63.5** |
