import boto3
import sys
import os

def manage_instances(action):
    region = os.environ.get('AWS_REGION', 'us-east-1')
    client = boto3.client('ec2', region_name=region)

    # Use more specific tag filtering to target exactly your instances
    instance_tags = client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    'keycloak-server'  # Change this to your specific instance name tag
                ]
            },
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running' if action == 'stop' else 'stopped',
                ]
            }
        ],
    )

    # Extract instance IDs
    ids = [instance['InstanceId']
        for reservation in instance_tags['Reservations']
        for instance in reservation['Instances']]

    if not ids:
        print(f"No instances found in {action} state to perform action on")
        return

    # Perform the requested action
    if action == 'stop':
        response = client.stop_instances(InstanceIds=ids)
        print(f"Stopped instances: {ids}")
        print(f"Response: {response}")
    elif action == 'start':
        response = client.start_instances(InstanceIds=ids)
        print(f"Started instances: {ids}")
        print(f"Response: {response}")
    else:
        print(f"Invalid action: {action}")

if __name__ == "__main__":
    # Get action from command line argument (stop or start)
    action = sys.argv[1] if len(sys.argv) > 1 else 'stop'
    manage_instances(action)
