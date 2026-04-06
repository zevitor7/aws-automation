import boto3
import os

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

ec2 = boto3.client('ec2')
