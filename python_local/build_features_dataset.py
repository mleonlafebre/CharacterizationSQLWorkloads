import json
import csv
from pathlib import Path

ROOT = Path.home() / "Downloads" / "tpcds_lambda_results"

rows = []

for f in ROOT.rglob("*.json"):

    try:

        with open(f, "r", encoding="utf-8") as infile:
            data = json.load(infile)

        response = data.get("lambda_output", {})

        body = response.get("body", response)

        de = body.get("data_estimation", {})
        stats = de.get("sql_stats", {})
        new_rules = stats.get("new_rules", {})
        estimated = body.get("estimated", {})
        additional = (
            response
            .get("data_estimation", {})
            .get("additional_features", {})
        )

        rows.append({

            "template_id": data.get("template_id"),
            "scale_factor": data.get("scale_factor"),
            "executed_emr": data.get("executed_emr"),

            "query_complexity": de.get("query_complexity"),
            "factor_complexity": de.get("factor_complexity"),

            "total_bytes_raw": de.get("total_bytes_raw"),
            "total_bytes": de.get("total_bytes"),
            "total_bytes_effective": de.get("total_bytes_effective"),

            "subquery_multiplier_adjusted": stats.get("subquery_multiplier_adjusted"),
            "subquery_chain_depth_main": stats.get("subquery_chain_depth_main"),
            "cte_real_subqueries_count": stats.get("cte_real_subqueries_count"),
            
            "repeated_bytes_ratio": new_rules.get("repeated_bytes_ratio"),
            "runtime_estimated": estimated.get("runtime_minutes"),
            "cost_estimated": estimated.get("cost_usd"),
            
            "join_count": additional.get("join_count"),
            "group_by_count": additional.get("group_by_count"),
            "distinct_count": additional.get("distinct_count"),
            "window_count": additional.get("window_count"),
            "subquery_count": additional.get("subquery_count"),
            "table_count": additional.get("table_count"),
            "join_to_table_ratio": additional.get("join_to_table_ratio"),
            "table_size_cv": additional.get("table_size_cv")


        })

    except Exception as e:
        print(f"Error en {f}: {e}")

outfile = ROOT / "tpcds_complexity_dataset.csv"

with open(outfile, "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.DictWriter(
        csvfile,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)

print(f"Filas generadas: {len(rows)}")
print(f"CSV: {outfile}")