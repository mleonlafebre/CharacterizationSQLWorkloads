# CharacterizationSQLWorkloads
Notebook of CharacterizationSQLWorkloads

ICDE 2027: Analytical SQL Workload Characterization
Reproducible workflow for the unified 357-row dataset.
* The 297 unique query-scale observations are used for PCA, grouped model comparison, SHAP, permutation importance, ablation, clustering, and scale stability.
* The 72 observed EMR executions are used only for exploratory external runtime validation.
* Repeated EMR executions are excluded from the characterization experiments to avoid overweighting six query templates.
