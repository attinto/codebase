import json
import boto3

ec2_client = boto3.client('ec2')
INSTANCE_ID = 'INSTANCE-ID-HERE' 

def lambda_handler(event, context):
    try:
        # Stop EC2 instance
        response = ec2_client.stop_instances(InstanceIds=[INSTANCE_ID])
        print(f"Res: {response}")
        print(f"EC2 instance {INSTANCE_ID} stopped successfully.")
        
        # Return a success message
        return {
            'statusCode': 200,
            'body': json.dumps(f"EC2 instance {INSTANCE_ID} stopped successfully.")
        }
        
    except Exception as e:
        print(f"Error stopping EC2 instance: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error stopping EC2 instance: {str(e)}")
        }