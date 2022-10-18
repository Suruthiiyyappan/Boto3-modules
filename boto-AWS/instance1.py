import sys
import boto3
session=boto3.session(profile_name="aws_ec2_iam_user",region_name="us-east-1")
instances=session.resource(service_name="ec2")

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)
