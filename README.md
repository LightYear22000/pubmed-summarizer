# How to run?

- We use Gemini to generate summaries and reports. So, to run this you need an API Key. "Get API key" on [Google AI Studio](aistudio.google.com/app/apikey).
- Export the created API Key as environment variable

```
export API_KEY="your-api-key"
```

- Create an NCBI API Key as per instructions in [this page](https://ncbiinsights.ncbi.nlm.nih.gov/2017/11/02/new-api-keys-for-the-e-utilities/) and export it using the following command:

```
export NCBI_API_KEY="your-ncbi-api-key"
```

- Trigger the summar and results generation process using the following command:

```
python3 main.py
```

- Check the summary and tables generated in `data/summaries` and `data/tables` directories respectively.

# Controls

- Modify MAX_THREADS in config.py to manipulate the threadpool size used for concurrent processing of URLs

# Limitations

- No backend to trigger or fetch summaries/results.

# Examples

## hTERT Peptide Fragment GV1001 Prevents the Development of Porphyromonas gingivalis-Induced Periodontal Disease and Systemic Disorders in ApoE-Deficient Mice

[Link to paper](https://pubmed.ncbi.nlm.nih.gov/38892314/)

### Summary

This research investigated the preventative effects of GV1001, an anticancer peptide, on _Porphyromonas gingivalis_ (_Pg_)-induced periodontal disease and its associated systemic disorders in ApoE-deficient mice. The study found that GV1001 mitigated periodontal disease, atherosclerosis, and Alzheimer's disease-like conditions. This was achieved by reducing local and systemic inflammation, inhibiting the accumulation of _Pg_ DNA, LPS, and gingipains in affected tissues. GV1001 also suppressed atherosclerosis by inhibiting vascular inflammation, lipid deposition, and endothelial-to-mesenchymal transition. Furthermore, it reduced AD biomarkers in the brain. These findings suggest GV1001's potential as a preventative agent for atherosclerosis and AD-related conditions associated with periodontal disease. In vitro studies confirmed GV1001's ability to inhibit _Pg_ gingipain expression and reduce foam cell formation.

### Results Table in CSV

| Figure | Variable                               | PBS + PBS | PBS + GV1001 | Pg + PBS | Pg + GV1001 |
| ------ | -------------------------------------- | --------- | ------------ | -------- | ----------- |
| 2      | IL-1β                                  | 0.00      | 0.00         | 0.02     | 0.01        |
| 2      | TNF-α                                  | 0.00      | 0.01         | 0.23     | 0.04        |
| 2      | IL-6                                   | 0.01      | 0.01         | 0.20     | 0.05        |
| 3      | Number of Pg colonies                  | 0.00      | 0.00         | 21.0     | 11.0        |
| 3      | Number of LPS Pg aggregates            | 0.00      | 0.00         | 18.0     | 4.0         |
| 3      | Number of Kgp aggregates               | 0.00      | 0.00         | 250.0    | 80.0        |
| 3      | Number of RgpB aggregates              | 0.00      | 0.00         | 150.0    | 20.0        |
| 4      | CEJ-ABC (mm)                           | 0.29      | 0.28         | 0.37     | 0.29        |
| 5      | IL-1β                                  | 0.10      | 0.11         | 0.26     | 0.11        |
| 5      | TNF-α                                  | 0.13      | 0.12         | 0.47     | 0.14        |
| 5      | IL-6                                   | 0.12      | 0.12         | 0.35     | 0.12        |
| 6      | Number of Pg bacteria aggregates       | 0.00      | 0.00         | 14.0     | 5.0         |
| 6      | % of LPS staining area                 | 0.00      | 0.00         | 20.0     | 5.0         |
| 6      | % of Kgp staining area                 | 0.00      | 0.00         | 30.0     | 5.0         |
| 6      | % of RgpB staining area                | 0.00      | 0.00         | 15.0     | 5.0         |
| 7      | IL-1β                                  | 0.01      | 0.01         | 0.03     | 0.01        |
| 7      | TNF-α                                  | 0.01      | 0.01         | 0.04     | 0.01        |
| 7      | IL-6                                   | 0.01      | 0.01         | 0.04     | 0.01        |
| 8      | IL-1β                                  | 2.0       | 2.0          | 62.0     | 2.0         |
| 8      | TNF-α                                  | 5.0       | 5.0          | 52.0     | 5.0         |
| 8      | IL-6                                   | 20.0      | 20.0         | 100.0    | 20.0        |
| 8      | GM-CSF                                 | 5.0       | 5.0          | 40.0     | 5.0         |
| 8      | VEGF                                   | 30.0      | 30.0         | 240.0    | 30.0        |
| 8      | IL-17                                  | 1.0       | 1.0          | 70.0     | 1.0         |
| 8      | KC                                     | 15.0      | 15.0         | 130.0    | 15.0        |
| 11     | Fluorescent intensity of CD31          | 17.0      | 16.0         | 20.0     | 16.0        |
| 11     | Fluorescent intensity of FSP-1         | 1.0       | 1.0          | 20.0     | 1.0         |
| 12     | % of Dil-oxLDL stained area per field  | 7.0       | 7.0          | 20.0     | 7.0         |
| 13     | % of CD47 staining intensity per field | 1.0       | 1.0          | 18.0     | 1.0         |
| 15     | Number of Aβ42 aggregates              | 0.0       | 0.0          | 85.0     | 0.0         |
| 15     | Number of p-Tau aggregates             | 0.0       | 0.0          | 20.0     | 0.0         |
| 16     | RgpA                                   | 0.00007   | 0.00007      | 0.0003   | 0.00007     |
| 16     | RgpB                                   | 0.0006    | 0.0006       | 0.003    | 0.0006      |
| 16     | Kgp                                    | 0.0003    | 0.0003       | 0.001    | 0.0003      |

## Enhancing hepatocellular carcinoma management: prognostic value of integrated CCL17, CCR4, CD73, and HHLA2 expression analysis

[Link to paper](https://pubmed.ncbi.nlm.nih.gov/38914802/)

### Summary

This research investigated the prognostic value of CCL17, CCR4, CD73, and HHLA2 expression in hepatocellular carcinoma (HCC). Analyzing 873 HCC patients post-radical surgery, the study found increased CCL17 and CCR4 expression correlated with poor survival. A novel stromal cell population, CCR4+CD73+, was identified and linked to adverse outcomes. A prognostic nomogram incorporating these immunological markers and clinical variables was developed to improve HCC management. The study suggests that reduced CCR4 and CCR4+CD73+ cell prevalence may predict improved outcomes after transcatheter arterial chemoembolization (TACE), highlighting the potential of targeting these markers for enhanced HCC therapy. The findings provide a nuanced understanding of the HCC immunological milieu and improve patient stratification.

### Results Table in CSV

| Characters      | Training cohort (n=354) | Validation cohort (n=519) | p-value |
| --------------- | ----------------------- | ------------------------- | ------- | ------ |
| Gender          | male/female             | 301/53                    | 433/86  | 0.526  |
| Age             | <60/≥60                 | 239/115                   | 284/235 | <0.001 |
| Asite           | no/yes                  | 335/19                    | 488/31  | 0.705  |
| Cirrhosis       | no/yes                  | 243/111                   | 285/234 | <0.001 |
| Tumor number    | single/multiple         | 292/62                    | 453/66  | 0.049  |
| Tumor size      | <5/≥5 cm                | 210/144                   | 296/223 | 0.862  |
| Tumor capsule   | no/yes                  | 105/249                   | 333/186 | <0.001 |
| Bleeding        | no/yes                  | 322/32                    | 475/44  | 0.773  |
| Differentiation | I-II/III-IV             | 222/132                   | 341/178 | 0.364  |
| MVI             | no/yes                  | 205/149                   | 381/138 | <0.001 |
| HBsAg           | negative/positive       | 45/309                    | 75/444  | 0.464  |
| AFP             | <400/≥400 ng/mL         | 162/192                   | 365/154 | <0.001 |
| TB              | <45/≥45 U/L             | 307/47                    | 474/45  | 0.030  |
| GGT             | <45/≥45 U/L             | 143/211                   | 215/304 | 0.761  |
| ALT             | <50/≥50 U/L             | 285/69                    | 417/102 | 0.953  |
| ALB             | <35/≥35 g/L             | 27/327                    | 177/342 | <0.001 |
| CD4             | <80/≥80                 | 307/47                    | 440/79  | 0.422  |
| CD34            | Low/high                | 174/180                   | 240/279 | 0.398  |
| CD68            | <100/≥100               | 225/129                   | 324/195 | 0.734  |
| CD66b           | <22/≥22                 | 224/130                   | 297/222 | 0.074  |
| Treg/CD8        | <1/≥1                   | 230/124                   | 208/311 | <0.001 |
| Treg            | <19/≥19                 | 214/140                   | 205/314 | <0.001 |
| CD8             | <50/≥50                 | 178/176                   | 180/339 | <0.001 |
| CCR4-T          | Low/High                | 175/179                   | 231/288 | 0.152  |
| CCR4-I          | <25/≥25                 | 192/162                   | 273/246 | 0.634  |
| CCL17-T         | Low/High                | 185/169                   | 257/262 | 0.426  |
| CCL17-I         | <30/≥30                 | 141/213                   | 209/310 | 0.897  |
| HHLA-2-T        | Low/High                | 199/155                   | 269/250 | 0.202  |
| CD73-T          | Low/High                | 146/208                   | 192/327 | 0.206  |
| CCR4+CD73+      | <13/≥13                 | 170/184                   | 270/249 | 0.246  |
| CD47            | Low/High                | 226/128                   | 341/178 | 0.571  |
| PDL1            | Low/High                | 211/143                   | 310/209 | 0.970  |
