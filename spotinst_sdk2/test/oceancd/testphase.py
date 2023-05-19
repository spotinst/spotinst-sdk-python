from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.ocean_cd import *

session = SpotinstSession(auth_token='30b3dd9d0d62ebf0c0b702027f0ce2d1a2ddfb96347f6993e0f079c1cc904034',
                          base_url='https://api.spotinst.io')
client = session.client("oceancd", log_level="debug")
# Create elastigroup and retrieve group id
# response = client.ocean_cd_describe_rollout_phase(rollout_id='rol-d80f2865def6')
# print(response)
response = client.ocean_cd_describe_workloads_revision(workload_id='anurag-experiment-deployment', namespace='default',
                                                       cluster_id='anurag-cluster-experiment', kind='SpotDeployment')
print(response)
