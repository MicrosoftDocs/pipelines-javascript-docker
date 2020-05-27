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

def upload_data(lastUpdatedDatetime, deployer, imageName, digest):
    url = "http://ttdata.life:7061/uploaddata"
    device_data = [{
    'last_updated_datetime': lastUpdatedDatetime,
    'name': imageName,
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
    digest = 'abcdef' #sys.argv[1]
    lastUpdatedTime = '12/12/1998' #sys.argv[3]
    deployer = 'Nimai' #sys.argv[4]
    imageName = 'nimaipipelinesjavascriptdocker' #sys.argv[5]

    register(imageName)
    upload_data(lastUpdatedTime, deployer, imageName, digest)



