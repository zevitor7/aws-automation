import boto3

ec2 = boto3.client('ec2')

instance_id = 'i-088822a024ce99a87'  # coloca uma das suas

ec2.start_instances(InstanceIds=[instance_id])

print("Instância iniciando...")