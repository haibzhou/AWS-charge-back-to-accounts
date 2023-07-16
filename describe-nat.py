#create function to list all NAT gateways
import boto3
def list_nat_gateways(profile, region):
#list all nat gateways
    session = boto3.Session(profile_name=profile, region_name=region)
    ec2 = session.client('ec2')
    response = ec2.describe_nat_gateways()
    print(response)
    return response


        
#main program
if __name__ == '__main__':
    profile='default'
    region='us-east-1'
    response = list_nat_gateways('default', 'us-east-1')
    
        
            
        