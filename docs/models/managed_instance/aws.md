<h1 id="spotinst_sdk2.models.managed_instance.aws">spotinst_sdk2.models.managed_instance.aws</h1>


<h2 id="spotinst_sdk2.models.managed_instance.aws.Persistence">Persistence</h2>

```python
Persistence(
  self,
  persist_root_device: bool = 'd3043820717d74d9a17694c176d39733',
  persist_block_devices: bool = 'd3043820717d74d9a17694c176d39733',
  block_devices_mode: str = 'd3043820717d74d9a17694c176d39733',
  persist_private_ip: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __persist_root_device__: bool
- __persist_block_devices__: bool
- __block_devices_mode__: str
- __persist_private_ip__: bool

<h2 id="spotinst_sdk2.models.managed_instance.aws.HealthCheck">HealthCheck</h2>

```python
HealthCheck(
  self,
  type: str = 'd3043820717d74d9a17694c176d39733',
  auto_healing: bool = 'd3043820717d74d9a17694c176d39733',
  grace_period: int = 'd3043820717d74d9a17694c176d39733',
  unhealthy_duration: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: bool
- __auto_healing__: bool
- __grace_period__: int
- __unhealthy_duration__: int

<h2 id="spotinst_sdk2.models.managed_instance.aws.Task">Task</h2>

```python
Task(self,
     task_type: str = 'd3043820717d74d9a17694c176d39733',
     start_time: str = 'd3043820717d74d9a17694c176d39733',
     cron_expression: str = 'd3043820717d74d9a17694c176d39733',
     is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
     frequency: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __task_type__: str
- __start_time__: str
- __cron_expression__: str
- __is_enabled__: bool
- __frequency__: str

<h2 id="spotinst_sdk2.models.managed_instance.aws.Scheduling">Scheduling</h2>

```python
Scheduling(
    self,
    tasks:
    typing.List[spotinst_sdk2.models.managed_instance.aws.Task] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __tasks__: list[Task]

<h2 id="spotinst_sdk2.models.managed_instance.aws.RevertToSpot">RevertToSpot</h2>

```python
RevertToSpot(self, perform_at: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __perform_at__: str

<h2 id="spotinst_sdk2.models.managed_instance.aws.Strategy">Strategy</h2>

```python
Strategy(
  self,
  life_cycle: str = 'd3043820717d74d9a17694c176d39733',
  orientation: str = 'd3043820717d74d9a17694c176d39733',
  draining_timeout: int = 'd3043820717d74d9a17694c176d39733',
  fallback_to_od: bool = 'd3043820717d74d9a17694c176d39733',
  utilize_reserved_instances: bool = 'd3043820717d74d9a17694c176d39733',
  utilize_commitments: bool = 'd3043820717d74d9a17694c176d39733',
  optimization_windows:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  revert_to_spot: RevertToSpot = 'd3043820717d74d9a17694c176d39733',
  minimum_instance_lifetime: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __life_cycle__: str
- __orientation__: str
- __draining_timeout__: int
- __fallback_to_od__: bool
- __utilize_reserved_instances__: bool
- __utilize_commitments__: bool
- __optimization_windows__: list[str]
- __revert_to_spot__: RevertToSpot
- __minimum_instance_lifetime__: int

<h2 id="spotinst_sdk2.models.managed_instance.aws.EBS">EBS</h2>

```python
EBS(self,
    delete_on_termination: bool = 'd3043820717d74d9a17694c176d39733',
    encrypted: bool = 'd3043820717d74d9a17694c176d39733',
    iops: int = 'd3043820717d74d9a17694c176d39733',
    throughput: float = 'd3043820717d74d9a17694c176d39733',
    kms_key_id: str = 'd3043820717d74d9a17694c176d39733',
    snapshot_id: str = 'd3043820717d74d9a17694c176d39733',
    volume_size: int = 'd3043820717d74d9a17694c176d39733',
    volume_type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __delete_on_termination__: bool
- __encrypted__: bool
- __iops__: int
- __throughput__: float
- __volume_size__: int
- __volume_type__: str
- __kms_key_id__: str
- __snapshot_id__: str

<h2 id="spotinst_sdk2.models.managed_instance.aws.BlockDeviceMapping">BlockDeviceMapping</h2>

```python
BlockDeviceMapping(
  self,
  device_name: str = 'd3043820717d74d9a17694c176d39733',
  ebs: EBS = 'd3043820717d74d9a17694c176d39733',
  no_device: str = 'd3043820717d74d9a17694c176d39733',
  virtual_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __device_name__: str
- __ebs__: EBS
- __no_device__: str
- __virtual_name__: str

<h2 id="spotinst_sdk2.models.managed_instance.aws.CreditSpecification">CreditSpecification</h2>

```python
CreditSpecification(self,
                    cpu_credits: str = 'd3043820717d74d9a17694c176d39733'
                    )
```

__Arguments__

- __cpu_credits__: str

<h2 id="spotinst_sdk2.models.managed_instance.aws.IamRole">IamRole</h2>

```python
IamRole(self,
        name: str = 'd3043820717d74d9a17694c176d39733',
        arn: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __arn__: str

<h2 id="spotinst_sdk2.models.managed_instance.aws.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(
  self,
  preferred_type: str = 'd3043820717d74d9a17694c176d39733',
  types: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __preferred_type__: str
- __types__: list[str]

<h2 id="spotinst_sdk2.models.managed_instance.aws.NetworkInterface">NetworkInterface</h2>

```python
NetworkInterface(
  self,
  device_index: int = 'd3043820717d74d9a17694c176d39733',
  associate_public_ip_address: bool = 'd3043820717d74d9a17694c176d39733',
  associate_ipv6_address: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __device_index__: int
- __associate_public_ip_address__: bool
- __associate_ipv6_address__: bool

<h2 id="spotinst_sdk2.models.managed_instance.aws.TagSpecification">TagSpecification</h2>

```python
TagSpecification(self,
                 should_tag: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __should_tag__: bool

<h2 id="spotinst_sdk2.models.managed_instance.aws.ResourceTagSpecification">ResourceTagSpecification</h2>

```python
ResourceTagSpecification(
  self,
  volumes: TagSpecification = 'd3043820717d74d9a17694c176d39733',
  snapshots: TagSpecification = 'd3043820717d74d9a17694c176d39733',
  enis: TagSpecification = 'd3043820717d74d9a17694c176d39733',
  amis: TagSpecification = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __volumes__: TagSpecification
- __snapshots__: TagSpecification
- __enis__: TagSpecification
- __amis__: TagSpecification

<h2 id="spotinst_sdk2.models.managed_instance.aws.Tag">Tag</h2>

```python
Tag(self,
    tag_key: str = 'd3043820717d74d9a17694c176d39733',
    tag_value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.managed_instance.aws.LaunchSpecification">LaunchSpecification</h2>

```python
LaunchSpecification(
    self,
    instance_types: InstanceTypes = 'd3043820717d74d9a17694c176d39733',
    ebs_optimized: bool = 'd3043820717d74d9a17694c176d39733',
    monitoring: bool = 'd3043820717d74d9a17694c176d39733',
    tenancy: str = 'd3043820717d74d9a17694c176d39733',
    iam_role: IamRole = 'd3043820717d74d9a17694c176d39733',
    security_group_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    image_id: str = 'd3043820717d74d9a17694c176d39733',
    key_pair: str = 'd3043820717d74d9a17694c176d39733',
    tags:
    typing.List[spotinst_sdk2.models.managed_instance.aws.Tag] = 'd3043820717d74d9a17694c176d39733',
    resource_tag_specification:
    ResourceTagSpecification = 'd3043820717d74d9a17694c176d39733',
    user_data: str = 'd3043820717d74d9a17694c176d39733',
    shutdown_script: str = 'd3043820717d74d9a17694c176d39733',
    credit_specification:
    CreditSpecification = 'd3043820717d74d9a17694c176d39733',
    network_interfaces:
    typing.List[spotinst_sdk2.models.managed_instance.aws.NetworkInterface] = 'd3043820717d74d9a17694c176d39733',
    block_device_mappings:
    typing.List[spotinst_sdk2.models.managed_instance.aws.BlockDeviceMapping] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __instance_types__: InstanceTypes
- __ebs_optimized__: bool
- __monitoring__: bool
- __tenancy__: str
- __iam_role__: IamRole
- __security_group_ids__: list[str]
- __image_id__: str
- __key_pair__: str
- __tags__: list[Tag]
- __resource_tag_specification__: ResourceTagSpecification
- __user_data__: str
- __shutdown_script__: str
- __credit_specification__: CreditSpecification
- __network_interfaces__: list[NetworkInterface]
- __block_device_mappings__: list[BlockDeviceMapping]

<h2 id="spotinst_sdk2.models.managed_instance.aws.Compute">Compute</h2>

```python
Compute(
    self,
    subnet_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    vpc_id: str = 'd3043820717d74d9a17694c176d39733',
    elastic_ip: str = 'd3043820717d74d9a17694c176d39733',
    private_ip: str = 'd3043820717d74d9a17694c176d39733',
    product: str = 'd3043820717d74d9a17694c176d39733',
    launch_specification:
    LaunchSpecification = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __subnet_ids__: list[str]
- __vpc_id__: str
- __elastic_ip__: str
- __private_ip__: str
- __product__: str
- __launch_specification__: LaunchSpecification

<h2 id="spotinst_sdk2.models.managed_instance.aws.Route53RecordSetConfiguration">Route53RecordSetConfiguration</h2>

```python
Route53RecordSetConfiguration(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  use_public_ip: bool = 'd3043820717d74d9a17694c176d39733',
  use_public_dns: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __use_public_ip__: bool
- __use_public_dns__: bool

<h2 id="spotinst_sdk2.models.managed_instance.aws.Route53DomainConfiguration">Route53DomainConfiguration</h2>

```python
Route53DomainConfiguration(
    self,
    hosted_zone_id: str = 'd3043820717d74d9a17694c176d39733',
    spotinst_account_id: str = 'd3043820717d74d9a17694c176d39733',
    record_set_type: str = 'd3043820717d74d9a17694c176d39733',
    record_sets:
    typing.List[spotinst_sdk2.models.managed_instance.aws.Route53RecordSetConfiguration] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __hosted_zone_id__: str
- __spotinst_account_id__: str
- __record_set_type__: str
- __record_sets__: list[Route53RecordSetConfiguration]

<h2 id="spotinst_sdk2.models.managed_instance.aws.Route53Configuration">Route53Configuration</h2>

```python
Route53Configuration(
    self,
    domains:
    typing.List[spotinst_sdk2.models.managed_instance.aws.Route53DomainConfiguration] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __domains__: list[Route53DomainsConfiguration]

<h2 id="spotinst_sdk2.models.managed_instance.aws.LoadBalancer">LoadBalancer</h2>

```python
LoadBalancer(self,
             name: str = 'd3043820717d74d9a17694c176d39733',
             arn: str = 'd3043820717d74d9a17694c176d39733',
             type: str = 'd3043820717d74d9a17694c176d39733',
             balancer_id: str = 'd3043820717d74d9a17694c176d39733',
             target_set_id: str = 'd3043820717d74d9a17694c176d39733',
             az_awareness: bool = 'd3043820717d74d9a17694c176d39733',
             auto_weight: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __arn__: str
- __type__: str
- __balancer_id__: str
- __target_set_id__: str
- __az_awareness__: bool
- __auto_weight__: bool

<h2 id="spotinst_sdk2.models.managed_instance.aws.LoadBalancersConfiguration">LoadBalancersConfiguration</h2>

```python
LoadBalancersConfiguration(
    self,
    load_balancers:
    typing.List[spotinst_sdk2.models.managed_instance.aws.LoadBalancer] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __load_balancers__: list[LoadBalancer]

<h2 id="spotinst_sdk2.models.managed_instance.aws.IntegrationsConfig">IntegrationsConfig</h2>

```python
IntegrationsConfig(
    self,
    route53: Route53Configuration = 'd3043820717d74d9a17694c176d39733',
    load_balancers_config:
    LoadBalancersConfiguration = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __route53__: Route53Configuration
- __load_balancers_config__: LoadBalancersConfiguration

<h2 id="spotinst_sdk2.models.managed_instance.aws.ManagedInstance">ManagedInstance</h2>

```python
ManagedInstance(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  description: str = 'd3043820717d74d9a17694c176d39733',
  region: str = 'd3043820717d74d9a17694c176d39733',
  strategy: Strategy = 'd3043820717d74d9a17694c176d39733',
  persistence: Persistence = 'd3043820717d74d9a17694c176d39733',
  health_check: HealthCheck = 'd3043820717d74d9a17694c176d39733',
  scheduling: Scheduling = 'd3043820717d74d9a17694c176d39733',
  compute: Compute = 'd3043820717d74d9a17694c176d39733',
  integrations: IntegrationsConfig = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __description__: str
- __region__: str
- __strategy__: Strategy
- __persistence__: Persistence
- __health_check__: HealthCheck
- __scheduling__: Scheduling
- __compute__: Compute
- __integrations__: IntegrationsConfig

