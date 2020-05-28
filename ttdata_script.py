import sys
import requests

def register(did):
    url = "http://ttdata.life:7061/register"
    payload = {"device_id": did,
                "category": "saic"
              }
    response = requests.post(url=url, data = payload)
    print(response.text.encode('utf8'))
    print("^^register response^^")

def upload_data(creationDatetime, lastUpdatedDatetime, deployer, imageName, digest, tag):
    url = "http://ttdata.life:7061/uploaddata"
    device_data = [{
    'creation_datetime': creationDatetime,
    'last_updated_datetime': lastUpdatedDatetime,
    'name': imageName,
    'tag': tag,
    'deployer': deployer,
    'digest': digest,
    'key': "last_updated_datetime|name|deployer|digest"
    }]

    payload = {
    "data_type": 2,
    "device_id": imageName,
    "key": "last_updated_datetime|name|deployer|digest",
    "device_data": device_data
    }

    r = requests.post(url = url, json = payload)
    print(r.text.encode('utf8'))


if __name__ == "__main__":
    deployer = sys.argv[1]
    imageName = sys.argv[2]
    digest = sys.argv[3]
    lastUpdatedTime = sys.argv[5]
    creationTime = sys.argv[8]
    tag = sys.argv[9]

    print(lastUpdatedTime)
    print(digest)
    print(creationTime)
    print(tag)
    
    register(imageName)
    upload_data(creationTime, lastUpdatedTime, deployer, imageName, digest, tag)



