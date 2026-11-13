# credit-pd-freddie-mac

12-month probability-of-default (PD) model on the Freddie Mac Single-Family Loan-Level Dataset,
validated the way a bank model-validation team would: discrimination, calibration, stability and
out-of-time performance. Packaged as an API with Docker, MLflow and CI.

> Résumé (FR) : modèle de PD à 12 mois sur données réelles de prêts immobiliers (Freddie Mac),
> comparant scorecard logistique (WoE) et LightGBM, avec validation out-of-time, calibration, PSI,
> SHAP, puis déploiement via FastAPI + Docker + MLflow. Projet en cours (fin prévue le 7 déc. 2026).

## Status
Work in progress. Results will be added here once produced by the code.

## Quick start
```bash
./scripts/setup_mac.sh   # installs uv, creates the env, runs tests
make test
make api                 # FastAPI on http://localhost:8000/health
make up                  # API + MLflow via Docker Compose
```

## Layout
`src/credit_pd` modelling code · `api` FastAPI service · `tests` · `data` (git-ignored) · `docs` validation report.
