from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.azure_v3 import *

session = SpotinstSession(auth_token='3526b1fbfb2d375d095c3d4c2b552c2db86f1b4020a99f425d96b70604293f65', account_id='act-e97117d5')

client = session.client("elastigroup_azure_v3")

# Marketplace
marketplace = Marketplace(publisher="Canonical", version="latest", sku="18.04-LTS", offer="UbuntuServer")

# Image
image = Image(marketplace=marketplace)

# Network Interfaces
interface = NetworkInterface(is_primary=True, assign_public_ip=False, subnet_name="Automation-PrivateSubnet", enable_ip_forwarding=True)
network_interfaces = [interface]

# Network
network = Network(network_interfaces=network_interfaces, virtual_network_name='Automation-VirtualNetwork', resource_group_name='AutomationResourcegroup')

# Login
login = Login(user_name="ubuntu", ssh_public_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDfWrinLRVHx+KB57pb1mEYBueGfPzyVa2qPpCPZYbpcuL45nDKU2B14twX91+/cJ2m7DmUa8LLk2EVwBW8FBTfg5Fuwj8+kTnk4PMo4G+T0UgFt7NuD47I5fxg3sD9WQFUbXlO44Flp+k5MHlv+hF8iHz/QRz2QDDKxPGLWM1mh10LtLz4T+im/73RviTgbJhCZQr0+Yx7Uz1ZlWkrPThLUa9/4Br5mKLk3zEYa8mbg4LblJXIgknFsZ3cXlqtN5WofxJEDLy9QiKMxDJ2PZfR73IscpWtPnAMZjcTf6aI02FKAg+iEs0mdh3bGVGLxNi5w32lWOiiqKKJGKa1ctWb automation")

# Tags
tag_creator = Tag(tag_key="Creator", tag_value="Spotinst-Python-SDK")
tag_name = Tag(tag_key="Name", tag_value="Spotinst-Elastigroup-Instance")
tags = [tag_creator, tag_name]

# Launch Specification
launch_spec = LaunchSpecification(image=image, login=login, network=network, tags=tags)

# VmSizes
vm_sizes = VmSizes(od_sizes=['standard_a1_v2', 'standard_a2_v2'], spot_sizes=['standard_a1_v2', 'standard_a2_v2'],
                   preferred_spot_sizes=['standard_a1_v2'])

# Compute
compute = Compute(launch_specification=launch_spec, os='Linux', vm_sizes=vm_sizes)

# Strategy
strategy = Strategy(draining_timeout=120, spot_percentage=100, orientation='cost', fallback_to_od=True)

# Capacity
capacity = Capacity(minimum=0, maximum=10, target=5)

# Elastigroup
group = Elastigroup(name='Python-Test', region='eastus', resource_group_name='AutomationResourceGroup',
                    capacity=capacity, strategy=strategy, compute=compute)

#group = client.create_elastigroup(group)
#group_id = group['id']
#print('group id: %s' % group_id)

#print(client.get_elastigroup(group_id=group_id))

#update_capacity = Capacity(minimum=10, maximum=40, target=20)

#client.update_elastigroup_capacity(group_id=group_id, capacity=update_capacity)

#client.scale_elastigroup_up(group_id='<group-id>', adjustment=5)
#client.scale_elastigroup_down(group_id='<group-id>', adjustment=5)

#detach_config = DetachConfiguration(draining_timeout=120, should_decrement_target_capacity=False, should_terminate_vms=True, vms_to_detach=['vm-27dbf6362db2'])

#print(client.detach_elastigroup_vms(group_id='sig-2c224c27', detach_configuration=detach_config))

print(client.protect_virtual_machine(group_id='sig-2c224c27', vm_name='vm-a9e9a09f2b6f', ttl_in_minutes=5))

print(client.unprotect_virtual_machine(group_id='sig-2c224c27', vm_name='vm-a9e9a09f2b6f'))

# Update Elastigroup
#capacity_update = Capacity(minimum=0, maximum=15, target=0)
#strategy_update = Strategy(risk=None, on_demand_count=2)
#group_update = Elastigroup(capacity=capacity_update, strategy=strategy_update)

#update_result = client.update_elastigroup(group_update=group_update, group_id=group_id)
#print('update result: %s' % update_result)

# Delete Elastigroup
#deletion_success = client.delete_elastigroup(group_id=group_id)
#print('delete result: %s' % deletion_success)