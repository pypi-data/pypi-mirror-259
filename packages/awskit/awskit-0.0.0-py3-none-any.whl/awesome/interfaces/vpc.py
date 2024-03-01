from lib.interface import AwsInterface


class Vpc(AwsInterface):

    def __init__(self):
        super().__init__("ec2", "2016-11-15")

    def CreateVpc(self, region: str, **kwargs) -> dict:
        """
        Given a region and request arguments, creates a VPC
        """

        resp = self.post(region, "CreateVpc", **kwargs)
        return resp["CreateVpcResponse"]

    def DescribeVpcs(self, region: str) -> list:
        """
        Given a region, returns a list of all VPCs available in that region
        """

        resp = self.get(region, "DescribeVpcs")
        return resp["DescribeVpcsResponse"]

    def DeleteVpc(self, region: str,**kwargs) -> dict:
        """
        Given a region and request arguments, deletes a VPC
        """

        resp = self.post(region, "DeleteVpc", **kwargs)
        return resp["DeleteVpcResponse"]
