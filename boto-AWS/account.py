# import boto3
# sts = boto3.client(
#     "sts", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY,
# )
# account_id = sts.get_caller_identity()["Account"]

import boto3

# ACCESS_KEY = 'AKIA6OY255R3RX3UUPN7'
# SECRET_KEY = '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'
ACCESS_KEY = 'AKIARP337VSRIFPRWSWG'
SECRET_KEY = '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'

iam = boto3.resource('iam',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)
account_id = iam.CurrentUser().arn.split(':')[4]

print (account_id)