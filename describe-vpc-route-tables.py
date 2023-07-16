#create function to describe vpc route tables
import boto3
import json
import sys


def describe_vpc_route_tables(profile, region):
    session = boto3.Session(profile_name=profile, region_name=region)
    client = session.client('ec2')
    response = client.describe_route_tables()
    #print(response)
    #print each route table entries
    for route_table in response['RouteTables']:
        #print vpc id
        print(route_table['VpcId'])
        #print route table id
        print(route_table['RouteTableId'])
        #print route table name
        #print(route_table['RouteTableName'])
        #print route table entries
        #print(route_table['Routes'])
        #print route table associations
        print(route_table['Associations'])
        print()
        for route in route_table['Routes']:
            print(route)
            #print route destination
            print(route['DestinationCidrBlock'])
            #check if GateId is present
            if 'GatewayId' in route:
                print(route['GatewayId'])
                print()
                continue
            #check if NatGatewayId is present
            if 'NatGatewayId' in route:
                print(route['NatGatewayId'])
                print()
                continue
            #check if NetworkInterfaceId is present
            if 'NetworkInterfaceId' in route:
                print(route['NetworkInterfaceId'])
                print()
                continue
            #check if VpcPeeringConnectionId is present
            if 'VpcPeeringConnectionId' in route:
                print(route['VpcPeeringConnectionId'])
                print()
                continue
            #check if VpcEndpointId is present
            if 'VpcEndpointId' in route:
                print(route['VpcEndpointId'])
                print()
                continue
            #check if vpc gateway endpoint id is present
            if 'VpcGatewayEndpointId' in route:
                print(route['VpcGatewayEndpointId'])
                print()
                continue
            #check if VpcPeeringConnectionId is present
            if 'VpcPeeringConnectionId' in route:
                print(route['VpcPeeringConnectionId'])
                print()
                continue
            #check if transit gateway id is present
            if 'TransitGatewayId' in route:
                print(route['TransitGatewayId'])
                print()
                continue
            #check if local gateway id is present
            if 'LocalGatewayId' in route:
                print(route['LocalGatewayId'])
                print()
                continue
            #check if igw id is present
            if 'IgwId' in route:
                print(route['IgwId'])
                print()
                continue
            #check if load balancer id is present
            if 'LoadBalancerId' in route:
                print(route['LoadBalancerId'])
                print()
                continue
            #check if firewall id is present
            if 'FirewallId' in route:
                print(route['FirewallId'])
                print()
                continue
            #check if gateway load balancer id is present
            if 'GatewayLoadBalancerId' in route:
                print(route['GatewayLoadBalancerId'])
                print()
                continue
            #check if direct connect gateway id is present
            if 'DirectConnectGatewayId' in route:
                print(route['DirectConnectGatewayId'])
                print()
                continue
            print()

    return response

#main program
if __name__ == '__main__':
    profile = 'network'
    region = 'us-east-1'
    describe_vpc_route_tables(profile, region)
    
    profile = 'network'
    region = 'us-west-2'
    describe_vpc_route_tables(profile, region)
    
    profile = 'sales'
    region = 'us-east-1'
    describe_vpc_route_tables(profile, region)
    
    profile = 'sales'
    region = 'us-west-2'
    describe_vpc_route_tables(profile, region)
    
    
    profile = 'hr'
    region = 'us-east-1'
    describe_vpc_route_tables(profile, region)
    
    profile = 'hr'
    region = 'us-west-2'
    describe_vpc_route_tables(profile, region)
    



        
        
        

