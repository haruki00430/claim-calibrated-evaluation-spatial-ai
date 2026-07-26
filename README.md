# Claim-Calibrated Evaluation of Spatial AI in Health Care Forecasting

> **English** | [日本語](#日本語)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21482470.svg)](https://doi.org/10.5281/zenodo.21482470)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.14](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue.svg)](https://doi.org/10.17605/OSF.IO/ANVGC)

---

## English

### Paper

> **Model Rankings Are Not Self-Interpreting: A Claim-Calibrated Evaluation of Spatial AI in Health Care Forecasting**  
> Haruki Saito, MD candidate¹; Tetsuya Ohira, MD, PhD¹²  
> ¹ Department of Epidemiology, Fukushima Medical University School of Medicine, Fukushima, Japan  
> ² Radiation Medical Science Center for the Fukushima Health Management Survey, Fukushima Medical University, Fukushima, Japan  
> *Submitted for publication, 2026*

### Overview

AI research frequently reports that "model A outperformed model B", but such rankings often carry unstated assumptions about which model was chosen as a comparator and what specific claim the ranking is meant to support.

This paper introduces the **Claim-Calibrated Evaluation Procedure (CCEP)** — a framework that:

1. Records a model ranking (e.g., ST-GNN vs. XGBoost)
2. Enumerates *candidate substantive claims* and *alternative explanations* for the ranking
3. Identifies what evidence would distinguish between them
4. Matches available evidence against each claim
5. Reports the **narrowest defensible claim** supported by the evidence

The procedure is applied to a synthesis of two independent studies comparing spatiotemporal graph neural networks (ST-GNN) against baseline models across 51 international environments and 2,517 US counties.

### Key Findings

| Finding | Result |
|---------|--------|
| ST-GNN vs. XGBoost (E1, n=51) | Positive in **34/51** environments; median = **+0.096** |
| ST-GNN vs. Linear+FE (E2, n=51) | Positive in **2/51** environments; median = **−0.641** |
| ICI-E1 correlation (primary, n=49) | r = **0.374**, p = **0.008** |
| ICI-E1 correlation (full panel, n=51) | r = **0.267**, p = **0.058** |
| Study 2 preregistered H1 (n=2,517 counties) | β_std = **−0.0105**, p = **0.427** (null result) |

**Main conclusion**: Comparator choice changed the apparent spatial-AI advantage from 67% to 4% of environments. The observed advantage is conditional on the model, target, comparator, evaluation design, and health care system — not an unconditional property of spatial AI.

### Repository Contents

| File | Description |
|------|-------------|
| [`Supplementary_Data_1.csv`](Supplementary_Data_1.csv) | 51-environment Study 1 comparator audit: ICI, R² for ST-GNN/XGBoost/Linear+FE, E1/E2/E4 values, sample flags |
| [`Supplementary_Code_1.py`](Supplementary_Code_1.py) | Reproduces all E1/E2/E4 arithmetic and ICI-E1 Pearson correlations — standard library only, no dependencies; developed and tested with Python 3.14 |
| [`Figure_1.png`](Figure_1.png) | Conceptual flow diagram of the Claim-Calibrated Evaluation Procedure |
| [`REPRODUCE.md`](REPRODUCE.md) | Step-by-step reproduction instructions |
| [`CITATION.cff`](CITATION.cff) | Machine-readable citation file |

### Data Description (`Supplementary_Data_1.csv`)

The CSV contains 51 rows (one per evaluation environment) and 18 columns:

| Column | Description |
|--------|-------------|
| `environment` | Name of the evaluation environment (country/region) |
| `n_spatial_units` | Number of spatial units (prefectures, regions, counties, etc.) |
| `ici` | Information Continuity Index (0–1) |
| `linear_fe_r2` | Linear fixed-effects model out-of-sample R² |
| `xgboost_r2` | XGBoost out-of-sample R² |
| `stgnn_r2` | ST-GNN out-of-sample R² |
| `e1_stgnn_minus_xgboost` | E1 = ST-GNN R² − XGBoost R² |
| `e2_stgnn_minus_linear_fe` | E2 = ST-GNN R² − Linear+FE R² |
| `e4_stgnn_minus_best_reported` | E4 = ST-GNN R² − max(XGBoost R², Linear+FE R²) |
| `e1_positive` / `e2_positive` / `e4_positive` | Boolean flags indicating positive advantage |
| `primary_ici_sample` | TRUE = included in the primary ICI-E1 correlation (n=49; UK(England) and Pennsylvania excluded) |
| `source_notes` | Interpretive notes for each environment |
| `fold_outputs_status` | Availability of fold-level predictions (MISSING for all) |
| `formal_uncertainty_status` | Availability of formal uncertainty quantification |

### How to Reproduce

```bash
git clone https://github.com/haruki00430/claim-calibrated-evaluation-spatial-ai.git
cd claim-calibrated-evaluation-spatial-ai
python Supplementary_Code_1.py
```

See [REPRODUCE.md](REPRODUCE.md) for expected output and scope notes.

### Related Repositories

| Repository | Role in this paper |
|-----------|-------------------|
| [beyond-information-continuity-us](https://github.com/haruki00430/beyond-information-continuity-us) | Study 2 — preregistered county-level analysis (2,517 US counties) |
| [institutional-channel-simulation-study](https://github.com/haruki00430/institutional-channel-simulation-study) | Companion paper (Study 0) |
| [spatial-signal-learnability-simulation-study](https://github.com/haruki00430/spatial-signal-learnability-simulation-study) | Companion paper (Paper 4) |

### Preregistration

Study 2 primary analysis was preregistered at OSF before data analysis:  
**https://osf.io/anvgc/** (doi: [10.17605/OSF.IO/ANVGC](https://doi.org/10.17605/OSF.IO/ANVGC))

### Citation

Please cite this repository using the information in [CITATION.cff](CITATION.cff) or use the Zenodo DOI:  
**https://doi.org/10.5281/zenodo.21482470**

To cite the manuscript:
> Saito H, Ohira T. Model Rankings Are Not Self-Interpreting: A Claim-Calibrated Evaluation of Spatial AI in Health Care Forecasting. *Submitted for publication*, 2026.

### License

Code: [MIT License](LICENSE)  
Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 日本語

> [English](#english) | **日本語**

### 論文情報

> **モデルの順位表は自己説明しない：医療予測における空間AIの主張較正評価**  
> 齋藤治輝（医学生）¹、大平哲也（MD, PhD）¹²  
> ¹ 福島県立医科大学医学部疫学講座、福島、日本  
> ² 福島県立医科大学 放射線医学県民健康管理センター、福島、日本  
> *投稿中、2026年*

### 概要

AI研究では「モデルAがモデルBより優れていた」という結果が頻繁に報告されます。しかし、このような順位表にはしばしば暗黙の前提が含まれており、**比較相手の選び方**や**その結果でどこまでの主張が支持されるのか**が明示されないまま広い主張に使われることがあります。

本論文では **主張較正評価手続き（Claim-Calibrated Evaluation Procedure: CCEP）** を提案します。この手続きは：

1. モデルの比較結果（例：ST-GNN vs. XGBoost）を記録する
2. その結果から支持できる候補主張と代替説明を列挙する
3. 主張を区別するために必要な証拠を特定する
4. 実際に得られた証拠と照合する
5. 証拠で支持できる**最も狭い（控えめな）主張**を結論とする

この手続きを、51地域（日本・英国・韓国・米国）と米国2,517郡の2つの独立研究のデータに適用しました。

### 主要結果

| 結果 | 値 |
|------|-----|
| ST-GNN vs. XGBoost（E1、n=51環境） | **34/51環境**で正；中央値 = **+0.096** |
| ST-GNN vs. Linear+FE（E2、n=51環境） | **2/51環境**で正；中央値 = **−0.641** |
| ICI-E1相関（主解析、n=49） | r = **0.374**、p = **0.008** |
| ICI-E1相関（全体、n=51） | r = **0.267**、p = **0.058** |
| Study 2 事前登録H1（n=2,517郡） | β_std = **−0.0105**、p = **0.427**（帰無結果） |

**主な結論**：比較相手を変えるだけで、空間AIの「見かけの優位性」が環境の67%から4%へと劇的に変化しました。この優位性は空間AIが本質的に優れているという証拠ではなく、モデル・予測対象・比較相手・評価設計・医療システムという条件に依存した、**条件付きの性能差**です。

### リポジトリ構成

| ファイル | 内容 |
|---------|------|
| [`Supplementary_Data_1.csv`](Supplementary_Data_1.csv) | 51環境の Study 1 比較監査データ（ICI・各モデルR²・E1/E2/E4値） |
| [`Supplementary_Code_1.py`](Supplementary_Code_1.py) | E1/E2/E4算術とICI-E1相関を再現するPythonスクリプト（外部ライブラリ不要） |
| [`Figure_1.png`](Figure_1.png) | 主張較正評価手続きの概念図 |
| [`REPRODUCE.md`](REPRODUCE.md) | 再現手順（日英） |
| [`CITATION.cff`](CITATION.cff) | 機械可読引用ファイル |

### 再現方法

```bash
git clone https://github.com/haruki00430/claim-calibrated-evaluation-spatial-ai.git
cd claim-calibrated-evaluation-spatial-ai
python Supplementary_Code_1.py
```

詳細は [REPRODUCE.md](REPRODUCE.md) を参照してください。

### 姉妹リポジトリ

| リポジトリ | 本論文における役割 |
|-----------|------------------|
| [beyond-information-continuity-us](https://github.com/haruki00430/beyond-information-continuity-us) | Study 2 — 事前登録済み郡レベル解析（米国2,517郡） |
| [institutional-channel-simulation-study](https://github.com/haruki00430/institutional-channel-simulation-study) | コンパニオン論文（Study 0） |
| [spatial-signal-learnability-simulation-study](https://github.com/haruki00430/spatial-signal-learnability-simulation-study) | コンパニオン論文（Paper 4） |

### 事前登録

Study 2 の主解析は解析開始前にOSFで事前登録されています：  
**https://osf.io/anvgc/**（doi: [10.17605/OSF.IO/ANVGC](https://doi.org/10.17605/OSF.IO/ANVGC)）

### 引用

本リポジトリの引用には [CITATION.cff](CITATION.cff) を参照するか、Zenodo DOIをお使いください：  
**https://doi.org/10.5281/zenodo.21482470**

論文の引用：
> Saito H, Ohira T. Model Rankings Are Not Self-Interpreting: A Claim-Calibrated Evaluation of Spatial AI in Health Care Forecasting. *投稿中*. 2026.

### ライセンス

コード：[MIT License](LICENSE)  
データ：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
