[![Build Status](https://travis-ci.org/spotinst/spotinst-sdk-python.svg?branch=master)](https://travis-ci.org/spotinst/spotinst-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/spotinst/spotinst-sdk-python/badge.svg?branch=master)](https://coveralls.io/github/spotinst/spotinst-sdk-python?branch=master)
[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# spotinst-sdk-python
Spotinst SDK for the Python programming language

## Table of contents
<!--ts-->
   * [Installation](#installation)
   * [Configuring Credentials](#configuring-credentials)
   * [Usage](#usage)
      * [Elastigroup](#elastigroup)
        * [Getting Started With Elastigroup](#getting-started-with-elastigroup)
        * [Elastigroup Additional Configurations](#elastigroup-additional-configurations)
          * [Scaling Policies](#scaling-policies)
          * [Scheduling](#scheduling)
        * [Third Party Integrations](#third-party-integrations)
          * [ECS](#ecs)
          * [EMR](#emr)
          * [Kubernetes](#kubernetes)
          * [Nomad](#nomad)
          * [Docker Swarm](#dockerswarm)
          * [CodeDeploy](#codedeploy)
          * [Route53](#route53)
          * [ElasticBeanstalk](#elasticbeanstalk)
      * [Functions](#functions)
        * [Getting Started With Functions](#getting-started-with-functions)
<!--te-->

## Installation
```bash
pip install --upgrade spotinst-sdk
```

## Configuring Credentials
The mechanism in which the sdk looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. 
The order in which the sdk searches for credentials is:
  1. Passing credentials as parameters to the `SpotinstClient()` constructor
- example
```python
client = SpotinstClient(auth_token='token', account_id='act-123')
```

  2. Fetching the account and token from environment variables under `SPOTINST_ACCOUNT` & `SPOTINST_TOKEN`

If you choose to not pass your credentials directly you configure a credentials file, this file should be a valid `.yml` file.
The default shared credential file location is `~/.spotinst/credentials` and the default profile is `default`
- example
```yaml
default: #profile
  token: $defaul_spotinst_token
  account: $default_spotinst-account-id
my_profle:
  token: $my_spotinst_token
  account: $my_spotinst-account-id
```

  3. You can overwrite the credentials file location and the profile used as parameters in the `SpotinstClient()` constructor
- example
```python
client = SpotinstClient(credentials_file='/path/to/file', profile='my_profile')
```
  
  4. You can overwrite the credentials file location and the profile used as environment variables `SPOTINST_PROFILE` and/or `SPOTINST_SHARED_CREDENTIALS_FILE`
  5. Fetching from the default location with the default profile
  
## Usage

## Elastigroup

### Getting Started With Elastigroup
```python
from spotinst_sdk import SpotinstClient
from spotinst_sdk.aws_elastigroup import *

client = SpotinstClient()

# Initialize group strategy
strategy = Strategy(risk=100, utilize_reserved_instances=False, fallback_to_od=True, availability_vs_cost="balanced")

# Initialize group capacity
capacity = Capacity(minimum=0, maximum=10, target=0, unit="instance")

# Initialize group tags
tag_creator = Tag(tag_key="Creator", tag_value="Spotinst-Python-SDK")
tag_name = Tag(tag_key="Name", tag_value="Spotinst-Elastigroup-Instance")
tags = [tag_creator, tag_name]

# Initialize group security group id list
securityGroupIds = ["sg-46e6b33d"]

# Initialize group instances iam roles
iam_role = IamRole(name='s3ReadOnly', arn='arn:aws:iam:us-east-1:123456789012:environment/s3ReadOnly')

# Initialize Launch Specification
launchSpec = LaunchSpecification(image_id="ami-f173cc91", key_pair="spotinst-oregon", tags=tags, security_group_ids=securityGroupIds, monitoring=True, iam_role=[iam_role])

# Initialize Availability Zones
az_list = [AvailabilityZone(name="us-west-2a", subnet_ids=["subnet-5df28914"])]

# Initialize spot and on demand instance types
instance_types = InstanceTypes(ondemand="c3.large", spot=["c3.large", "c4.large"], preferred_spot=["c4.large"])

# Initialize Compute
compute = Compute(product="Linux/UNIX", instance_types=instance_types, availability_zones=az_list, launch_specification=launchSpec)

# Initialize Elastigroup
group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute)

# Create elastigroup and retrieve group id
group = client.create_elastigroup(group)
group_id = group['id']
print('group id: %s' % group_id)

# Update Elastigroup
capacity_update = Capacity(minimum=0, maximum=15, target=0)
strategy_update = Strategy(risk=None, on_demand_count=2)
group_update = Elastigroup(capacity=capacity_update, strategy=strategy_update)

update_result = client.update_elastigroup(group_update=group_update, group_id=group_id)
print('update result: %s' % update_result)

# Delete Elastigroup
deletion_success = client.delete_elastigroup(group_id=group_id)
print('delete result: %s' % deletion_success)
```

### Elastigroup Additional Configurations
#### Scaling Policies
```python
scaling_policy_up_action = ScalingPolicyAction(type='percentageAdjustment', adjustment=20)
scaling_policy_up_instance_dimension = ScalingPolicyDimension(name='InstanceId')
scaling_policy_up = ScalingPolicy(metric_name='CPUUtilization', statistic='average',
                                  unit='percent', namespace='AWS/EC2', threshold=90,
                                  period=300, evaluation_periods=1, cooldown=300,
                                  operator='gte', action=scaling_policy_up_action,
                                  dimensions=[scaling_policy_up_instance_dimension])

scaling_policy_down_action = ScalingPolicyAction(type='adjustment', adjustment=1)
scaling_policy_down_cluster_dimension = ScalingPolicyDimension(name='Cluster', value='M2M')
scaling_policy_down_env_dimension = ScalingPolicyDimension(name='Environment', value='ia-staging')
scaling_policy_down = ScalingPolicy(metric_name='overhead', statistic='average',
                                    unit='milliseconds', namespace='Monitoring', threshold=0.8,
                                    period=300, evaluation_periods=1, cooldown=300,
                                    operator='lt', action=scaling_policy_down_action,
                                    dimensions=[scaling_policy_down_cluster_dimension,
                                                scaling_policy_down_env_dimension]
                                    )

target_tracking = TargetTrackingPolicy(policy_name='target_policy_1', metric_name='CPUUtilization',
                                       statistic='average', source='cloudWatch', unit='percent', target=50,
                                       namespace='AWS/EC2', cooldown=300)

scaling = Scaling(up=[scaling_policy_up], down=[scaling_policy_down], target=[target_tracking])                                                           
                                                            
group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute, scaling=scaling)
```

#### Scheduling
```python
scheduled_ami_backup = ScheduledTask(frequency='hourly', task_type='backup_ami')
scheduled_roll = ScheduledTask(cron_expression='00 17 * * 3', task_type='roll', batch_size_percentage=30)
scheduled_scale = ScheduledTask(cron_expression='00 22 * * 3', task_type='scale',
                                start_time='2018-05-23T10:55:09Z', scale_target_capacity=0,
                                scale_min_capacity=0,
                                scale_max_capacity=3)

scheduling = Scheduling(tasks=[scheduled_ami_backup, scheduled_roll, scheduled_scale])                                                            
                                                            
group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute, scheduling=scheduling)
```

#### Stateful
```python
availability_zones= AvailabilityZone(name="us-west-2",subnet_ids=["subnet_ids","subnet_ids"])

stateful_instance = StatefulInstance(
  should_keep_private_ip=False , 
  original_instance_id="original_instance_id" , 
  name="Test" , 
  product="Linux/UNIX" , 
  spot_instance_types=["m1.medium", "c3.xlarge", "m3.xlarge"] ,
  region="us-west-2" ,
  availability_zones=[availability_zones])

client.import_stateful_instance(stateful_instance="stateful_instance")

client.get_stateful_instances(group_id="group_id")

client.deallocate_stateful_instance(group_id="group_id", stateful_instance_id="stateful_instance_id")

client.get_stateful_import_status(stateful_migration_id="stateful_migration_id")

client.delete_stateful_import(stateful_migration_id="stateful_migration_id")

client.pause_stateful_instance(group_id="group_id", stateful_instance_id="stateful_instance_id")

client.resume_stateful_instance(group_id="group_id", stateful_instance_id="stateful_instance_id")

client.recycle_stateful_instance(group_id="group_id", stateful_instance_id="stateful_instance_id")
```

### Third Party Integrations
#### ECS
```python
ecs_auto_scale_down = EcsAutoScalerDownConfiguration(evaluation_periods=3)
ecs_auto_scale_attribute = EcsAutoScalerAttributeConfiguration(key='the_key', value='the_value')
ecs_auto_scale_headroom = EcsAutoScalerHeadroomConfiguration(cpu_per_unit=4096, memory_per_unit=4096, num_of_units=30)
ecs_auto_scale = EcsAutoScaleConfiguration(is_enabled=True, is_auto_config=False, cooldown=900, headroom=ecs_auto_scale_headroom, down=ecs_auto_scale_down, attributes=[ecs_auto_scale_attribute])
ecs = EcsConfiguration(cluster_name='test-ecs', auto_scale=ecs_auto_scale)
third_party_integrations = ThirdPartyIntegrations(ecs=ecs)

group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute, third_parties_integration=third_party_integrations)
```

#### EMR
```python
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "PythonSpotinstSDK"))

from spotinst_sdk import SpotinstClient
from spotinst_sdk.spotinst_emr import *

client = SpotinstClient()


################ Scaling ################

action = Action(    
  type="adjustment",
  adjustment=2,
  min_target_capacity=1,
  target=5,
  minimum=0,
  maximum=10)

dimension = Dimension(name="test_dim")

up = Metric(    
  metric_name="metric_name",
  statistic="average",
  unit="percent",
  threshold=100,
  adjustment=2,
  namespace="AWS/ElasticMapReduce",
  period=300,
  evaluation_periods=1,
  cooldown=600,
  dimensions=[dimension],
  operator="gte")

down = Metric(    
  metric_name="metric_name",
  statistic="average",
  unit="percent",
  threshold=100,
  adjustment=2,
  namespace="AWS/ElasticMapReduce",
  period=300,
  evaluation_periods=1,
  cooldown=600,
  dimensions=[dimension],
  operator="gte")

scaling = Scaling(up=[up], down=[down])

################ Copmute ################

c_file = File(bucket="test_bucket", key="test_key")

configurations = Configurations(file=c_file)


volume_specification = VolumeSpecification(volume_type="gp2", size_in_gb=10)

ebs_config = SingleEbsConfig(volume_specification=volume_specification, volumes_per_instance=1)

ebs_configuration = EbsConfiguration(ebs_block_device_configs=[ebs_config], ebs_optimized=True)

capacity = Capacity(target=1, maximum=1, minimum=1)


master_group = MasterGroup(instance_types=["m1.medium", "c3.xlarge", "m3.xlarge"], target=1, life_cycle="SPOT")

core_group = CoreGroup(instance_types=["m1.medium", "c3.xlarge", "m3.xlarge"], target=1, life_cycle="SPOT")

task_group = TaskGroup(instance_types=["m1.medium", "c3.xlarge", "m3.xlarge"], capacity=capacity, life_cycle="SPOT")

instance_groups = InstanceGroups(master_group=master_group, core_group=core_group, task_group=task_group)


s_file = File(bucket="test_bucket", key="test_key")

steps = Steps(file=s_file)


ba_file = File(bucket="test_bucket", key="test_key")

bootstrap_actions = BootstrapActions(file=ba_file)


compute = Compute(ebs_root_volume_size=10, availability_zones=[{"name": "us-west-2a","subnetId": "subnet-79da021e"}], instance_groups=instance_groups)

################ Strategy ################

cloning = Cloning(origin_cluster_id="j-6T5B467690OT", include_steps=False)

provisioning_timeout = ProvisioningTimeout(timeout=600, timeout_action="terminate")

strategy = Strategy(cloning=cloning, provisioning_timeout=provisioning_timeout)

name = "SDK-Test"

description = "This was created with the SDK"

region = "us-west-2"

emr = EMR(name=name, description=description, region=region, strategy=strategy, compute=compute, scaling=scaling)

emr = client.create_emr(emr)
```




#### Kubernetes
```python
kubernetes_auto_scale_down = KubernetesAutoScalerDownConfiguration(evaluation_periods=5)
kubernetes_auto_scale_headroom = KubernetesAutoScalerHeadroomConfiguration(cpu_per_unit=2000, memory_per_unit=4000, num_of_units=2)
kubernetes_auto_scale = KubernetesAutoScalerConfiguration(is_enabled=True, cooldown=300, headroom=kubernetes_auto_scale_headroom, down=kubernetes_auto_scale_down, is_auto_config=False)
kubernetes = KubernetesConfiguration(integration_mode='pod', cluster_identifier='test-k8s', auto_scale=kubernetes_auto_scale)
third_party_integrations = ThirdPartyIntegrations(kubernetes=kubernetes)

group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute, third_parties_integration=third_party_integrations)
```

#### Nomad
```python
nomad_down = NomadAutoScalerDownConfiguration(evaluation_periods=3)
nomad_constraints = NomadAutoScalerConstraintsConfiguration(key='${node.class}', value='value')
nomad_scale_headroom = NomadAutoScalerHeadroomConfiguration(cpu_per_unit=10, memory_per_unit=1000, num_of_units=2)
nomad_auto_scale = NomadAutoScalerConfiguration(is_enabled=True, cooldown=180, headroom=nomad_scale_headroom, constraints=[nomad_constraints], down=nomad_down)
nomad = NomadConfiguration(master_host="https://master.host.com", master_port=443, acl_token='123', auto_scale=nomad_auto_scale)
third_party_integrations = ThirdPartyIntegrations(nomad=nomad)

group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute, third_parties_integration=third_party_integrations)
```

#### DockerSwarm
```python
docker_swarm_down = DockerSwarmAutoScalerDownConfiguration(evaluation_periods=4)
docker_swarm_headroom = DockerSwarmAutoScalerHeadroomConfiguration(cpu_per_unit=1000000000, memory_per_unit=800000000, num_of_units=3)
docker_swarm_auto_scale = DockerSwarmAutoScalerConfiguration(is_enabled=True, cooldown=300, headroom=docker_swarm_headroom, down=docker_swarm_down)
docker_swarm = DockerSwarmConfiguration(master_host='10.10.10.10', master_port=1234, auto_scale=docker_swarm_auto_scale)
third_party_integrations = ThirdPartyIntegrations(docker_swarm=docker_swarm)

group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute, third_parties_integration=third_party_integrations)
```

#### CodeDeploy
```python
code_deploy_deployment_groups = CodeDeployDeploymentGroupsConfiguration(application_name='test-app', deployment_group_name='test-grp')
code_deploy = CodeDeployConfiguration(clean_up_on_failure=False, terminate_instance_on_failure=False, deployment_groups=[code_deploy_deployment_groups])
third_party_integrations = ThirdPartyIntegrations(code_deploy=code_deploy)

group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute, third_parties_integration=third_party_integrations)
```

#### Route53
```python
route53_record_set = Route53RecordSetsConfiguration(use_public_ip=True, name='test-domain.com')
route53_domains = Route53DomainsConfiguration(hosted_zone_id='Z3UFMBCGJMYLUT', record_sets=[route53_record_set])
route53 = Route53Configuration(domains=[route53_domains])
third_party_integrations = ThirdPartyIntegrations(route53=route53)

group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute, third_parties_integration=third_party_integrations)
```

#### ElasticBeanstalk
```python
deployment_strategy = BeanstalkDeploymentStrategy(action='REPLACE_SERVER', should_drain_instances=True)
deployment_preferences = DeploymentPreferences(automatic_roll=True, batch_size_percentage=50, grace_period=600,
                                               strategy=deployment_strategy)
elastic_beanstalk = ElasticBeanstalk(environment_id='123', deployment_preferences=deployment_preferences)
third_party_integrations = ThirdPartyIntegrations(elastic_beanstalk=elastic_beanstalk)

group = Elastigroup(name="TestGroup", description="Created by the Python SDK", capacity=capacity, strategy=strategy, compute=compute, third_parties_integration=third_party_integrations)
```

## Functions
### Getting Started With Functions
```python
from spotinst_sdk import SpotinstClient
from spotinst_sdk.spotinst_functions import *

client = SpotinstClient()

# Initialize application
application = Application("example_application")

# Create application and retrieve application_id
app = client.create_application(application)
app_id = app['id']
print('app id: %s' % app_id)

# Initialize providers
providers = ['aws']

# Initialize locations
locations = ['us-east-1']

# Initialize environment
environment_config = Environment("test-environment", app_id, providers, locations)
environment = client.create_environment(environment_config)
environment_id = environment['id']
print('env id: %s' % environment_id)

# Initialize function
function_config = Function("ping", environment_id, '/development/my_project/ping', 'main', 'nodejs83', 128, 30)

# Create function and retrieve invocation URL
function = client.create_function(function_config)
function_url = function['url']
print('function url: %s' % function_url)
```