#get all subnets for network in us-east-1

import boto3
import sys
import json

def list_subnets(profile, region):

    session = boto3.Session(profile_name=profile)
    ec2=session.resource('ec2', region_name=region)
    for subnet in ec2.subnets.all():  
        json_data = {"owner_id":subnet.owner_id,"region":region,"vpc_id":subnet.vpc_id,"availability_zone_id":subnet.availability_zone_id,"subnet_id":subnet.id,"cidr_block":subnet.cidr_block}


        print(json_data)
      #  print(region, subnet.vpc_id, subnet.availability_zone_id, subnet.id, subnet.cidr_block, subnet.owner_id) 
      #  subnet = subnet.owner_id+',' +region+','+ subnet.vpc_id+','+ subnet.availability_zone_id+','+ subnet.id+','+ subnet.cidr_block+ '\n'
      #  file.write(subnet)
        file.write(json.dumps(json_data)+'\n')
            

 #main program
if __name__ == '__main__':
    #open file for writing
    file = open("describe-subnets.txt", "w")
   # file.write('owner_id,region,vpc_id,availability_zone_id,subnet_id,cidr_block\n')

    list_subnets('network', 'us-east-1', )
    list_subnets('network', 'us-west-2')
    list_subnets('sales', 'us-east-1')
    list_subnets('sales', 'us-west-2')
    list_subnets('hr', 'us-east-1')
    list_subnets('hr', 'us-west-2')
    
    file.close()



        
