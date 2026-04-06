import boto3

ec2 = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

def listar():
    response = ec2.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['InstanceId'], "-", i['State']['Name'])

def ligar():
    id = input("ID da instância: ")
    ec2.start_instances(InstanceIds=[id])
    print("Ligando...")

def parar():
    id = input("ID da instância: ")
    ec2.stop_instances(InstanceIds=[id])
    print("Parando...")

def criar():
    instance = ec2_resource.create_instances(
        ImageId='ami-0c3389a4fa5bddaad',
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro'
    )
    print("Criado:", instance[0].id)

while True:
    print("\n1-Listar 2-Criar 3-Ligar 4-Parar 5-Sair")
    op = input("Escolha: ")

    if op == "1":
        listar()
    elif op == "2":
        criar()
    elif op == "3":
        ligar()
    elif op == "4":
        parar()
    elif op == "5":
=======
import boto3

ec2 = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

def listar():
    response = ec2.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            print(i['InstanceId'], "-", i['State']['Name'])

def ligar():
    id = input("ID da instância: ")
    ec2.start_instances(InstanceIds=[id])
    print("Ligando...")

def parar():
    id = input("ID da instância: ")
    ec2.stop_instances(InstanceIds=[id])
    print("Parando...")

def criar():
    instance = ec2_resource.create_instances(
        ImageId='ami-0c3389a4fa5bddaad',
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro'
    )
    print("Criado:", instance[0].id)

while True:
    print("\n1-Listar 2-Criar 3-Ligar 4-Parar 5-Sair")
    op = input("Escolha: ")

    if op == "1":
        listar()
    elif op == "2":
        criar()
    elif op == "3":
        ligar()
    elif op == "4":
        parar()
    elif op == "5":
>>>>>>> 709116668bb8ac620532311794e09c25a8cd5ab6
        break