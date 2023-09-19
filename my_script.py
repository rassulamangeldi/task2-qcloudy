import json\
import requests\
\
def get_instance_info():\
    # Get the instance ID from the EC2 metadata service\
    response = requests.get("http://169.254.169.254/latest/meta-data/instance-id")\
    instance_id = response.text\
\
    # Get the public IP address from the EC2 metadata service\
    response = requests.get("http://169.254.169.254/latest/meta-data/public-ipv4")\
    public_ip = response.text\
\
    # Create a dictionary with the instance information\
    instance_info = \{\
        "instance_id": instance_id,\
        "public_ip": public_ip\
    \}\
\
    return instance_info\
\
if __name__ == "__main__":\
    instance_info = get_instance_info()\
\
    # Convert the instance info dictionary to JSON format\
    instance_info_json = json.dumps(instance_info, indent=4)\
\
    # Print the JSON response\
    print(instance_info_json)\
}
