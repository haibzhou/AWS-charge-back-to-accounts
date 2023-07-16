import boto3
import json
#Find the packet path from source subnet to destination subnet using AWS EC2.
#import boto3
#import json
#import sys

#open file subnets-src-dst-matrix.txt
subnets_src_dst_matrix = open("subnets-src-dst-matrix_json.txt", "r")
#read the file line by line
for line in subnets_src_dst_matrix:
    #load line to json format
    json_line = json.loads(line)
    for data in json_line:
        #get source subnnet information
        src_subnet = json.loads(data['source'])
        print('src_subnet')
        
        for key in src_subnet:
            if key == 'subnet_id':
                src_subnet_id = src_subnet[key]
                print(src_subnet_id)
            if key == 'vpc_id':
                src_vpc_id = src_subnet[key]
                print(src_vpc_id)   
            if key == 'cidr_block':
                src_cidr_block = src_subnet[key]
                print(src_cidr_block)
            if key == 'availability_zone_id':
                src_availability_zone_id = src_subnet[key]
                print(src_availability_zone_id)
            if key == 'owner_id':
                src_owner_id = src_subnet[key]
                print(src_owner_id)

        
        #get destination subnnet information
        print('dst_subnet')
        dst_subnet = json.loads(data['destination'])
        for key in dst_subnet:
            if key == 'subnet_id':
                dst_subnet_id = dst_subnet[key]
                print(dst_subnet_id)
            if key == 'vpc_id':
                dst_vpc_id = dst_subnet[key]
                print(dst_vpc_id)   
            if key == 'cidr_block':
                dst_cidr_block = dst_subnet[key]
                print(dst_cidr_block)
            if key == 'availability_zone_id':
                dst_availability_zone_id = dst_subnet[key]
                print(dst_availability_zone_id)
            if key == 'owner_id':
                dst_owner_id = dst_subnet[key]
                print(dst_owner_id)
    print("=============================== ")   



        
