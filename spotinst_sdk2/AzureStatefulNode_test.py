import sys
sys.path.append("C:\GitHubProjects\TestDemo\Synced-Version\spotinst-sdk-python\spotinst_sdk2")
from spotinst_sdk2 import SpotinstSession

from spotinst_sdk2.models.stateful_node import *

session = SpotinstSession(auth_token='7821a95f9184fb5b3c4ee212203dda373bbeec505521042c13c1a9b5f63946b7',
                          account_id='act-e97117d5')

client = session.client("stateful_node_azure", log_level="debug")

# strategy = Strategy(preferred_lifecycle = PreferredLifeCycle.spot.value,
#                     capacity_reservation=CapacityReservation(capacity_reservation_groups=[CapacityReservationGroups(name="Test", resource_group_name="AutomationResourceGroup", should_prioritize=True)],
#                                                              should_utilize=True,
#                                                              utilization_strategy=UtilizationStrategy.utilize_over_spot.value),
#                     draining_timeout=180,
#                     fallback_to_od=True,
#                     od_windows=["Sun:23:00-Mon:02:30"],
#                     optimization_windows=["Mon:03:00-Wed:02:30"],
#                     revert_to_spot=RevertToSpot(perform_at=PerformAt.always.value),
#                     signals=[Signal(timeout=180,
#                                    type=SignalType.vm_ready.value)],
#                     availability_vs_cost=100)

# compute = Compute(launch_specification=LaunchSpecification(boot_diagnostics=BootDiagnostics(is_enabled=True,
#                                                                                             storage_uri=none,
#                                                                                             type=StorageType.managed.value),
#                                                            # custom_data="",
#                                                            data_disks=[DataDisk(lun=1, size_g_b=1, type=DataDiskType.standard_lrs.value)],
#                                                            extensions=[Extension(api_version="2.0",minor_version_auto_upgrade=True,
#                                                                                  name="extensionName",
#                                                                                  publisher="Microsoft.Azure.Extensions",
#                                                                                  type="customScript")],
#                                                            image=Image(marketplace=Marketplace(publisher="Canonical", offer="0001-com-ubuntu-server-jammy",
#                                                                                                sku="22_04-lts-gen2",
#                                                                                                version="latest")),
#                                                                        # custom=Custom(resource_group_name="spotinst-azure",
#                                                                        #               name="custom-image-name"),
#                                                                        # gallery=Gallery(gallery_name="gallery-name",
#                                                                        #                 image_name="gallery-image-name",
#                                                                        #                 resource_group_name="spotinst-azure",
#                                                                        #                 spot_account_id="act-123456789",
#                                                                        #                 version_name="0.0.1")),
#                                                            # license_type="Windows_Client",
#                                                            load_balancers_config=LoadBalancerConfig(load_balancers=[LoadBalancer(backend_pool_names=["Automation-Lb-BackendPool"],
#                                                                                                                                  load_balancer_sku="Standard",
#                                                                                                                                  name="Automation-Lb",
#                                                                                                                                  resource_group_name="AutomationResourceGroup",
#                                                                                                                                  type=LoadBalancerType.load_balancer.value)]),
#                                                            login=Login(ssh_public_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDfWrinLRVHx+KB57pb1mEYBueGfPzyVa2qPpCPZYbpcuL45nDKU2B14twX91+/cJ2m7DmUa8LLk2EVwBW8FBTfg5Fuwj8+kTnk4PMo4G+T0UgFt7NuD47I5fxg3sD9WQFUbXlO44Flp+k5MHlv+hF8iHz/QRz2QDDKxPGLWM1mh10LtLz4T+im/73RviTgbJhCZQr0+Yx7Uz1ZlWkrPThLUa9/4Br5mKLk3zEYa8mbg4LblJXIgknFsZ3cXlqtN5WofxJEDLy9QiKMxDJ2PZfR73IscpWtPnAMZjcTf6aI02FKAg+iEs0mdh3bGVGLxNi5w32lWOiiqKKJGKa1ctWb automation",
#                                                                        user_name="ubuntu"),
#                                                                        # password="password"),
#                                                            managed_service_identities=[ManagedServiceIdentity(resource_group_name="MC_AutomationResourceGroup_aks-np-test_eastus", name="aks-np-test-agentpool")],
#                                                            network=Network(network_interfaces=[NetworkInterface(additional_ip_configurations=[AdditionalIpConfiguration(name="testIp",
#                                                                                                                                                                         private_ip_address_version=PrivateIpAddressVersion.ipv4.value)],
#                                                                                                                 application_security_groups=[ApplicationSecurityGroup(name="Terraform-Testing-ASG",
#                                                                                                                                                                       resource_group_name="AutomationResourceGroup")],
#                                                                                                                 assign_public_ip=True,
#                                                                                                                 enable_ip_forwarding=True,
#                                                                                                                 is_primary=True,
#                                                                                                                 network_security_group=NetworkSecurityGroup(name="Automation-NSG-PrivateSubnet",
#                                                                                                                                                             resource_group_name="AutomationResourceGroup"),
#                                                                                                                 # private_ip_addresses=["172.23.4.20"],
#                                                                                                                 public_ips=[PublicIp(name="ImportDeletionOfVM-ip", resource_group_name="AutomationResourceGroup")],
#                                                                                                                 public_ip_sku=PublicIpSku.standard.value,
#                                                                                                                 subnet_name="Automation-PrivateSubnet")],
#                                                                            virtual_network_name="Automation-VirtualNetwork",
#                                                                            resource_group_name="AutomationResourceGroup"),
#                                                            os_disk=OsDisk(size_g_b=31,
#                                                                           type=DataDiskType.standard_lrs.value),
#                                                            # proximity_placement_groups=[ProximityPlacementGroups(name="TestTerraformProximityPlacementGroup",
#                                                            #                                                      resource_group_name="AutomationResourceGroup")],
#                                                            # secrets=[Secret(source_vault=SourceVault(name="name", resource_group_name="rgname"),
#                                                            #                 vault_certificates=[VaultCertificate(certificate_store="string",
#                                                            #                                                      certificate_url="string")])],
#                                                            security=Security(secure_boot_enabled=True, security_type=SecurityType.trusted_launch.value, v_tpm_enabled=True),
#                                                            shutdown_script="IyEvdXNyL2Jpbi9lbnYgYmFzaAoiR29vZGJ5ZSBvbGQgaW5zdGFuY2Ui",
#                                                            tags=[Tag(tag_key="env", tag_value="staging")],
#                                                            user_data="SXlFdlltbHVMMkpoYzJnS1pXTm9ieUFpZEdWemRDSQ==",
#                                                            # vm_name="devVm1",
#                                                            vm_name_prefix="prefix"),
#                   os=OsType.linux.value,
#                   # preferred_zone="1",
#                   # zones=["1", "2"],
#                   vm_sizes=VmSizes(od_sizes=["standard_ds2_v2"],
#                                    preferred_spot_sizes=["standard_ds2_v2"],
#                                    spot_sizes=["standard_ds2_v2", "standard_ds1_v2"]))

# persistence = Persistence(data_disks_persistence_mode=PersistenceMode.on_launch.value,
#                           os_disk_persistence_mode=PersistenceMode.on_launch.value,
#                           should_persist_data_disks=False,
#                           should_persist_network=True,
#                           should_persist_os_disk=True)

# scheduling = Scheduling(tasks=[SchedulingTask(is_enabled=True, cron_expression="35 12 * * *", type=SchedulingTaskType.recycle.value)])

# health = Health(health_check_types=["vmState"], auto_healing=False, grace_period=180, unhealthy_duration=360)

# stateful_node_obj = StatefulNode(compute=compute,
#                                  description="Python SDK Stateful node test",
#                                  health=health,
#                                  name="Message-Center-Do-Not-Delete",
#                                  persistence=persistence,
#                                  region="eastus",
#                                  resource_group_name="AutomationResourceGroup",
#                                  scheduling=scheduling,
#                                  strategy=strategy)

# group_resp = client.create_stateful_node(stateful_node_obj)
#ssn-a0d8d176
#ssn-a46587e7
# client.get_stateful_node("ssn-a0d8d176")
# client.get_all_stateful_nodes(region="eastus")
#client.get_all_stateful_node_costs(from_date="1700499413", to_date="1700867813", owner_id="ssn-615bbd16")
# client.get_all_stateful_node_aggregated_daily_costs(from_date="1700499413", to_date="1700867813", owner_id="ssn-615bbd16")
# client.get_stateful_node_size_usage(from_date="1700499413", to_date="1700867813", owner_id="ssn-a46587e7")

# Prepare Deallocation Config for Stateful Node
dellocate_spec = Deallocate(should_deallocate=True,
                            ttl_in_hours=0)

deallocation_spec = DeallocationConfig(disk_deallocation_config=dellocate_spec,
                                        network_deallocation_config=dellocate_spec,
                                        public_ip_deallocation_config=dellocate_spec,
                                        snapshot_deallocation_config=dellocate_spec,
                                        should_terminate_vm=False,
                                        should_deregister_from_lb=True)

# Delete the Stateful Node
client.delete_stateful_node(
    'ssn-65028dc0', deallocation_spec)