from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.ocean.aws import *


#Todo Baruch delete this add document as readMe
def main():
    session = SpotinstSession(auth_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzcG90aW5zdCIsImV4cCI6MTg5ODQyNDgyNSwiaWF0IjoxNTgzMDY0ODI1LCJ1aWQiOi0xLCJyb2xlIjoyLCJvaWQiOiI2MDYwNzk4NzUyMzEifQ.4JC6xdhUfA5H0MR8WcNEDEPvJTeYZ1XcbVB5E8ovnqA', account_id='act-2a68b54d')
    client = session.client("ocean_aws")

    all_match = AllMatch([{"type": "label", "key": "k8s-app", "operator": "notEquals", "value": "dns-controller"}])
    any_match = [all_match]

    # aggregated_cluster_costs = AggregatedClusterCosts(start_time="1655812800000", end_time="1655985600000", group_by="resource.label.k8s-addon",
    #                                                       aggregated_filter=Filter("resource", Conditions(any_match)))
    aggregated_cluster_costs = AggregatedClusterCosts(start_time="1657411200000", end_time="1658052000000")

    aggregated_cluster_costs_response = client.get_aggregated_cluster_costs(ocean_id="o-56d4124b", aggregated_cluster_costs_request=aggregated_cluster_costs)
    print(aggregated_cluster_costs_response)


if __name__ == '__main__':
    main()

