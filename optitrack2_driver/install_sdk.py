import requests
import tarfile
import os

print('Downloading started')

url='https://s3.amazonaws.com/naturalpoint/software/NatNetSDKLinux/ubuntu/NatNet_SDK_4.0_ubuntu.tar'
req = requests.get(url)

filename='NatNetSDK.tar'

with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading completed')

print('Extracting started')
tar = tarfile.open(filename)
tar.extractall(path='NatNetSDK/')
tar.close()
print('Extracting completed')

os.remove(filename)
print('Removed extra files')
