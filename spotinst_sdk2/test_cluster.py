
from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.clients.notification_center import NotificationCenterClient

session = SpotinstSession(auth_token='c6791c1d3bcab7d4179f64f0f4d50f6091bfe7fadaa790ba8e98fc8645e2b576',
                          account_id='act-7c46c6df')
client = session.client("notification_center", log_level="debug")

notificationCenter = NotificationCenterClient(account_id="act-7c46c6df")
# resource_limits = ResourceLimits(max_memory_gib=1000, max_v_cpu=200)
# down = Down(max_scale_down_percentage=60)
# headroom = Headroom(cpu_per_unit=2000, memory_per_unit=0, gpu_per_unit=0, num_of_units=4)
# auto_scaler = AutoScaler(is_enabled=True, cooldown=180, resource_limits=resource_limits, down=down, headroom=headroom,
#                          is_auto_config=False)

# capacity = Capacity(minimum=0, maximum=10, target=6)

# clusterOrientation = ClusterOrientation(availability_vs_cost=AvailabilityVsCost.balanced.value)
# strategy = Strategy(utilize_reserved_instances=True, fallback_to_od=True, spot_percentage=100, grace_period=600,
#                     draining_timeout=60, utilize_commitments=False, cluster_orientation=clusterOrientation,
#                     spread_nodes_by=SpreadNodesBy.count.value)

# clusterRoll = ClusterRoll(batch_size_percentage=20, comment="This cluster is deployed for python sdk testing",
#                           batch_min_healthy_percentage=100, respect_pdb=True)
# parameters = Parameters(cluster_roll=clusterRoll)
# tasks = Tasks(is_enabled=True, cron_expression="0 1 * * *", task_type=TaskType.cluster_roll.value,
#               parameters=parameters)
# shutDownHours = ShutdownHours(time_windows=["Sat:08:00-Sun:08:00"], is_enabled=True)
# scheduling = Scheduling(tasks=[tasks], shutdown_hours=shutDownHours)

# container_image = ContainerImage()
# security = Security(container_image=container_image)

# instance_type_filters = InstanceTypesFilters(architectures=[Architectures.i386.value, Architectures.x86_64.value],
#                                              categories=[Categories.accelerated_computing.value,
#                                                          Categories.compute_optimized.value],
#                                              disk_types=[DiskTypes.nvme.value, DiskTypes.ebs.value],
#                                              exclude_families=["m*"], exclude_metal=False,
#                                              hypervisor=[Hypervisor.nitro.value], include_families=["c*", "t*"],
#                                              is_ena_supported=True, max_gpu=1,
#                                              max_memory_gi_b=16, max_network_performance=20, max_vcpu=16, min_enis=1,
#                                              min_gpu=0, min_memory_gi_b=8,
#                                              min_network_performance=2, min_vcpu=2,
#                                              root_device_types=[RootDeviceTypes.ebs.value],
#                                              virtualization_types=[VirtualizationTypes.hvm.value])
# instanceTypes = InstanceTypes(
    # whitelist=["c4.xlarge",
    #            "c4.2xlarge",
    #            "c4.4xlarge",
    #            "c4.8xlarge"],
    # blacklist=["r5.large",
    #            "r5.xlarge"],
#     filters=instance_type_filters
# )
# iamInstanceProfile = IamInstanceProfile(name="eks-0ac22b2d-42db-6acf-bfb9-784110a9065f")
# ebs = EBS(delete_on_termination=True, encrypted=False, throughput=125,
#           # volume_size=20,
#           volume_type="gp3",
#           iops=100,
#           # kms_key_id="alias/aws/ebs",
#           snapshot_id="snap-022e80ce52365a9ce",
#           dynamic_volume_size=DynamicVolumeSize(base_size=50, resource="CPU", size_per_resource_unit=20))
# blockDeviceMappings = BlockDeviceMappings(device_name="/dev/sdf", ebs=ebs)
# tags = [Tags(tag_key="creator", tag_value="python sdk"), Tags(tag_key="Condition", tag_value="Test")]
# launchSpecification = LaunchSpecifications(security_group_ids=["sg-0121ca2d8d996e6af"],
#                                            iam_instance_profile=iamInstanceProfile,
#                                            key_pair="automation-kp",
#                                            image_id="ami-01dfb5782bffd09d6",
#                                            user_data="TUlNRS1WZXJzaW9uOiAxLjAKQ29udGVudC1UeXBlOiBtdWx0aXBhcnQvbWl4ZWQ7IGJvdW5kYXJ5PSIvLyIKCi0tLy8KQ29udGVudC1UeXBlOiB0ZXh0L3gtc2hlbGxzY3JpcHQ7IGNoYXJzZXQ9InVzLWFzY2lpIgojIS9iaW4vYmFzaApzZXQgLWV4CkI2NF9DTFVTVEVSX0NBPUxTMHRMUzFDUlVkSlRpQkRSVkpVU1VaSlEwRlVSUzB0TFMwdENrMUpTVU12YWtORFFXVmhaMEYzU1VKQlowbENRVVJCVGtKbmEzRm9hMmxIT1hjd1FrRlJjMFpCUkVGV1RWSk5kMFZSV1VSV1VWRkVSWGR3Y21SWFNtd0tZMjAxYkdSSFZucE5RalJZUkZSSmVVMVVSWGRQUkVFeFRsUkJlVTFXYjFoRVZFMTVUVlJGZDA1VVFURk9WRUY1VFZadmQwWlVSVlJOUWtWSFFURlZSUXBCZUUxTFlUTldhVnBZU25WYVdGSnNZM3BEUTBGVFNYZEVVVmxLUzI5YVNXaDJZMDVCVVVWQ1FsRkJSR2RuUlZCQlJFTkRRVkZ2UTJkblJVSkJUVlZWQ25aTmVVNXlaVVIwWnl0bFQzb3ljVUpyUzJSdlFsUTFkeXQ1YTA1eVZHMXBaRmhrWTB0d0swVkVSMXBSWjJ4NWRIZ3JjbUZ4TmtaMGIwUkphMHd6YlhnS2VscHVWR1J0Y1hOWFVXTjRhVkJoZEZac2QxaFNkU3RUT1d4MVpqbDNSMDkwYlhOSVRsVndhbXhuWWk5b1RHUmpjRGd5ZERZMlpubENRV2hWUVdjNFNBcExOV056TVhoTFUwSTFhVThyU1dWcVowNW9Ra3RUYW5ONVEwcG1jbXN4WlhsM09FOU5RMmhuVUVsNmJGTjNkVzg0VEdFNGEyeHNaMWswVW5oTE5FUTBDbWd4WVhJeWMzVXlVbTFCTkRkS2VHMU1RakZOY1N0b2JtZFljazFOTmt0WU1VRnFZVmhPV2xGR1ltcGhjSFJGV1dOWWIzQjJiVXBDVlVKWlFrOXhjbk1LTmpaVFFrVkVjamRWZFVWak9WWnJPSGN5VjJSR2VEZGxWRU5UYlZFNVpYa3ZVVTVyVkZVeFZHNWFWVzR3T0daNGRFaGxVak12ZWt0cU16WlFPRkJpTXdwc1ExUnNSalJLUTA0M1dHdFpSV2hFV0VwVlEwRjNSVUZCWVU1YVRVWmpkMFJuV1VSV1VqQlFRVkZJTDBKQlVVUkJaMHRyVFVFNFIwRXhWV1JGZDBWQ0NpOTNVVVpOUVUxQ1FXWTRkMGhSV1VSV1VqQlBRa0paUlVaRE4xUXpRMmxEUkdaR1MxaFlPRFZIU1ZaV1dqWnRjR3BUUjI1TlFsVkhRVEZWWkVWUlVVOEtUVUY1UTBOdGRERlpiVlo1WW0xV01GcFlUWGRFVVZsS1MyOWFTV2gyWTA1QlVVVk1RbEZCUkdkblJVSkJRM1l3V0RWeWNYbExNRmhHT0ZFMFdsTXJPQXBCVjFaNmFDOWtMMFpsVERkbGNWaEtUMEUxYmxVMll6ZFlMMkZ5UjJKbmVpOU9ablU1T0ZkUFJWWmtXVGhQZWtkVlMzVkZNbkZ5Y2xwS2RIQlZPWGRsQ2xwVWVDOUZhakF3TlZSNGR6aHNibXhhZFZOb0x5c3pSSE13VVVjek1XaFlZMHN2TDFKc1FqWXlWMlJrTUhGSlVIZDBLMGh0VDBzNVRWaDJPVzE1VFdNS2NGSXZWR0ZMTDAwNGMyZFZNa05ZYzJjdmVFTkZhMFU0VjBKd2NTOUNkVTlIYTNrd2JuQjBNbEUxU0dsUU1FRTJaMnhNZVhOSFJuZE5lbGRyZVhZM09BcGFOVWx1UkhFdmVqQXJaRWQ2ZVZOdEszVnlSMWt2WlZGYVJtWm9OR3BwWkZOS01tSnJjbkkxUWpoek5saG1NVlZHZURGTlUzSkhiRVZIY0ZvM1pWSkVDbmRQV1ZOVlVrOUJVRU0wVXpJdlowOVdkM0ZNUTBkVGNrdGxkbmxEU25oMlRXaGFVbXBQUzBsTGQyWXpLMHQ2VWt0TFR6Vm1OSE5pWVZKdVpucDVWRmtLT1ROelBRb3RMUzB0TFVWT1JDQkRSVkpVU1VaSlEwRlVSUzB0TFMwdENnPT0KQVBJX1NFUlZFUl9VUkw9aHR0cHM6Ly8wMzRFRDAwRkE1M0Y0MEVBRjIyMjczMDJCQjlDNTE0OC5ncjcudXMtd2VzdC0yLmVrcy5hbWF6b25hd3MuY29tCks4U19DTFVTVEVSX0ROU19JUD0xMC4xMDAuMC4xMAovZXRjL2Vrcy9ib290c3RyYXAuc2ggRUtTX0F1dG9tYXRpb25fQ2x1c3Rlcl9BUEkgLS1rdWJlbGV0LWV4dHJhLWFyZ3MgJy0tbm9kZS1sYWJlbHM9ZWtzLmFtYXpvbmF3cy5jb20vbm9kZWdyb3VwLWltYWdlPWFtaS0wMWRmYjU3ODJiZmZkMDlkNixla3MuYW1hem9uYXdzLmNvbS9jYXBhY2l0eVR5cGU9T05fREVNQU5ELGVrcy5hbWF6b25hd3MuY29tL25vZGVncm91cD1ORzEgLS1tYXgtcG9kcz0xNycgLS1iNjQtY2x1c3Rlci1jYSAkQjY0X0NMVVNURVJfQ0EgLS1hcGlzZXJ2ZXItZW5kcG9pbnQgJEFQSV9TRVJWRVJfVVJMIC0tZG5zLWNsdXN0ZXItaXAgJEs4U19DTFVTVEVSX0ROU19JUCAtLXVzZS1tYXgtcG9kcyBmYWxzZQoKLS0vLy0t",
#                                            tags=tags,
#                                            # root_volume_size=20,
#                                            use_as_template_only=False,
#                                            block_device_mappings=[blockDeviceMappings],
#                                            associate_public_ip_address=False,
#                                            associate_ipv6_address=False,
#                                            monitoring=True,
#                                            ebs_optimized=True,
#                                            instance_metadata_options=InstanceMetadataOptions(
#                                                http_tokens=HttpTokens.optional.value,
#                                                http_endpoint=HttpEndpoint.disabled.value,
#                                                http_put_response_hop_limit=12))
# compute = Compute(subnet_ids=["subnet-42f1e418", "subnet-8ab89cc1", "subnet-4333093a", "subnet-e623aecd"],
#                   instance_types=instanceTypes,
#                   launch_specification=launchSpecification)
# # logging = Logging(export=Export(s3=S3(id="id-123")))
# ocean_obj = Ocean(name="TestAMRCluster", controller_cluster_id="test-amr-cluster",
#                   region="us-west-2",
#                   auto_scaler=auto_scaler, capacity=capacity, compute=compute, scheduling=scheduling, strategy=strategy)

response = notificationCenter.get_account_resources(account_id="act-7c46c6df")
#response = client.get_all_ocean_cluster()
#response = client.get_ocean_cluster(ocean_id="o-028e5553")
# response = client.update_ocean_cluster(ocean_id="o-028e5553", ocean=ocean_obj, auto_apply_tags="true")
# attribute = Attribute(type=Type.label.value, key="app", operator=Operator.equals.value, value="coredns")
# filter = RightSizingRecommendationFilter(namespaces=["kube-system"], attribute=attribute)
# response = client.fetch_rightsizing_recommendations(ocean_id="o-ccf050ab", filter=filter)
# response = client.delete_ocean_cluster('o-8930e4bc')

# cluster_cost = AggregatedClusterCosts(start_time="2023-05-28T11:35:02.745Z", end_time="2023-05-30T11:30:01.745Z")
# response = client.get_aggregated_cluster_costs("o-6e6e349c", cluster_cost)
# roll = Roll(batch_size_percentage=20, comment="Test cluster roll python sdk", respect_pdb=True,
#             batch_min_healthy_percentage=100)
# response = client.initiate_roll("o-ccf050ab", roll)
# response = client.list_rolls("o-ccf050ab")
# response = client.update_roll("o-ccf050ab", "scr-41601381", status="STOPPED")
# response1 = client.launch_nodes_in_vng(ocean_launch_spec_id="ols-036cafcb",
#                                        amount=1
#                                        #launch_nodes=LaunchNodes(amount=5)
#                                        )
# response = client.get_roll(ocean_id="o-ccf050ab", roll_id="scr-88015376")
# response = client.get_cluster_nodes(ocean_id="o-b9a92410")
# response = client.get_heartbeat_status(ocean_id="o-ccf050ab")
# response = client.instance_types_filter_simulation(ocean_id="o-028e5553", instance_type_filter=instance_type_filters)
# response = client.allowed_instance_types(ocean_id="o-028e5553")
# response = client.get_virtual_node_group(ocean_launch_spec_id="ols-6544c166")
print(response)
