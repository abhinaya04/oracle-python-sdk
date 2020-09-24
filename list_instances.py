import oci
import sys

delegation_token = open('/etc/oci/delegation_token', 'r').read()
signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(delegation_token=delegation_token)
compute_client = oci.core.ComputeClient({},signer=signer)

def list_oce_instances(id):
	response = compute_client.list_instances(compartment_id=id)
	for each_instance in response.data:
		print(each_instance.id,each_instance.display_name)

def launch_instance(id):
	response = compute_client.launch_instance(oci.core.models.LaunchInstanceDetails(subnet_id='ocid1.subnet.oc1.ap-mumbai-1.aaaaaaaajx24qmiugri3ndtamoki3tmdhwysopssh4qe2yvgeo34yzif7ecq',shape='VM.Standard.E2.1.Micro',availability_domain='KapI:AP-MUMBAI-1-AD-1',compartment_id=id))


if __name__ == "__main__":
	if len(sys.argv) != 2:
		raise RuntimeError('Invalid number of arguments provided to the script')
    	compartment_id = sys.argv[1]
	#launch_instance(compartment_id)
	shape_resp=compute_client.list_shapes(compartment_id=compartment_id)
	print(shape_resp.data)
    	list_oce_instances(compartment_id)

