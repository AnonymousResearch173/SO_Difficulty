# Impact of Different Fine-Tuning Strategies on Embedding Models over the Extra Trees Classifier
*(Java)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 70.6 | 69.9 | **72.7** |
| BAAI BGE             | 71.8 | 71.0 | **73.9** |
| InstructorXL         | 71.1 | 70.4 | **72.4** |
| CodeBERT             | 67.9 | 67.1 | **69.5** |
| BERT                 | 67.3 | 66.1 | **67.7** |

*(JavaScript)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 67.8 | 67.2 | **70.3** |
| BAAI BGE             | 68.5 | 68.0 | **71.1** |
| InstructorXL         | 68.0 | 67.4 | **69.9** |
| CodeBERT             | 65.3 | 64.7 | **67.3** |
| BERT                 | 63.7 | 63.2 | **65.3** |

*(C++)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 67.3 | 66.8 | **68.8** |
| BAAI BGE             | 68.1 | 67.5 | **70.3** |
| InstructorXL         | 67.2 | 66.6 | **68.1** |
| CodeBERT             | 64.6 | 63.9 | **65.7** |
| BERT                 | 63.1 | 62.5 | **63.9** |

*(Python)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 61.8 | 61.1 | **63.7** |
| BAAI BGE             | 62.5 | 61.6 | **64.2** |
| InstructorXL         | 62.1 | 61.3 | **62.9** |
| CodeBERT             | 59.8 | 59.2 | **60.9** |
| BERT                 | 58.3 | 57.6 | **59.0** |

*(Merged Dataset)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 67.2 | 66.6 | **68.5** |
| BAAI BGE             | 67.8 | 67.1 | **68.9** |
| InstructorXL         | 66.9 | 66.3 | **67.9** |
| CodeBERT             | 64.5 | 63.8 | **65.7** |
| BERT                 | 63.0 | 62.3 | **63.9** |
