
import boto3
import json

#create function to find transit gateway attachments
def find_transit_gateway_attachments(vpc_id, transit_gateway_id, profile, region):
    session = boto3.Session(profile_name=profile, region_name=region)
    client = session.client('ec2')
   #find the transit gateway attachments for resource vpc-0044c21873e5dea1b
    try:
        response = client.describe_transit_gateway_attachments(
            Filters=[
                {
                    'Name': 'resource-id',
                    'Values': [
                        vpc_id,
                    ]
                },
                {
                    'Name': 'transit-gateway-id',
                    'Values': [
                        transit_gateway_id,
                    ]
                },
            ]
        )
        #get transit gateway attachments ids
        TransitGatewayAttachmentIds = []
        for transit_gateway_attachment in response['TransitGatewayAttachments']:
            TransitGatewayAttachmentIds.append(transit_gateway_attachment['TransitGatewayAttachmentId'])
            print(TransitGatewayAttachmentIds[0])
            
        #get transit gateway route table ids for each attachments Association
        TransitGatewayRouteTableIds = []
        for transit_gateway_attachment in response['TransitGatewayAttachments']:
            if transit_gateway_attachment['TransitGatewayAttachmentId'] == TransitGatewayAttachmentIds[0]:
            #get route table ids from transit gateway associations
              TransitGatewayRouteTableIds.append(transit_gateway_attachment['Association']['TransitGatewayRouteTableId'])
              print(TransitGatewayRouteTableIds)
        
      

    
        return TransitGatewayRouteTableIds
    except Exception as e:
        raise e
   
    
#create function to find transit gateways
def find_transit_gateway(profile, region):
    session = boto3.Session(profile_name=profile, region_name=region)
    client = session.client('ec2')
    try:
        response = client.describe_transit_gateways(
            
        )
        #get transit gateway ids
        TransitGatewayIds = []
        for transit_gateway in response['TransitGateways']:
            TransitGatewayIds.append(transit_gateway['TransitGatewayId'])
        return TransitGatewayIds
    
    except Exception as e:
        raise e

#search transit gateway routes
def search_transit_gateway_routes(transit_gateway_route_table_id, destination_cidr_block, profile, region):
    session = boto3.Session(profile_name=profile, region_name=region)
    client = session.client('ec2')
    #search the transit gateway routes to find next hop to destination cidr block in matched transit_gateway_route_table_id
    
    response = client.search_transit_gateway_routes(
        TransitGatewayRouteTableId=transit_gateway_route_table_id,
        #set filter to route-seatch that match supernet of destination_cidr_block, it will match 0.0.0.0/0 too
        Filters=[
            {
                'Name': 'route-search.supernet-of-match',
                'Values': [
                    destination_cidr_block,
                    
                    
                ]
                
            }
        ]
      
    )
    #find the longest match
    
    for route in response['Routes']:
        destination_cidr_block = route['DestinationCidrBlock']
        best_prefix_length = 0
        prefix_length = int(destination_cidr_block.split('/')[1])
        if prefix_length >= best_prefix_length:
            best_prefix_length = prefix_length
            best_route = route
        
    print(best_route)   
    return best_route 
    
#main program
if __name__ == "__main__":
#list all transit gateways in account network and region us-east-1
  
    #call function to find transit gateways in account network and region us-east-1 
    transit_gateway_ids = find_transit_gateway('network', 'us-east-1')
    print(transit_gateway_ids)
    #cextract transit gateway ids from list of transit gateways
    tgw_ids = [transit_gateway_ids[0]][0]
    print(tgw_ids)
    
    vpc_id = 'vpc-0044c21873e5dea1b'
    #call function to find transit gateway attachments
    transit_gateway_rtb_id = find_transit_gateway_attachments(vpc_id, tgw_ids, 'network', 'us-east-1')
    tgw_rbt_id = transit_gateway_rtb_id[0]
    print(tgw_rbt_id)
    
    #search transit gateway routes to find best match to destination cidr block in matched transit_gateway_route_table_id
    response = search_transit_gateway_routes(tgw_rbt_id, '10.2.0.0/24', 'network', 'us-east-1')
    print(response)
    

    
    
    
 
    
        

 