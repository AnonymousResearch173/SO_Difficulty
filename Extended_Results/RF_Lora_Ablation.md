# Impact of Different Fine-Tuning Strategies on Embedding Models over the RF Classifier
*(Java)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 71.2 | 70.4 | **73.3** |
| BAAI BGE             | 72.5 | 71.6 | **74.6** |
| InstructorXL         | 71.8 | 71.1 | **73.1** |
| CodeBERT             | 68.4 | 67.5 | **70.0** |
| BERT                 | 67.9 | 66.5 | **68.3** |

*(JavaScript)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 68.3 | 67.8 | **70.8** |
| BAAI BGE             | 69.1 | 68.6 | **71.6** |
| InstructorXL         | 68.5 | 68.0 | **70.4** |
| CodeBERT             | 65.8 | 65.1 | **67.7** |
| BERT                 | 64.2 | 63.6 | **65.8** |

*(C++)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 67.9 | 67.3 | **69.4** |
| BAAI BGE             | 68.7 | 68.0 | **70.9** |
| InstructorXL         | 67.8 | 67.1 | **68.6** |
| CodeBERT             | 65.1 | 64.4 | **66.1** |
| BERT                 | 63.7 | 63.1 | **64.3** |

*(Python)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 62.3 | 61.5 | **64.2** |
| BAAI BGE             | 63.0 | 62.1 | **64.7** |
| InstructorXL         | 62.6 | 61.8 | **63.4** |
| CodeBERT             | 60.3 | 59.6 | **61.2** |
| BERT                 | 58.8 | 58.0 | **59.4** |

*(Merged Dataset)*

| Embedding Model     | Base (Acc %) | Fully Tuned (Acc %) | LoRA (Acc %) |
|----------------------|--------------|----------------------|---------------|
| all-MiniLM-L6-v2     | 67.8 | 67.1 | **69.0** |
| BAAI BGE             | 68.4 | 67.7 | **69.3** |
| InstructorXL         | 67.5 | 66.8 | **68.5** |
| CodeBERT             | 65.0 | 64.2 | **66.1** |
| BERT                 | 63.5 | 62.8 | **64.4** |
