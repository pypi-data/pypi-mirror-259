from lib.interface import AwsInterface


class Subnet(AwsInterface):

    def __init__(self):
        super().__init__("ec2", "2016-11-15")

    def CreateSubnet(self, region: str, **kwargs) -> dict:
        """
        Given a region and request arguments, creates a subnet
        """

        resp = self.post(region, "CreateSubnet", **kwargs)
        return resp["CreateSubnetResponse"]

    def DescribeSubnets(self, region: str) -> list:
        """
        Given a region, returns a list of all subnets available in that region
        """

        resp = self.get(region, "DescribeSubnets")
        return resp["DescribeSubnetsResponse"]

    def DeleteSubnet(self, region: str,**kwargs) -> dict:
        """
        Given a region and request arguments, deletes a subnet
        """

        resp = self.post(region, "DeleteSubnet", **kwargs)
        return resp["DeleteSubnetResponse"]
