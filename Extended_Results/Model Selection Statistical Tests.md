# Statistical Analysis: Model Selection (BGE vs Other Embedding Models)

In this report, we present the statistical comparison of the BAAI BGE embedding model against other competing embedding models.  
Analyses were performed across five random seeds and five classifiers, ensuring statistical robustness.

---

## 🧩 F1 Score Comparisons

**Normality Test:**  
Shapiro–Wilk for BGE → p = **0.9170**  
✅ Data likely normal (fail to reject H₀)

**Global Difference:**  
Friedman Test → p = **0.0000**  
→ There is a **statistically significant difference** among models.

| Comparison | Wilcoxon p | Significance | Cohen’s d | Effect Size | Mean (BGE) | Mean (Other) |
|-------------|-------------|---------------|------------|--------------|--------------|---------------|
| **BGE vs MiniLM** | 0.0173 | ✅ Significant | 0.845 | Large | 74.13 | 73.06 |
| **BGE vs InstructorXL** | 0.0010 | ✅ Significant | 1.055 | Large | 74.13 | 72.65 |
| **BGE vs BERT** | 0.0000 | ✅ Significant | 4.971 | Large | 74.13 | 68.06 |
| **BGE vs CodeBERT** | 0.0000 | ✅ Significant | 2.835 | Large | 74.13 | 69.99 |

BGE significantly outperforms all competing models on the F1 metric, with **large effect sizes** across comparisons. The performance advantage is most pronounced over BERT and CodeBERT, highlighting the robustness of BGE’s contextual representations.

---

## 📊 Accuracy Comparisons

**Normality Test:**  
Shapiro–Wilk for BGE → p = **0.7754**  
✅ Data likely normal (fail to reject H₀)

**Global Difference:**  
Friedman Test → p = **0.0000**  
→ There is a **statistically significant difference** among models.

| Comparison | Wilcoxon p | Significance | Cohen’s d | Effect Size | Mean (BGE) | Mean (Other) |
|-------------|-------------|---------------|------------|--------------|--------------|---------------|
| **BGE vs MiniLM** | 0.0451 | ✅ Significant | 0.481 | Small | 74.19 | 73.49 |
| **BGE vs InstructorXL** | 0.0667 | ❌ Not Significant | 0.626 | Medium | 74.19 | 73.23 |
| **BGE vs BERT** | 0.0000 | ✅ Significant | 3.684 | Large | 74.19 | 68.59 |
| **BGE vs CodeBERT** | 0.0000 | ✅ Significant | 2.383 | Large | 74.19 | 70.36 |

While BGE shows a statistically significant improvement in Accuracy over most baselines, its margin over **MiniLM** and **InstructorXL** is relatively modest (small-to-medium effects). However, BGE remains **significantly superior** to **BERT** and **CodeBERT** with large effect sizes, reaffirming its stability and generalization strength.


---

*This markdown file accompanies the model comparison section (Table 5) in the manuscript and provides detailed statistical evidence supporting the selection of the BGE model for subsequent experiments.*
