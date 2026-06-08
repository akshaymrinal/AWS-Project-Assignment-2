import json
import boto3
from datetime import datetime

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

BUCKET_NAME = "ec2-state-backups-demo"

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    state = event['detail']['state']

    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance_data = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_data.append({
                "InstanceId": instance['InstanceId'],
                "InstanceType": instance['InstanceType'],
                "PrivateIp": instance.get('PrivateIpAddress'),
                "State": state,
                "LaunchTime": str(instance['LaunchTime']),
                "Tags": instance.get('Tags', [])
            })

    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    key = f"ec2-backups/{instance_id}/{timestamp}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(instance_data, indent=4)
    )

    return {"statusCode": 200, "body": "Backup completed"}
