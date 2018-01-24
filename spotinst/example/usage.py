import spotinst

# Initialize Spotinst Client with your Personal Access Token
client = spotinst.SpotinstClient(auth_token="YOUR_API_TOKEN_HERE", account_id="act-92d492634")

# Initialize group strategy
strategy = spotinst.aws_elastigroup.Strategy(risk=100, utilize_reserved_instances=False, fallback_to_od=True,
                                             availability_vs_cost="balanced")
# Initialize group capacity
capacity = spotinst.aws_elastigroup.Capacity(minimum=0, maximum=10, target=0, unit="instance")

# Initialize group tags
tag1 = spotinst.aws_elastigroup.Tag(tag_key="Creator", tag_value="Spotinst-Python-SDK")
tag2 = spotinst.aws_elastigroup.Tag(tag_key="Name", tag_value="Spotinst-Python-SDK")
tags = [tag1, tag2]

# Initialize group security group id list
securityGroupId = "sg-46e6b33d"
securityGroupIds = [securityGroupId]

# Initialize Launch Specification
launchSpec = spotinst.aws_elastigroup.LaunchSpecification(image_id="ami-f173cc91", key_pair="spotinst-oregon",
                                                          tags=tags,
                                                          security_group_ids=securityGroupIds, monitoring=True)

# Initialize Availability Zones
az1 = spotinst.aws_elastigroup.AvailabilityZone(name="us-west-2a", subnet_ids=["subnet-5df28914"])
az_list = [az1]

# Initialize spot and on demand instance types
instance_types = spotinst.aws_elastigroup.InstanceTypes(ondemand="c3.large", spot=["c3.large"])

# Initialize Compute
compute = spotinst.aws_elastigroup.Compute(product="Linux/UNIX", instance_types=instance_types,
                                           availability_zones=az_list,
                                           launch_specification=launchSpec)

# Initialize Elastigroup
group = spotinst.aws_elastigroup.Elastigroup(name="PythonGroup", description="Created by the Python SDK",
                                             capacity=capacity, strategy=strategy,
                                             compute=compute)

print "-------Create Group-------"
# Create elastigroup and retrieve group id
group = client.create_elastigroup(group)
group_id = group['id']
# Retrieve some internal property
utilize_reserved = group['strategy']['utilize_reserved_instances']
print group_id

print "-------Get Group-------"
# Retrieve a single elastigroup
group = client.get_elastigroup(group_id=group_id)

print "-------Update Group-------"
capacity_update = spotinst.aws_elastigroup.Capacity(minimum=0, maximum=15, target=0)
strategy_update = spotinst.aws_elastigroup.Strategy(risk=None, on_demand_count=2)
group_update = spotinst.aws_elastigroup.Elastigroup(capacity=capacity_update, strategy=strategy_update)

group_after_update = client.update_elastigroup(group_update=group_update, group_id=group_id)
print group_after_update

print "-------Update Only AMI-------"
update_lspec = spotinst.aws_elastigroup.LaunchSpecification(image_id="ami-12345")
update_compute = spotinst.aws_elastigroup.Compute(launch_specification=update_lspec)
group_update = spotinst.aws_elastigroup.Elastigroup(compute=update_compute)

group_after_update = client.update_elastigroup(group_update=group_update, group_id=group_id)
print group_after_update

print "-------Roll Group-------"
group_roll = spotinst.aws_elastigroup.Roll(batch_size_percentage=50, grace_period=600)
roll_response = client.roll_group(group_id=group_id, group_roll=group_roll)
print roll_response

# Delete elastigroup
deletion_success = client.delete_elastigroup(group_id=group_id)

print "-------Delete Group-------"
print deletion_success

# Retrieve all elastigroups and print their names and ids, and delete groups with the string "PythonGroup" in their name
groups = client.get_elastigroups()
for currgroup in groups:
    currgroup_id = currgroup['id']
    currgroup_name = currgroup['name']
    if currgroup_name == "name-i-am-looking-for":
        id_i_am_looking_for = currgroup_id
    print  currgroup_id + "-" + currgroup_name
    active_instances = client.get_elastigroup_active_instances(group_id=currgroup_id)
    print active_instances
    if "PythonGroup" in currgroup_name:
        client.delete_elastigroup(currgroup_id)

# To delete a stateful group and deallocate its resource
stateful_group_id = "sig-12345"
stateful_deallocation = spotinst.aws_elastigroup.StatefulDeallocation(
    should_delete_images=True,
    should_delete_network_interfaces=False,
    should_delete_snapshots=False,
    should_delete_volumes=True)

deletion_success = client.delete_elastigroup_with_deallocation(group_id=stateful_group_id,stateful_deallocation=stateful_deallocation)

print "-------Scale Group Up-------"
scale_up_result = client.scale_elastigroup_up(group_id=group_id, adjustment=3)
print(scale_up_result)

print "-------Detach Instances from Group-------"
group_detach_request = spotinst.aws_elastigroup.DetachConfiguration(
    instances_to_detach=['i-0fbd783a48fb50414', 'i-0cf19a275a381a034'],
    should_decrement_target_capacity=True)
detach_response = client.detach_elastigroup_instances(group_id=group_id,
                                                      detach_configuration=group_detach_request)
print detach_response


