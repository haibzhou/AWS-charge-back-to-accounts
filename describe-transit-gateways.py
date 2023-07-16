#list transit gateway in a region for a given account
import boto3
import sys


def list_transit_gateway_in_region(profile, region):
    session = boto3.Session(profile_name=profile)
    client = session.client('ec2', region_name=region)
    response = client.describe_transit_gateways()
    for tgw in response['TransitGateways']:
        print(tgw['TransitGatewayId'])
        print(tgw['State'])
    #get all transit gateway attachment
    print("g-----------------et all transit gateway attachment")
    
    response = client.describe_transit_gateway_attachments()
    for tgw_attachment in response['TransitGatewayAttachments']:
        print(tgw_attachment['TransitGatewayId'])
        print(tgw_attachment['State'])
        print(tgw_attachment['TransitGatewayAttachmentId'])
        print(tgw_attachment['Association'])
        print(tgw_attachment['Association']['TransitGatewayRouteTableId'])
        print(tgw_attachment['ResourceType'])
        response1 = client.search_transit_gateway_routes(
            TransitGatewayRouteTableId=tgw_attachment['Association']['TransitGatewayRouteTableId'],
            Filters=[
                {           
                    'Name': 'state',
                    'Values': [
                        'active',
                                    ]                
                },          
            ]
            )
        print(response1)
        for route in response1['Routes']:
            print(route['DestinationCidrBlock'])
            print(route['TransitGatewayAttachments'])
          
     

            
        
        

     

   
              
            
                
          
        


            

       
        
   
        
    
    
 


#main program
if __name__ == "__main__":
    list_transit_gateway_in_region('network', 'us-east-1')
 #   list_transit_gateway_in_region('network', 'us-west-2')