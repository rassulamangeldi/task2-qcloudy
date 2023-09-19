{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import json\
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
