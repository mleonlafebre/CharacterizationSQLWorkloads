# CharacterizationSQLWorkloads
Notebooks for Analytical SQL Workload Characterization

An analytical SQL workload characterization and reproducible workflow for the unified 357-row dataset.

* The 297 unique query-scale observations are used for PCA, grouped model comparison, SHAP, permutation importance, ablation, clustering, and scale stability analyses.

The `notebook` folder contains the final dataset and the required analysis.

The `AWS` folder includes the Lambda function used to generate the query analysis, while the `S3` folder contains the data dictionary and the TPC-DS queries used for this lab.

The `python_local` folder contains scripts to invoke the Lambda function, generate output files, and build the dataset.

* The 72 observed EMR executions are used exclusively for exploratory external runtime validation (this is a separate dataset).
* Repeated EMR executions are excluded from the characterization experiments to avoid overweighting the six query templates.


