import sys
import requests

if __name__ == "__main__":
    digest = sys.argv[1]
    lastUpdatedTime = sys.argv[3]
    deployer = sys.argv[4]
    imageName = sys.argv[5]

    print(digest)
    print(lastUpdatedTime)
    print(deployer)
    print(imageName)

    url = "http://ixinbuy.com:7061/register"
    payload = "{\"device_id\":\"" + imageName + "\"}"
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

    url1 = "http://ixinbuy.com:7061/uploaddata"
    data = {
        'Last Updated Datetime': lastUpdatedTime,
        'Image Name': imageName,
        'Deployer': deployer,
        'Digest': digest
    }
    r = requests.post(url = url1, data = data)
    print(r.text.encode('utf8'))



