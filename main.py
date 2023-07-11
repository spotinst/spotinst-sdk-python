from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.aws import *
from spotinst_sdk2.models.hpc.aws import *

session = SpotinstSession(auth_token='3526b1fbfb2d375d095c3d4c2b552c2db86f1b4020a99f425d96b70604293f65', account_id='act-7c46c6df')

client = session.client("hpc")

# Strategy
strategy = Strategy(draining_timeout=120)

# Capacity
capacity = Capacity(minimum=0, maximum=10, target=5)

# Instance Types
instance_types = InstanceTypes(ondemand="t2.micro", spot=["t2.micro"])



# Instance Types
instance_types = InstanceTypes(onDemand="t2.micro", spot=["t2.micro"])


# Launch Specification
launch_specification = LaunchSpecification(security_group_ids=["sg-a22000e8"],image_id="ami-0e987721f52d01f47",
                                           monitoring=False,key_pair="automation-kp",
                                           user_data="I2Nsb3VkLWJvb3Rob29rCiMhL2Jpbi9iYXNoCgoKIyBJbml0aWFsIGNvbmZpZ3VyYXRpb25zCmxvZ2ZpbGU9L3RtcC91c2VyX2RhdGEubG9nCmVjaG8gU1RBUlQgYGRhdGUgJyslWS0lbS0lZCAlSDolTTolUydgID4+ICRsb2dmaWxlCnNlZCAtaSAncy9hd3Nob3N0L3Nwb3Rob3N0L2cnIC91c3Ivc2hhcmUvbHNmL2NvbmYvbHNmLmNvbmYKCgojIFNvdXJjZSBMU0YgZW52aW9ybm1lbnQgYXQgdGhlIFZNIGhvc3QKTFNGX1RPUD0vdXNyL3NoYXJlL2xzZgpMU0ZfQ09ORl9GSUxFPSRMU0ZfVE9QL2NvbmYvbHNmLmNvbmYKLiAkTFNGX1RPUC9jb25mL3Byb2ZpbGUubHNmCmVudiA+PiAkbG9nZmlsZQoKCiMgU3VwcG9ydCByY19hY2NvdW50IHJlc291cmNlIHRvIGVuYWJsZSBSQ19BQ0NPVU5UIHBvbGljeQojIEFkZCBhZGRpdGlvbmFsIGxvY2FsIHJlc291cmNlcyBpZiBuZWVkZWQKaWYgWyAtbiAiJHtyY19hY2NvdW50fSIgXTsgdGhlbgpzZWQgLWkgInMvKExTRl9MT0NBTF9SRVNPVVJDRVM9LiopIi8xIFtyZXNvdXJjZW1hcCAke3JjX2FjY291bnR9KnJjX2FjY291bnRdIi8iICRMU0ZfQ09ORl9GSUxFCmVjaG8gInVwZGF0ZSBMU0ZfTE9DQUxfUkVTT1VSQ0VTIGxzZi5jb25mIHN1Y2Nlc3NmdWxseSwgYWRkIFtyZXNvdXJjZW1hcCAke3JjX2FjY291bnR9KnJjX2FjY291bnRdIiA+PiAkbG9nZmlsZQpmaQoKCiMgSW5jbHVkZSBvcmlnaW4gaW5mb3JtYXRpb24gZm9yIGZhdWx0IHRvbGVyYW5jZQppbnN0YW5jZV9pZD0kKGN1cmwgaHR0cDovLzE2OS4yNTQuMTY5LjI1NC9sYXRlc3QvbWV0YS1kYXRhL2luc3RhbmNlLWlkKQppZiBbIC1uICIkaW5zdGFuY2VfaWQiIF07IHRoZW4Kc2VkIC1pICJzLyhMU0ZfTE9DQUxfUkVTT1VSQ0VTPS4qKSIvMSBbcmVzb3VyY2VtYXAgJGluc3RhbmNlX2lkKmluc3RhbmNlSURdIi8iICRMU0ZfQ09ORl9GSUxFCmZpCmlmIFsgLW4gIiR0ZW1wbGF0ZV9pZCIgXTsgdGhlbgpzZWQgLWkgInMvKExTRl9MT0NBTF9SRVNPVVJDRVM9LiopIi8xIFtyZXNvdXJjZW1hcCAkdGVtcGxhdGVfaWQqdGVtcGxhdGVJRF0iLyIgJExTRl9DT05GX0ZJTEUKZmkKaWYgWyAtbiAiJGNsdXN0ZXJuYW1lIiBdOyB0aGVuCnNlZCAtaSAicy8oTFNGX0xPQ0FMX1JFU09VUkNFUz0uKikiLzEgW3Jlc291cmNlbWFwICRjbHVzdGVybmFtZSpjbHVzdGVyTmFtZV0iLyIgJExTRl9DT05GX0ZJTEUKZmkKaWYgWyAtbiAiJHByb3ZpZGVyTmFtZSIgXTsgdGhlbgpzZWQgLWkgInMvKExTRl9MT0NBTF9SRVNPVVJDRVM9LiopIi8xIFtyZXNvdXJjZW1hcCAkcHJvdmlkZXJOYW1lKnByb3ZpZGVyTmFtZV0iLyIgJExTRl9DT05GX0ZJTEUKZmkKaWYgWyAtbiAiJHByb3ZpZGVyTmFtZSIgXTsgdGhlbgpzZWQgLWkgInMvKExTRl9MT0NBTF9SRVNPVVJDRVM9LiopIi8xIFtyZXNvdXJjZW1hcCAkZ3JvdXBUeXBlKmdyb3VwVHlwZV0iLyIgJExTRl9DT05GX0ZJTEUKZmkKCgojIEFkZCBob3N0bmFtZSB0byBob3N0cwpwcml2YXRlX2lwPSQoY3VybCBodHRwOi8vMTY5LjI1NC4xNjkuMjU0L2xhdGVzdC9tZXRhLWRhdGEvbG9jYWwtaXB2NCkKc2hvcnRfaG9zdG5hbWU9JChob3N0bmFtZSAtcykKaG9zdG5hbWU9JChob3N0bmFtZSkKZWNobyAiJHByaXZhdGVfaXAgJHNob3J0X2hvc3RuYW1lICRob3N0bmFtZSIgPj4gL2V0Yy9ob3N0cwoKCiMgUnVuIGxzcmVnaG9zdCBjb21tYW5kIHRvIHJlZ2lzdGVyIHRoZSBob3N0IHRvIExTRiBtYXN0ZXIgaWYgbm8gRE5TIHVwZGF0ZQpMU0ZfRU5WRElSPS91c3Ivc2hhcmUvbHNmL2NvbmYKTFNGX1NFUlZFUkRJUj0vdXNyL3NoYXJlL2xzZi8xMC4xL2xpbnV4Mi42LWdsaWJjMi4zLXg4Nl82NC9ldGMKZWNobyAiaXAtMTcyLTMxLTI3LTU5IiA+PiAkTFNGX0VOVkRJUi9ob3N0cmVnc2V0dXAKbHNyZWdob3N0IC1zICRMU0ZfRU5WRElSL2hvc3RyZWdzZXR1cAoKCiMgU3RhcnQgTFNGIERhZW1vbnMKJExTRl9TRVJWRVJESVIvbHNmX2RhZW1vbnMgc3RhcnQKCgplY2hvIEVORCBBVCBgZGF0ZSAnKyVZLSVtLSVkICVIOiVNOiVTJ2AgPj4gJGxvZ2ZpbGU=")

#Compute
compute = Compute(launch_specification=launch_specification,
                  instance_types=instance_types,product="Linux/UNIX",
                  subnet_ids=["subnet-4333093a"])


# HPCCluster
hpc_cluster = HPC(name='Aditya_HPC_Cluster', region='us-west-2',
                    capacity=capacity, strategy=strategy, compute=compute)

hpc_cluster = client.create_hpc_cluster(hpc_cluster)
hpc_cluster_id = hpc_cluster['id']
print('hpc cluster id: %s' % hpc_cluster_id)
x = client.delete_hpc_cluster(hpc_cluster_id)
print('hpc cluster id: %s' % hpc_cluster_id + " is deleted")
y = client.get_all_hpc_clusters()
print(y)
z = client.get_hpc_cluster("shpc-d1155582")
print(z)
