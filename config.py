# config.py — dùng chung cho toàn bộ project
import os
from dotenv import load_dotenv

load_dotenv()

# ── AWS Core ──────────────────────────────────────────
AWS_REGION = os.getenv("AWS_REGION", "ap-southeast-1")
S3_BUCKET  = os.getenv("S3_BUCKET")
ROLE_ARN   = os.getenv("ROLE_ARN")

# ── S3 Paths ──────────────────────────────────────────
S3_PREFIX           = "ml-forecasting"
S3_RAW_DATA         = f"s3://{S3_BUCKET}/{S3_PREFIX}/data/raw/"
S3_PROCESSED_DATA   = f"s3://{S3_BUCKET}/{S3_PREFIX}/data/processed/"
S3_TRAIN_DATA       = f"s3://{S3_BUCKET}/{S3_PREFIX}/data/train/"
S3_VAL_DATA         = f"s3://{S3_BUCKET}/{S3_PREFIX}/data/validation/"
S3_TEST_DATA        = f"s3://{S3_BUCKET}/{S3_PREFIX}/data/test/"
S3_MODEL_ARTIFACTS  = f"s3://{S3_BUCKET}/{S3_PREFIX}/models/artifacts/"
S3_EVALUATION       = f"s3://{S3_BUCKET}/{S3_PREFIX}/outputs/evaluation/"
S3_MONITORING       = f"s3://{S3_BUCKET}/{S3_PREFIX}/monitoring/"

# ── SageMaker ─────────────────────────────────────────
EXPERIMENT_NAME = "sales-forecasting-experiment"
PIPELINE_NAME   = "sales-forecasting-pipeline"

# ── Model ─────────────────────────────────────────────
TARGET_COLUMN  = "Sales"
DATE_COLUMN    = "Date"
STORE_COLUMN   = "Store"

TRAIN_END_DATE = "2015-06-30"
VAL_END_DATE   = "2015-09-30"