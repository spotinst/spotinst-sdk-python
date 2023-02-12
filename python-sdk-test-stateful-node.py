from spotinst_sdk2 import SpotinstSession

from spotinst_sdk2.models.stateful_node import *

session = SpotinstSession(auth_token='3526b1fbfb2d375d095c3d4c2b552c2db86f1b4020a99f425d96b70604293f65', account_id='act-e97117d5')

client = session.client("stateful_node_azure")

############################# Compute ##############################

# Boot Diagnostics

boot_diagnostics = BootDiagnostics(is_enabled = True, type = "managed")

data_disks = [DataDisk(lun = 0, size_g_b=30, type = 'Standard_LRS'), DataDisk(lun = 1, size_g_b=32, type = 'StandardSSD_LRS')]
os_disk = OsDisk(size_g_b = 30, type = 'Standard_LRS')
marketplace = Marketplace(publisher = "Canonical", version = "latest", sku = "18.04-LTS", offer = "UbuntuServer")
image = Image(marketplace = marketplace)



# Network Interfaces

interface = NetworkInterface(is_primary = True, assign_public_ip = True, subnet_name = "Automation-PrivateSubnet",
                             enable_i_p_forwarding = True)

network_interfaces = [interface]



# Network
network = Network(network_interfaces = network_interfaces, virtual_network_name = 'Automation-VirtualNetwork',
                    resource_group_name = 'AutomationResourceGroup')

# Login
login = Login(user_name = "ubuntu",
              ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDfWrinLRVHx+KB57pb1mEYBueGfPzyVa2qPpCPZYbpcuL45nDKU2B14twX91+/cJ2m7DmUa8LLk2EVwBW8FBTfg5Fuwj8+kTnk4PMo4G+T0UgFt7NuD47I5fxg3sD9WQFUbXlO44Flp+k5MHlv+hF8iHz/QRz2QDDKxPGLWM1mh10LtLz4T+im/73RviTgbJhCZQr0+Yx7Uz1ZlWkrPThLUa9/4Br5mKLk3zEYa8mbg4LblJXIgknFsZ3cXlqtN5WofxJEDLy9QiKMxDJ2PZfR73IscpWtPnAMZjcTf6aI02FKAg+iEs0mdh3bGVGLxNi5w32lWOiiqKKJGKa1ctWb automation")



# Tags
tag_creator = Tag(tag_key = "Creator", tag_value="Spotinst-Python-SDK")
tag_name = Tag(tag_key = "Name", tag_value="Spotinst-Stateful-Node")
tags = [tag_creator, tag_name]

# Launch Specification
launch_spec = LaunchSpecification(
                                    boot_diagnostics = boot_diagnostics, 
                                    image = image, 
                                    login = login, 
                                    network = network,
                                    tags = tags, 
                                    os_disk = os_disk, 
                                    custom_data = "TXkgQ3VzdG9tIERhdGE=",
                                  shutdown_script = "TXkgU2h1dGRvd24gU2NyaXB0", 
                                  data_disks = data_disks)



# VmSizes
vm_sizes = VmSizes(od_sizes = ['standard_a1_v2', 'standard_a2_v2'],
                    spot_sizes = ['standard_a1_v2', 'standard_a2_v2'],
                    preferred_spot_sizes = ['standard_a1_v2'])

# Compute

compute = Compute(launch_specification = launch_spec, os = 'Linux', vm_sizes = vm_sizes, preferred_zone="1", zones=["1", "2", "3"])

############################# Strategy ##############################

strategy = Strategy(draining_timeout = 240, fallback_to_od = True, preferred_lifecycle="spot", revert_to_spot=RevertToSpot(perform_at="always"))

############################# Health ################################

health = Health(health_check_types=["vmState"], auto_healing=True, grace_period=350, unhealthy_duration=300)

############################# Scheduling #############################

# Scheduling Task

scheduling_task_1 = SchedulingTask(is_enabled = True, cron_expression = "* * * 1 *", type = "pause")
scheduling_task_2 = SchedulingTask(is_enabled = True, cron_expression = "*/2 * * * *", type = "resume")

# Scheduling
scheduling = Scheduling(tasks = [scheduling_task_1, scheduling_task_2])

############################# Persistence #############################
persistence = Persistence(data_disks_persistence_mode="reattach", os_disk_persistence_mode="reattach",should_persist_data_disks=False, should_persist_os_disk=True, should_persist_network=False)

# Stateful Node

node = StatefulNode(name = 'Python-Test', 
                    region = 'eastus',
                    description="This is a Test Run",
                    resource_group_name = 'AutomationResourceGroup',
                    persistence=persistence, 
                    strategy = strategy, 
                    compute = compute, 
                    scheduling = scheduling, 
                    health = health
                    )

response = client.create_stateful_node(node)

ssi_id = response['id']

print('group id: %s' %ssi_id)



#print(client.get_elastigroup(group_id=group_id))



#update_capacity = Capacity(minimum=10, maximum=40, target=20)



#client.update_elastigroup_capacity(group_id=group_id, capacity=update_capacity)



#client.scale_elastigroup_up(group_id='<group-id>', adjustment=5)

#client.scale_elastigroup_down(group_id='<group-id>', adjustment=5)



#detach_config = DetachConfiguration(draining_timeout=120, should_decrement_target_capacity=False, should_terminate_vms=True, vms_to_detach=['vm-27dbf6362db2'])



#print(client.detach_elastigroup_vms(group_id='sig-2c224c27', detach_configuration=detach_config))



#print(client.protect_virtual_machine(group_id='sig-2c224c27', vm_name='vm-a9e9a09f2b6f', ttl_in_minutes=5))



#print(client.unprotect_virtual_machine(group_id='sig-2c224c27', vm_name='vm-a9e9a09f2b6f'))



# Update Elastigroup

#capacity_update = Capacity(minimum=0, maximum=15, target=0)

#strategy_update = Strategy(risk=None, on_demand_count=2)

#group_update = Elastigroup(capacity=capacity_update, strategy=strategy_update)



#update_result = client.update_elastigroup(group_update=group_update, group_id=group_id)

#print('update result: %s' % update_result)



# Delete Elastigroup

#deletion_success = client.delete_elastigroup(group_id=group_id)

#print('delete result: %s' % deletion_success)