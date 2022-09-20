import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

filters = [{'Name':'tag:Name', 'Values':['*']}]
vpcs = list(ec2.vpcs.filter(Filters=filters))

print(f'These are the VPCs in the ec2:')
for vpc in vpcs:
    print(vpc)

for vpc in vpcs:
    tag = vpc.create_tags(Tags=[{'Key':'Project', "Value":'Talent-Academy'}])
    response = client.describe_tags(Filters=[{'Name': 'resource-type', 'Values':['vpc']}])
    print(*response['Tags'],sep='\n')