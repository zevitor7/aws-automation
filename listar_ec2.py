import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("ID:", instance['InstanceId'])
        print("Estado:", instance['State']['Name'])
        print("Tipo:", instance['InstanceType'])
        print("-" * 30)