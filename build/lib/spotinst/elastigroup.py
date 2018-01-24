import json

none = "d3043820717d74d9a17694c176d39733"


# region Elastigroup
class Elastigroup:
    def __init__(self, name=none, description=none, capacity=none, strategy=none,
                 compute=none, scaling=none,
                 scheduling=none, multai=none,
                 thirdPartiesIntegration=none):
        self.name = name
        self.description = description
        self.capacity = capacity
        self.strategy = strategy
        self.scaling = scaling
        self.scheduling = scheduling
        self.multai = multai
        self.thirdPartiesIntegration = thirdPartiesIntegration
        self.compute = compute


# endregion

# region Strategy
class Strategy:
    def __init__(self, availabilityVsCost=none, risk=none, utilizeReservedInstances=none,
                 fallbackToOd=none,
                 onDemandCount=none, drainingTimeout=none,
                 spinUpTime=none, lifetimePeriod=none, signalsList=none,
                 scalingStrategy=none, persistence=none):
        self.risk = risk
        self.utilizeReservedInstances = utilizeReservedInstances
        self.fallbackToOd = fallbackToOd
        self.onDemandCount = onDemandCount
        self.availabilityVsCost = availabilityVsCost
        self.drainingTimeout = drainingTimeout
        self.spinUpTime = spinUpTime
        self.lifetimePeriod = lifetimePeriod
        self.spinUpTime = spinUpTime
        self.signals = signalsList
        self.scalingStrategy = scalingStrategy
        self.persistence = persistence


class Signal:
    def __init__(self, name=none, timeout=none):
        self.name = name
        self.timeout = timeout


class ScalingStrategy:
    def __init__(self, terminateAtEndOfBillingHour):
        self.terminateAtEndOfBillingHour = terminateAtEndOfBillingHour


class Persistence:
    def __init__(self, shouldPersistBlockDevices=none, shouldPersistRootDevice=none,
                 shouldPersistPrivateIp=none):
        self.shouldPersistBlockDevices = shouldPersistBlockDevices
        self.shouldPersistRootDevice = shouldPersistRootDevice
        self.shouldPersistPrivateIp = shouldPersistPrivateIp


# endregion

# region Capacity
class Capacity:
    def __init__(self, minimum=none, maximum=none, target=none, unit=none):
        self.minimum = minimum
        self.maximum = maximum
        self.target = target
        self.unit = unit


# endregion

# region Scaling
class Scaling:
    def __init__(self, up=none, down=none):
        self.up = up
        self.down = down


class ScalingPolicyDimension:
    def __init__(self, name=none, value=none):
        self.name = name
        self.value = value


class ScalingPolicyAction:
    def __init__(self, type=none, adjustment=none, minTargetCapacity=none,
                 maxTargetCapacity=none, target=none,
                 minimum=none,
                 maximum=none):
        self.type = type
        self.adjustment = adjustment
        self.minTargetCapacity = minTargetCapacity
        self.maxTargetCapacity = maxTargetCapacity
        self.target = target
        self.minimum = minimum
        self.maximum = maximum


class ScalingPolicy:
    def __init__(self, namespace=none, metricName=none, statistic=none,
                 evaluationPeriods=none, period=none,
                 threshold=none,
                 cooldown=none, action=none, unit=none, operator=none,
                 dimensions=none, policyName=none):
        self.policyName = policyName
        self.namespace = namespace
        self.metricName = metricName
        self.dimensions = dimensions
        self.statistic = statistic
        self.evaluationPeriods = evaluationPeriods
        self.period = period
        self.threshold = threshold
        self.cooldown = cooldown
        self.action = action
        self.unit = unit
        self.operator = operator


# endregion

# region Scheduling
class Scheduling:
    def __init__(self, tasks=none):
        self.tasks = tasks


class ScheduledTask:
    def __init__(self, taskType=none, scaleTargetCapacity=none,
                 scaleMinCapacity=none,
                 scaleMaxCapacity=none, batchSizePercentage=none, gracePeriod=none,
                 adjustment=none,
                 adjustmentPercentage=none, isEnabled=none,
                 frequency=none, cronExpression=none, ):
        self.isEnabled = isEnabled
        self.frequency = frequency
        self.cronExpression = cronExpression
        self.taskType = taskType
        self.scaleTargetCapacity = scaleTargetCapacity
        self.scaleMinCapacity = scaleMinCapacity
        self.scaleMaxCapacity = scaleMaxCapacity
        self.batchSizePercentage = batchSizePercentage
        self.gracePeriod = gracePeriod
        self.adjustment = adjustment
        self.adjustmentPercentage = adjustmentPercentage


# endregion

# region Multai
class Multai:
    def __init__(self, token=none, balancers=none):
        self.token = token
        self.balancers = balancers


class MultaiLoadBalancer:
    def __init__(self, projectId=none, balancerId=none, targetSetId=none, azAwareness=none,
                 autoWeight=none):
        self.projectId = projectId
        self.balancerId = balancerId
        self.targetSetId = targetSetId
        self.azAwareness = azAwareness
        self.autoWeight = autoWeight


# endregion

# region ThirdPartyIntegrations
class Rancher:
    def __init__(self, accessKey=none, secretKey=none, masterHost=none):
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.masterHost = masterHost


class Mesosphere:
    def __init__(self, apiServer=none):
        self.apiServer = apiServer


class ElasticBeanstalk:
    def __init__(self, environmentId=none, deploymentPreferences=none):
        self.environmentId = environmentId
        self.deploymentPreferences = deploymentPreferences


class DeploymentPreferences:
    def __init__(self, automaticRoll=none, batchSizePercentage=none, gracePeriod=none,
                 strategy=none):
        self.automaticRoll = automaticRoll
        self.batchSizePercentage = batchSizePercentage
        self.gracePeriod = gracePeriod
        self.strategy = strategy


class BeanstalkDeploymentStrategy:
    def __init__(self, action=none, shouldDrainInstances=none):
        self.action = action
        self.shouldDrainInstances = shouldDrainInstances


class EcsConfiguration:
    def __init__(self, clusterName=none):
        self.clusterName = clusterName


class KubernetesConfiguration:
    def __init__(self, apiServer=none, token=none):
        self.apiServer = apiServer
        self.token = token


class RightScaleConfiguration:
    def __init__(self, accountId=none, refreshToken=none):
        self.accountId = accountId
        self.refreshToken = refreshToken


class OpsWorksConfiguration:
    def __init__(self, layerId=none):
        self.layerId = layerId


class ChefConfiguration:
    def __init__(self, chefServer=none, organization=none, user=none, pemKey=none,
                 chefVersion=none):
        self.chefServer = chefServer
        self.organization = organization
        self.user = user
        self.pemKey = pemKey
        self.chefVersion = chefVersion


class ThirdPartyIntegrations:
    def __init__(self, rancher=none, mesosphere=none, elasticBeanstalk=none, ecs=none,
                 kubernetes=none, rightScale=none,
                 opsWorks=none, chef=none):
        self.rancher = rancher
        self.mesosphere = mesosphere
        self.elasticBeanstalk = elasticBeanstalk
        self.ecs = ecs
        self.kubernetes = kubernetes
        self.rightScale = rightScale
        self.opsWorks = opsWorks
        self.chef = chef


# endregion

# region Compute
class Compute:
    def __init__(self, launchSpecification=none, instanceTypes=none, product=none,
                 availabilityZonesList=none,
                 elasticIpsStringList=none,
                 ebsVolumesList=none):
        self.elasticIps = elasticIpsStringList
        self.instanceTypes = instanceTypes
        self.availabilityZones = availabilityZonesList
        self.product = product
        self.ebsVolumePool = ebsVolumesList
        self.launchSpecification = launchSpecification


class AvailabilityZone:
    def __init__(self, name=none, subnetId=none, subnetIds=none, placementGroupName=none):
        self.name = name
        self.subnetId = subnetId
        self.subnetIds = subnetIds
        self.placementGroupName = placementGroupName


class InstanceTypes:
    def __init__(self, ondemand=none, spotTypesList=none, instanceTypeWeightsList=none):
        self.ondemand = ondemand
        self.spot = spotTypesList
        self.weights = instanceTypeWeightsList


class Weight:
    def __init__(self, instanceType=none, weightedCapacity=none):
        self.instanceType = instanceType
        self.weightedCapacity = weightedCapacity


class EbsVolume:
    def __init__(self, deviceName=none, volumeIds=none):
        self.deviceName = deviceName
        self.volumeIds = volumeIds


class LaunchSpecification:
    def __init__(self, securityGroupIdsList=none, imageId=none, monitoring=none,
                 healthCheckType=none,
                 loadBalancersConfig=none,
                 healthCheckGracePeriod=none, healthCheckUnhealthyDurationBeforeReplacement=none,
                 ebsOptimized=none, tenancy=none, iamRole=none, keyPair=none,
                 userData=none, shutdownScript=none,
                 blockDeviceMappingsList=none,
                 networkInterfacesList=none, tagsList=none):
        self.loadBalancersConfig = loadBalancersConfig
        self.healthCheckType = healthCheckType
        self.healthCheckGracePeriod = healthCheckGracePeriod
        self.healthCheckUnhealthyDurationBeforeReplacement = healthCheckUnhealthyDurationBeforeReplacement
        self.securityGroupIds = securityGroupIdsList
        self.monitoring = monitoring
        self.ebsOptimized = ebsOptimized
        self.imageId = imageId
        self.tenancy = tenancy
        self.iamRole = iamRole
        self.keyPair = keyPair
        self.userData = userData
        self.shutdownScript = shutdownScript
        self.blockDeviceMappings = blockDeviceMappingsList
        self.networkInterfaces = networkInterfacesList
        self.tags = tagsList


class LoadBalancersConfig:
    def __init__(self, loadBalancersList=none):
        self.loadBalancers = loadBalancersList


class LoadBalancer:
    def __init__(self, type=none, arn=none, name=none):
        self.name = name
        self.arn = arn
        self.type = type


class IAmRole:
    def __init__(self, name=none, arn=none):
        self.name = name
        self.arn = arn


class BlockDeviceMapping:
    def __init__(self, deviceName=none, ebs=none, noDevice=none, virtualName=none):
        self.deviceName = deviceName
        self.ebs = ebs
        self.noDevice = noDevice
        self.virtualName = virtualName


class EBS:
    def __init__(self, deleteOnTermination=none, encrypted=none, iops=none, snapshotId=none,
                 volumeSize=none,
                 volumeType=none):
        self.deleteOnTermination = deleteOnTermination
        self.encrypted = encrypted
        self.iops = iops
        self.snapshotId = snapshotId
        self.volumeSize = volumeSize
        self.volumeType = volumeType


class Tag:
    def __init__(self, tagKey=none, tagValue=none):
        self.tagKey = tagKey
        self.tagValue = tagValue


class NetworkInterface:
    def __init__(self, deleteOnTermination=none, deviceIndex=none, description=none,
                 secondaryPrivateIpAddressCount=none,
                 associatePublicIpAddress=none, groupsList=none, networkInterfaceId=none,
                 privateIpAddress=none,
                 privateIpAddressObjList=none, subnetId=none,
                 associateIpv6Address=none):
        self.description = description
        self.deviceIndex = deviceIndex
        self.secondaryPrivateIpAddressCount = secondaryPrivateIpAddressCount
        self.associatePublicIpAddress = associatePublicIpAddress
        self.deleteOnTermination = deleteOnTermination
        self.groups = groupsList
        self.networkInterfaceId = networkInterfaceId
        self.privateIpAddress = privateIpAddress
        self.privateIpAddresses = privateIpAddressObjList
        self.subnetId = subnetId
        self.associateIpv6Address = associateIpv6Address


class PrivateIpAddress:
    def __init__(self, privateIpAddress=none, primary=none):
        self.privateIpAddress = privateIpAddress
        self.primary = primary


# endregion

class ElastigroupCreationRequest:
    def __init__(self, elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupUpdateRequest:
    def __init__(self, elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
