import os
import unittest
import json
from mock import patch

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.azure_v3 import *


class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class AzureV3InitTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("elastigroup_azure_v3")

        self.mock_ok_res = self.load_json('../../test_lib/output/res_ok.json')

        self.mock_api_call = SimpleNamespace(**self.load_json('../../test_lib/api_res.json'))

    @staticmethod
    def load_json(path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
            return json.load(group_json)


# Elastigroup Tests
class AzureV3InitTestElastigroup(AzureV3InitTestCase):

    @patch('requests.post')
    def testCreateElastigroup(self, mock):
        mock_group_response = self.load_json('../../test_lib/output/elastigroup/group_res.json')
        mock_group_json = self.load_json('../../test_lib/input/elastigroup/azure_v3_group.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_response)

        mock.return_value = self.mock_api_call

        response = self.client.create_elastigroup(group=mock_group_json)

        self.assertEqual(len(response), len(mock_group_response["response"]["items"][0]))

    @patch('requests.put')
    def testUpdateElastigroup(self, mock):
        mock_group_response = self.load_json('../../test_lib/output/elastigroup/group_res.json')
        mock_group_json = self.load_json('../../test_lib/input/elastigroup/azure_v3_group.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_response)

        mock.return_value = self.mock_api_call

        response = self.client.update_elastigroup(group_update=mock_group_json, group_id="sig-123456")

        self.assertEqual(len(response), len(mock_group_response["response"]["items"][0]))

    @patch('requests.delete')
    def testDeleteElastigroup(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.delete_elastigroup(group_id="sig-12345")

        self.assertEqual(response, True)

    @patch('requests.get')
    def testGetElastigroup(self, mock):
        mock_get_group_res = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_elastigroup(group_id="sig-123456")

        self.assertEqual(len(response), len(mock_get_group_res["response"]["items"][0]))

    @patch('requests.get')
    def testGetElastigroups(self, mock):
        mock_get_group_res = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_elastigroups()

        self.assertEqual(len(response), len(mock_get_group_res["response"]["items"]))

    @patch('requests.put')
    def testScaleGroupUp(self, mock):
        mock_group_scale_response = self.load_json('../../test_lib/output/elastigroup/group_scale_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_scale_response)

        mock.return_value = self.mock_api_call

        response = self.client.scale_elastigroup_up(group_id="sig-123456", adjustment=1)

        self.assertEqual(len(response), len(mock_group_scale_response["response"]["items"]))

    @patch('requests.put')
    def testScaleGroupDown(self, mock):
        mock_group_scale_response = self.load_json('../../test_lib/output/elastigroup/group_scale_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_scale_response)

        mock.return_value = self.mock_api_call

        response = self.client.scale_elastigroup_down(group_id="sig-123456", adjustment=1)

        self.assertEqual(len(response), len(mock_group_scale_response["response"]["items"]))

    @patch('requests.put')
    def testUpdateElastigroupCapacity(self, mock):
        mock_group_scale_response = self.load_json('../../test_lib/output/elastigroup/group_scale_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_scale_response)

        mock.return_value = self.mock_api_call

        response = self.client.update_elastigroup_capacity(group_id="sig-123456", capacity=Capacity(minimum=2,
                                                                                                    maximum=10,
                                                                                                    target=8))

        self.assertEqual(len(response), len(mock_group_scale_response["response"]["items"]))

    @patch('requests.put')
    def testDetachElastigroupInstances(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.detach_elastigroup_vms(group_id="sig-123456",
                                                      detach_configuration=DetachConfiguration(
                                                          vms_to_detach="test",
                                                          should_terminate_vms="test",
                                                          draining_timeout="test",
                                                          should_decrement_target_capacity="test"))

        self.assertEqual(response, self.mock_ok_res['response']['status'])

    @patch('requests.post')
    def testProtectVirtualMachine(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.protect_virtual_machine(group_id="sig-123456", vm_name="vm_name")

        self.assertEqual(response, self.mock_ok_res['response']['status'])

    @patch('requests.delete')
    def testUnprotectVirtualMachine(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.unprotect_virtual_machine(group_id="sig-12345", vm_name="vm_name")

        self.assertEqual(response, True)

    @patch('requests.get')
    def testGetElastigroupStatus(self, mock):
        mock_get_group_res = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_elastigroup_status(group_id="sig-12345")

        self.assertEqual(len(response), len(mock_get_group_res["response"]["items"]))

    @patch('requests.get')
    def testGetVmHealthiness(self, mock):
        mock_instance_healthiness_res = self.load_json(
            "../../test_lib/output/elastigroup/instance_healthiness_res.json")

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_instance_healthiness_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_vm_healthiness(group_id="sig-12345")

        self.assertEqual(len(response), len(mock_instance_healthiness_res["response"]["items"]))

    @patch('requests.put')
    def testSuspendProcess(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.suspend_elastigroup(group_id="sig-12345", processes=Processes(
                                                          name="test"))

        self.assertEqual(response, self.mock_ok_res['response']['status'])

    @patch('requests.put')
    def testResumeProcess(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.resume_elastigroup(group_id="sig-12345", processes=Processes(
            name="test"))

        self.assertEqual(response, self.mock_ok_res['response']['status'])

    @patch('requests.put')
    def testStartDeployment(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.start_deployment(group_id="sig-12345", deployment=DeploymentConfiguration(
            batch_min_healthy_percentage="test",
            batch_size_percentage="test",
            draining_timeout="test",
            grace_period="test",
            health_check_types="test"))

        self.assertEqual(response, self.mock_ok_res['response']['status'])

    @patch('requests.get')
    def testGetAllDeployments(self, mock):
        mock_get_group_res = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_all_deployments(group_id="sig-123456", limit="test", sort="test")

        self.assertEqual(len(response), len(mock_get_group_res["response"]["items"]))

    @patch('requests.get')
    def testGetDeployment(self, mock):
        mock_get_group_res = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_deployment(group_id="sig-123456", deployment_id="test")

        self.assertEqual(len(response), len(mock_get_group_res["response"]["items"]))

    @patch('requests.get')
    def testGetDeploymentStatus(self, mock):
        mock_get_group_res = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_deployment_status(group_id="sig-123456", deployment_id="test")

        self.assertEqual(len(response), len(mock_get_group_res["response"]["items"]))

    @patch('requests.get')
    def testImportFromScaleSet(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.import_from_scale_set(resource_group_name="test", scale_set_name="test")

        self.assertEqual(response, self.mock_ok_res['response']['status'])

    @patch('requests.get')
    def testImportFromVM(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.import_from_virtual_machine(resource_group_name="test", virtual_machine_name="test")

        self.assertEqual(response, self.mock_ok_res['response']['status'])

    @patch('requests.get')
    def testImportFromLoadBalancer(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.import_from_load_balancer(resource_group_name="test", load_balancer_name="test",
                                                         backend_pool_name="test")

        self.assertEqual(response, self.mock_ok_res['response']['status'])

    @patch('requests.get')
    def testImportFromApplicationGateway(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.import_from_application_gateway(resource_group_name="test",
                                                               application_gateway_name="test",
                                                               backend_pool_name="test")

        self.assertEqual(response, self.mock_ok_res['response']['status'])

    @patch('requests.post')
    def testCreateVMSignal(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.create_vm_signal(vm_name="i-123456", signal_type="TEST")

        self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

    @patch('requests.get')
    def testGetElastilog(self, mock):
        mock_get_group_res = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_azure_elastilog(group_id="group_id", from_date="from_date", to_date="to_date",
                                             severity="severity", resource_id="resource_id", limit="limit")

        self.assertEqual(len(response), len(mock_get_group_res["response"]["items"]))
