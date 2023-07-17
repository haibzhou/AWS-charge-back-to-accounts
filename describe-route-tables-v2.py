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

#main program
if __name__ == '__main__':


    #get entire route table for this account and this region
    route_table_region = get_route_table_id('083820776020', 'us-east-1')
    #extract each route tables associations
    for route_table in route_table_region['RouteTables']:
        
      
        
        for association in route_table['Associations']:
            print(association)
            
            #check if there is subnet id in association
            #if there is no subnet id in association, it is associated with main route table for the VPC
            if 'SubnetId' in association:
                print(association['SubnetId'])
                #print route table id in association
                print(association['RouteTableId'])
            
            #find the main route table id for the VPC
            if 'Main' in association:
                print('main route table')
                print(association['RouteTableId'])
                print(route_table['VpcId'])
        #print Routes
        routes = route_table['Routes']
        #print each route
        for route in routes:
            print(route)
                
                
                
            
                
    
    
 
  
    

    
    



        

    
