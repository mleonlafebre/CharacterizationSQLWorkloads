import json
import time
import requests
from pathlib import Path

URL = "https://5rvprvewwkcrks2epstqhi5pli0bskdx.lambda-url.us-east-1.on.aws/"

OUTPUT_ROOT = Path.home() / "Downloads" / "tpcds_lambda_results"

OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

#EMR_EXECUTED = {
#    14, 23, 47, 64, 67, 80
#}
EMR_EXECUTED = {}

#for scale_factor in [1, 3]:
for scale_factor in [10]:

    sf_dir = OUTPUT_ROOT / f"{scale_factor}tb"
    sf_dir.mkdir(parents=True, exist_ok=True)

    for template_id in range(1, 100):

        payload = {
            "action": "recommend",
            "query_bucket": "bigdatamell",
            "metrics_bucket": "algoritmomell",
            "metrics_key": "info_result/metrics/",
            "scale_factor_tb": scale_factor,
            "query_key": f"queries/{template_id}.sql"
        }

        print(
            f"Template {template_id} "
            f"SF={scale_factor}"
        )

        try:

            response = requests.post(
                URL,
                json=payload,
                headers={
                    "Content-Type": "application/json"
                },
                timeout=300
            )

            result = response.json()

            output = {
                "template_id": template_id,
                "scale_factor": scale_factor,
                "executed_emr": template_id in EMR_EXECUTED,
                "runtime_real_seconds": None,
                "cost_real_usd": None,
                "lambda_output": result
            }

            outfile = (
                sf_dir /
                f"{template_id}.json"
            )

            with open(
                outfile,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    output,
                    f,
                    indent=2
                )

            print(
                f"OK {template_id}"
            )

        except Exception as e:

            print(
                f"ERROR {template_id}: {e}"
            )

        time.sleep(0.2)

print("Finalizado")