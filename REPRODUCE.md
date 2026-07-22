# Reproduction Instructions / 再現手順

## English

### Requirements

- **Python 3.10 or later** (no third-party packages required — standard library only)
- The two files must be in the same directory:
  - `Supplementary_Code_1.py`
  - `Supplementary_Data_1.csv`

### Steps

```bash
# Clone this repository
git clone https://github.com/haruki00430/claim-calibrated-evaluation-spatial-ai.git
cd claim-calibrated-evaluation-spatial-ai

# Run the reproduction script
python Supplementary_Code_1.py
```

The script will:
1. Load `Supplementary_Data_1.csv`
2. Validate E1, E2, and E4 arithmetic for all 51 environments (tolerance: 1 × 10⁻¹²)
3. Compute and print ICI-E1 Pearson correlations using a pure-Python implementation of the regularized incomplete beta function
4. Output a JSON summary to stdout

### Expected Output

```json
{
  "n_environments": 51,
  "positive_counts": {
    "E1": 34,
    "E2": 2,
    "E4": 2
  },
  "medians": {
    "E1": 0.096,
    "E2": -0.641,
    "E4": -0.641
  },
  "ici_e1_correlations": {
    "primary": {
      "n": 49,
      "pearson_r": 0.373616...,
      "p_value": 0.008186...
    },
    "full": {
      "n": 51,
      "pearson_r": 0.267159...,
      "p_value": 0.058066...
    }
  },
  "scope_note": "Aggregate displayed values only; ..."
}
```

Values match those reported in the manuscript to within floating-point precision.

### What This Script Does NOT Reproduce

This script reproduces only the arithmetic summaries derived from the pre-computed `R²` values stored in the CSV. It does **not**:

- Retrain any forecasting model (ST-GNN, XGBoost, or Linear+FE)
- Reconstruct fold-level predictions or confidence intervals
- Re-run the Study 2 primary analysis

For Study 2 analytic data and code, see the companion repository:  
[https://github.com/haruki00430/beyond-information-continuity-us](https://github.com/haruki00430/beyond-information-continuity-us)  
(Zenodo: [https://doi.org/10.5281/zenodo.21212774](https://doi.org/10.5281/zenodo.21212774))

---

## 日本語

### 必要環境

- **Python 3.10 以降**（外部パッケージ不要・標準ライブラリのみ使用）
- 同じディレクトリに以下の2ファイルが必要：
  - `Supplementary_Code_1.py`
  - `Supplementary_Data_1.csv`

### 手順

```bash
# リポジトリをクローン
git clone https://github.com/haruki00430/claim-calibrated-evaluation-spatial-ai.git
cd claim-calibrated-evaluation-spatial-ai

# 再現スクリプトを実行
python Supplementary_Code_1.py
```

スクリプトは以下を実行します：
1. `Supplementary_Data_1.csv` を読み込む
2. 51 環境すべての E1・E2・E4 の算術を検証（許容誤差：1 × 10⁻¹²）
3. 正則化不完全ベータ関数の純 Python 実装を使って ICI-E1 ピアソン相関を算出
4. JSON サマリーを標準出力に出力

### 期待される出力

```json
{
  "n_environments": 51,
  "positive_counts": {
    "E1": 34,
    "E2": 2,
    "E4": 2
  },
  "medians": {
    "E1": 0.096,
    "E2": -0.641,
    "E4": -0.641
  },
  "ici_e1_correlations": {
    "primary": {
      "n": 49,
      "pearson_r": 0.373616...,
      "p_value": 0.008186...
    },
    "full": {
      "n": 51,
      "pearson_r": 0.267159...,
      "p_value": 0.058066...
    }
  }
}
```

論文に報告されている値と浮動小数点精度の範囲内で一致します。

### このスクリプトが再現しないもの

本スクリプトは CSV に格納済みの R² 値から導出される算術サマリーのみを再現します。以下は**再現しません**：

- 予測モデル（ST-GNN・XGBoost・Linear+FE）の再学習
- フォールドレベルの予測値や信頼区間の復元
- Study 2 の主解析の再実行

Study 2 の解析データ・コードは姉妹リポジトリを参照してください：  
[https://github.com/haruki00430/beyond-information-continuity-us](https://github.com/haruki00430/beyond-information-continuity-us)  
（Zenodo: [https://doi.org/10.5281/zenodo.21212774](https://doi.org/10.5281/zenodo.21212774)）
