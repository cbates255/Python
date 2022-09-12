import boto3
import pprint



ec2=boto3.client('ec2')
regions=[region['RegionName']
    for region in ec2.describe_regions()['Regions']]
print(regions)

#for region in regions:
    #ec2=boto3.resource('ec2', region_name=region)
    #print('Region:', region)
