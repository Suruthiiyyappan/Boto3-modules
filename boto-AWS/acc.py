# import boto3
# ACCESS_KEY = 'AKIARP337VSRIFPRWSWG'
# SECRET_KEY = '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'
# sts = boto3.client(
#     "sts", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY,
# )
# account_id = boto3.client("sts").get_caller_identity()["Account"]
import boto3

def get_account_id():
    client = boto3.client("sts")
    return client.get_caller_identity()["Account"]


if __name__ == "__main__":
    print(get_account_id())
