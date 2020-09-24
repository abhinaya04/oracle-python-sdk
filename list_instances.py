#!/usr/bin/env python
import oci
delegation_token = open('/etc/oci/delegation_token', 'r').read()
signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(delegation_token=delegation_token)
compute_client = oci.core.ComputeClient({},signer=signer)
response = compute_client.list_instances(compartment_id='ocid1.tenancy.oc1..aaaaaaaawtn7irpmolyzfoxqyzmigdkiffwy7cejmkilajquov7jwdln3j6a')
print(response.data)
