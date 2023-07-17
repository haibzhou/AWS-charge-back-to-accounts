#get route table id for subnet
import boto3
import argparse
import json


def get_route_table_id(profile, region):
    #describe route tables for profile and region
    session = boto3.Session(profile_name=profile, region_name=region)
    ec2 = session.client('ec2')
      
    route_tables = ec2.describe_route_tables()
    return route_tables
    
def search_route_table_id(profile, region, vpcid,subnetid):
    #get entire route table for this account and this region
    route_table_region = get_route_table_id(profile, region)
    #extract each route tables associations
    for route_table in route_table_region['RouteTables']:
        for association in route_table['Associations']:
            #check if there is subnet id in association
            #if there is no subnet id in association, it is associated with main route table for the VPC
            if 'SubnetId' in association:
                subnet_routeatble_id = association['RouteTableId']
            
            #check if association is main route table for the VPC
            if association['Main'] == True:
              vpcid_routeable = route_table['VpcId']
              owner_id_routetable  = route_table['OwnerId']
              if(profile == owner_id_routetable) and (vpcid == vpcid_routeable):
                  subnet_routetable_id = association['RouteTableId']
    
        #print each route
        #for route in routes:
           # print(route)
    return subnet_routetable_id


#main program
if __name__ == '__main__':

    #open file describe-subnets_no_rtb.txt
    file = open('describe-subnets_no_rtb.txt', 'r')
    file_out = open('describe-subnets.txt', 'w')
    #get all the route table id for this account and this region
    for line in file:
        print(line)
        #strip the \n from the end of the line
        line = line.rstrip()
        #get profile and region
        profile, region, vpcid, avaibility_zone_id,subnetid, cidr_block = line.split(',')
        #get route table id for this account and this region
        response = search_route_table_id(profile, region, vpcid, subnetid)
        output = profile + ',' + region + ',' + vpcid + ',' + avaibility_zone_id + ',' + subnetid + ',' + cidr_block + ',' + response + '\n'
        print(output)
        file_out.write(output)
        
    file.close()
    file_out.close()
        
    
   
    
                
                
                
            
                
    
    
 
  
    

    
    



        

    
