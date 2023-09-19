import boto3

def get_instance_info():
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Specify the filters to find the running EC2 instance with your key-value pair
    filters = [
        {'Name': 'tag:Name', 'Values': ['ASG-Task-Instance']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]

    # Use the filters to describe instances
    instances = ec2.describe_instances(Filters=filters)

    # Check if instances were found
    if instances['Reservations']:
        # Get the first instance (assuming only one instance matches the filter)
        instance = instances['Reservations'][0]['Instances'][0]

        # Extract instance ID and public IP address
        instance_id = instance['InstanceId']
        public_ip = instance.get('PublicIpAddress', 'N/A')  # If public IP not available, set to 'N/A'

        # Create a dictionary to hold the instance information
        instance_info = {
            'InstanceId': instance_id,
            'PublicIpAddress': public_ip
        }

        return instance_info
    else:
        return {'message': 'No running instances matching the filter were found.'}

if __name__ == '__main__':
    instance_info = get_instance_info()
    print(instance_info)
