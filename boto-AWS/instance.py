import boto3
session=boto3.session(profile_name="aws_ec2_iam_user",region_name="us-east-1")
ec2_re=session.resource(service_name="ec2")
# ec2_cli=session.client(service_name="ec2")
#
for each_instance in ec2_re.instances.all():
    print(each_instance.id, each_instance.state['name'])