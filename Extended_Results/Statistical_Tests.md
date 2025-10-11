# Statistical Analysis Results — StackRanker Evaluation

This document presents the detailed statistical evaluation conducted for comparing **StackRanker** and baseline models (Hasan, Raida, WoLoRA, WoSMOTE, WoSPEAR).  
All tests were performed on **F1-score** and **Accuracy** metrics across five random seeds.  
Shapiro–Wilk tests were used to assess normality, followed by paired *t*-tests, Wilcoxon signed-rank tests, and computation of **Cohen’s d** effect sizes.  
Finally, Friedman tests were performed to confirm significance across models.

---

## 🧮 Shapiro–Wilk Test for Normality

### F1

| Model        | W        | p-value     | Normality |
|---------------|-----------|-------------|------------|
| Hasan         | 0.8343    | 8.9816e-04  | ❌ Non-normal |
| Raida         | 0.9213    | 5.4888e-02  | ✅ Normal |
| WoLoRA        | 0.9745    | 7.6005e-01  | ✅ Normal |
| WoSMOTE       | 0.9623    | 4.6237e-01  | ✅ Normal |
| WoSPEAR       | 0.9593    | 3.9980e-01  | ✅ Normal |
| StackRanker   | 0.9577    | 3.7014e-01  | ✅ Normal |

### Accuracy

| Model        | W        | p-value     | Normality |
|---------------|-----------|-------------|------------|
| Hasan         | 0.8692    | 4.1626e-03  | ❌ Non-normal |
| Raida         | 0.9206    | 5.2833e-02  | ✅ Normal |
| WoLoRA        | 0.9657    | 5.3915e-01  | ✅ Normal |
| WoSMOTE       | 0.9526    | 2.8724e-01  | ✅ Normal |
| WoSPEAR       | 0.9615    | 4.4426e-01  | ✅ Normal |
| StackRanker   | 0.9522    | 2.8115e-01  | ✅ Normal |

---

## 📊 Pairwise Statistical Tests (F1)

| Comparison | Wilcoxon (stat, p) | t-test (stat, p) | Cohen’s d | Interpretation |
|-------------|--------------------|------------------|------------|----------------|
| Hasan vs Raida | 117.0000, 2.3036e-01 | -1.2216, 2.3371e-01 | -0.2443 | Small effect |
| Hasan vs WoLoRA | 0.0000, 5.9605e-08 ✅ | -18.2128, 1.4816e-15 ✅ | -3.6426 | Large |
| Hasan vs WoSMOTE | 0.0000, 5.9605e-08 ✅ | -17.2467, 5.0118e-15 ✅ | -3.4493 | Large |
| Hasan vs WoSPEAR | 0.0000, 5.9605e-08 ✅ | -17.1534, 5.6558e-15 ✅ | -3.4307 | Large |
| Hasan vs StackRanker | 0.0000, 5.9605e-08 ✅ | -19.1157, 4.9850e-16 ✅ | -3.8231 | Large |
| Raida vs WoLoRA | 0.0000, 5.9605e-08 ✅ | -17.0370, 6.5804e-15 ✅ | -3.4074 | Large |
| Raida vs WoSMOTE | 0.0000, 5.9605e-08 ✅ | -16.6807, 1.0522e-14 ✅ | -3.3361 | Large |
| Raida vs WoSPEAR | 0.0000, 5.9605e-08 ✅ | -16.1597, 2.1221e-14 ✅ | -3.2319 | Large |
| Raida vs StackRanker | 0.0000, 5.9605e-08 ✅ | -17.8963, 2.1948e-15 ✅ | -3.5793 | Large |
| WoLoRA vs WoSMOTE | 2.0000, 1.7881e-07 ✅ | -8.6920, 7.0470e-09 ✅ | -1.7384 | Large |
| WoLoRA vs WoSPEAR | 0.0000, 5.9605e-08 ✅ | -11.3005, 4.2881e-11 ✅ | -2.2601 | Large |
| WoLoRA vs StackRanker | 0.0000, 5.9605e-08 ✅ | -16.9395, 7.4763e-15 ✅ | -3.3879 | Large |
| WoSMOTE vs WoSPEAR | 0.0000, 5.9605e-08 ✅ | -3.9394, 6.1408e-04 ✅ | -0.7879 | Medium |
| WoSMOTE vs StackRanker | 0.0000, 5.9605e-08 ✅ | -11.8890, 1.5146e-11 ✅ | -2.3778 | Large |
| WoSPEAR vs StackRanker | 0.0000, 5.9605e-08 ✅ | -10.9109, 8.7227e-11 ✅ | -2.1822 | Large |

---

## 📈 Pairwise Statistical Tests (Accuracy)

| Comparison | Wilcoxon (stat, p) | t-test (stat, p) | Cohen’s d | Interpretation |
|-------------|--------------------|------------------|------------|----------------|
| Hasan vs Raida | 0.0000, 5.9605e-08 ✅ | -8.4510, 1.1794e-08 ✅ | -1.6902 | Large |
| Hasan vs WoLoRA | 0.0000, 5.9605e-08 ✅ | -16.3670, 1.6016e-14 ✅ | -3.2734 | Large |
| Hasan vs WoSMOTE | 0.0000, 5.9605e-08 ✅ | -16.7459, 9.6492e-15 ✅ | -3.3492 | Large |
| Hasan vs WoSPEAR | 0.0000, 5.9605e-08 ✅ | -17.4594, 3.8136e-15 ✅ | -3.4919 | Large |
| Hasan vs StackRanker | 0.0000, 5.9605e-08 ✅ | -18.4009, 1.1762e-15 ✅ | -3.6802 | Large |
| Raida vs WoLoRA | 2.0000, 1.7881e-07 ✅ | -9.0754, 3.1561e-09 ✅ | -1.8151 | Large |
| Raida vs WoSMOTE | 0.0000, 5.9605e-08 ✅ | -11.4701, 3.1650e-11 ✅ | -2.2940 | Large |
| Raida vs WoSPEAR | 0.0000, 5.9605e-08 ✅ | -12.3736, 6.6080e-12 ✅ | -2.4747 | Large |
| Raida vs StackRanker | 0.0000, 5.9605e-08 ✅ | -12.6881, 3.9068e-12 ✅ | -2.5376 | Large |
| WoLoRA vs WoSMOTE | 1.0000, 1.1921e-07 ✅ | -13.0858, 2.0380e-12 ✅ | -2.6172 | Large |
| WoLoRA vs WoSPEAR | 0.0000, 5.9605e-08 ✅ | -19.0825, 5.1848e-16 ✅ | -3.8165 | Large |
| WoLoRA vs StackRanker | 0.0000, 5.9605e-08 ✅ | -21.4166, 3.7691e-17 ✅ | -4.2833 | Large |
| WoSMOTE vs WoSPEAR | 0.0000, 5.9605e-08 ✅ | -13.2965, 1.4527e-12 ✅ | -2.6593 | Large |
| WoSMOTE vs StackRanker | 0.0000, 5.9605e-08 ✅ | -13.4718, 1.0995e-12 ✅ | -2.6944 | Large |
| WoSPEAR vs StackRanker | 0.0000, 5.9605e-08 ✅ | -10.6797, 1.3403e-10 ✅ | -2.1359 | Large |

---

## 🧠 Friedman Test Across Models

| Metric | χ² | p-value | Significant Difference? |
|---------|----|----------|--------------------------|
| F1      | 120.8857 | 2.0376e-24 | ✅ Yes |
| Accuracy | 123.8800 | 4.7271e-25 | ✅ Yes |

---

### ✅ Interpretation Summary

- **Normality**: All models except *Hasan* are normally distributed.
- **Pairwise comparisons**: StackRanker consistently outperforms all baselines across both F1 and Accuracy (p < 0.001, large effect sizes).
- **Friedman test** confirms statistically significant differences among all models.
