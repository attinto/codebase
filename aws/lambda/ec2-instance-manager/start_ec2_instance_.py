import json
import boto3


"With this script you can easily turn on and off an EC2 instance and attach it to a trigger with a schedule using a cron job."

ec2_client = boto3.client('ec2')
INSTANCE_ID = 'INSTANCE-ID-HERE' 

def lambda_handler(event, context):
    try:
        # Start EC2 instance
        response = ec2_client.start_instances(InstanceIds=[INSTANCE_ID])
        print(f"Res: {response}")
        print(f"EC2 instance {INSTANCE_ID} started successfully.")
        
        # Return a success message
        return {
            'statusCode': 200,
            'body': json.dumps(f"EC2 instance {INSTANCE_ID} started successfully.")
        }
        
    except Exception as e:
        print(f"Error starting EC2 instance: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error starting EC2 instance: {str(e)}")
        }