# verify_setup.py — chạy để confirm môi trường hoạt động
import boto3
from config import AWS_REGION, S3_BUCKET, ROLE_ARN

def verify():
    print("=" * 50)
    print("Kiểm tra môi trường AWS...")
    print("=" * 50)

    # 1. Kiểm tra credentials
    try:
        sts = boto3.client("sts", region_name=AWS_REGION)
        identity = sts.get_caller_identity()
        print(f"✅ AWS Account: {identity['Account']}")
        print(f"✅ User/Role:   {identity['Arn']}")
    except Exception as e:
        print(f"❌ Credentials lỗi: {e}")
        return

    # 2. Kiểm tra S3 bucket
    try:
        s3 = boto3.client("s3", region_name=AWS_REGION)
        s3.head_bucket(Bucket=S3_BUCKET)
        print(f"✅ S3 Bucket:   s3://{S3_BUCKET} — accessible")
    except Exception as e:
        print(f"❌ S3 Bucket lỗi: {e}")

    # 3. Kiểm tra IAM Role
    try:
        iam = boto3.client("iam", region_name=AWS_REGION)
        role_name = ROLE_ARN.split("/")[-1]
        iam.get_role(RoleName=role_name)
        print(f"✅ IAM Role:    {role_name} — exists")
    except Exception as e:
        print(f"❌ IAM Role lỗi: {e}")

    # 4. Kiểm tra SageMaker API
    try:
        sm = boto3.client("sagemaker", region_name=AWS_REGION)
        sm.list_notebook_instances(MaxResults=1)
        print(f"✅ SageMaker:   API OK — region {AWS_REGION}")
    except Exception as e:
        print(f"❌ SageMaker lỗi: {e}")

    print("=" * 50)
    print("Xong! Nếu tất cả ✅ là sẵn sàng.")

if __name__ == "__main__":
    verify()