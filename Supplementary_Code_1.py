"""Reproduce the Study 1 comparator audit and ICI correlations.

Usage:
    python Supplementary_Code_1.py Supplementary_Data_1.csv

Developed and tested with Python 3.14; requires Python 3.8+ (standard library only). The script does not
reconstruct unavailable fold-level uncertainty or retrain any forecasting model.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path

TOLERANCE = 1e-12


def as_bool(value: str) -> bool:
    return value.strip().lower() in {"true", "1", "yes"}


def load_rows(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for raw in csv.DictReader(handle):
            rows.append(
                {
                    "environment": raw["environment"],
                    "ici": float(raw["ici"]),
                    "linear": float(raw["linear_fe_r2"]),
                    "xgboost": float(raw["xgboost_r2"]),
                    "stgnn": float(raw["stgnn_r2"]),
                    "e1": float(raw["e1_stgnn_minus_xgboost"]),
                    "e2": float(raw["e2_stgnn_minus_linear_fe"]),
                    "e4": float(raw["e4_stgnn_minus_best_reported"]),
                    "primary_ici_sample": as_bool(raw["primary_ici_sample"]),
                }
            )
    return rows


def validate_arithmetic(rows: list[dict[str, object]]) -> None:
    for row in rows:
        expected = {
            "e1": float(row["stgnn"]) - float(row["xgboost"]),
            "e2": float(row["stgnn"]) - float(row["linear"]),
            "e4": float(row["stgnn"]) - max(float(row["xgboost"]), float(row["linear"])),
        }
        for key, value in expected.items():
            if not math.isclose(float(row[key]), value, rel_tol=0.0, abs_tol=TOLERANCE):
                raise ValueError(
                    f"Arithmetic mismatch for {row['environment']} {key}: "
                    f"stored={row[key]!r}, recomputed={value!r}"
                )


def beta_continued_fraction(a: float, b: float, x: float) -> float:
    """Continued fraction used by the regularized incomplete beta function."""
    max_iterations = 200
    epsilon = 3.0e-14
    tiny = 1.0e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d
    for m in range(1, max_iterations + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < epsilon:
            return h
    raise ArithmeticError("Incomplete beta continued fraction did not converge")


def regularized_incomplete_beta(a: float, b: float, x: float) -> float:
    if not 0.0 <= x <= 1.0:
        raise ValueError("x must be between 0 and 1")
    if x in (0.0, 1.0):
        return x
    log_factor = (
        math.lgamma(a + b)
        - math.lgamma(a)
        - math.lgamma(b)
        + a * math.log(x)
        + b * math.log1p(-x)
    )
    factor = math.exp(log_factor)
    if x < (a + 1.0) / (a + b + 2.0):
        return factor * beta_continued_fraction(a, b, x) / a
    return 1.0 - factor * beta_continued_fraction(b, a, 1.0 - x) / b


def correlation(rows: list[dict[str, object]]) -> dict[str, float | int]:
    x = [float(row["ici"]) for row in rows]
    y = [float(row["e1"]) for row in rows]
    n = len(rows)
    x_mean = statistics.fmean(x)
    y_mean = statistics.fmean(y)
    cross = sum((a - x_mean) * (b - y_mean) for a, b in zip(x, y))
    x_ss = sum((a - x_mean) ** 2 for a in x)
    y_ss = sum((b - y_mean) ** 2 for b in y)
    r = cross / math.sqrt(x_ss * y_ss)
    df = n - 2
    t_squared = (r * r) * df / (1.0 - r * r)
    p_value = regularized_incomplete_beta(df / 2.0, 0.5, df / (df + t_squared))
    return {"n": n, "pearson_r": r, "p_value": p_value}


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    primary = [row for row in rows if bool(row["primary_ici_sample"])]
    return {
        "n_environments": len(rows),
        "positive_counts": {
            key.upper(): sum(float(row[key]) > 0 for row in rows)
            for key in ("e1", "e2", "e4")
        },
        "medians": {
            key.upper(): statistics.median(float(row[key]) for row in rows)
            for key in ("e1", "e2", "e4")
        },
        "ici_e1_correlations": {
            "primary": correlation(primary),
            "full": correlation(rows),
        },
        "scope_note": (
            "Aggregate displayed values only; no fold-level confidence intervals, "
            "superiority tests, or model retraining were reconstructed."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "csv_path",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("Supplementary_Data_1.csv"),
    )
    args = parser.parse_args()
    rows = load_rows(args.csv_path)
    validate_arithmetic(rows)
    print(json.dumps(summarize(rows), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
