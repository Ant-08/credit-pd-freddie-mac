import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# Data can live outside the project (e.g. outside a cloud-synced folder):
# export CREDIT_PD_DATA_DIR=~/data/credit-pd
DATA_DIR = Path(os.environ.get("CREDIT_PD_DATA_DIR", ROOT / "data")).expanduser()
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# Default definition: 90+ days past due (current_loan_delinquency_status >= 3)
# observed within 12 months after the observation date.
DEFAULT_DPD_THRESHOLD = 3
HORIZON_MONTHS = 12

# Out-of-time split by observation year (to be confirmed once data is loaded)
TRAIN_YEARS = range(2012, 2018)
VALID_YEARS = [2018]
TEST_YEARS = [2019]
STRESS_YEARS = [2020]
