#Create function to describe instances
import boto3
def list_instances(profile, region):
    session = boto3.Session(profile_name=profile)
    ec2=session.resource('ec2', region_name=region)
    for instance in ec2.instances.all():
        print(instance.id, instance.key_name)
        for tag in instance.tags:
            print(tag['Key'], tag['Value'])
        
    #print all network interfaces eni for this instance
        for eni in instance.network_interfaces:
            print(instance.id,eni.id, eni.subnet_id)
            print(instance.id,eni.id, eni.vpc_id)
            print(instance.id,eni.id, eni.private_ip_address)
            print(instance.id,eni.id, eni.status)
            print(instance.id,eni.id, eni.owner_id)
            print(instance.id,eni.id, eni.network_interface_id)

#main program
if __name__ == '__main__':
    list_instances('network', 'us-east-1')
    list_instances('network', 'us-west-2')
    list_instances('sales', 'us-east-1')
    list_instances('sales', 'us-west-2')
    list_instances('hr', 'us-east-1')
    list_instances('hr', 'us-west-2')

