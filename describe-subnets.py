#get all subnets for network in us-east-1

import boto3
def list_subnets(profile, region):
    session = boto3.Session(profile_name=profile)
    ec2=session.resource('ec2', region_name=region)
    for subnet in ec2.subnets.all():
        print(region, subnet.vpc_id, subnet.availability_zone_id, subnet.id, subnet.cidr_block, subnet.owner_id)
#        print(subnet.availability_zone_id)
#        print(subnet.vpc_id)
#        print(subnet.owner_id)
#        #print subnet tag key Name and value
#        print(subnet.tags)

       
        

 #main program
if __name__ == '__main__':
    list_subnets('network', 'us-east-1')
    list_subnets('network', 'us-west-2')
    list_subnets('sales', 'us-east-1')
    list_subnets('sales', 'us-west-2')
    list_subnets('hr', 'us-east-1')
    list_subnets('hr', 'us-west-2')



        