import boto3

ec2 = boto3.resource('ec2')

user_data_script = """#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
echo "<h1>Servidor criado com Python 🚀</h1>" > /var/www/html/index.html
"""

instance = ec2.create_instances(
    ImageId='ami-0c3389a4fa5bddaad',
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
    KeyName='josekey-new',  # sua chave
    UserData=user_data_script
)

print("Criando servidor...")
print("ID:", instance[0].id)