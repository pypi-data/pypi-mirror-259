from lib.interface import AwsInterface


class SecurityGroup(AwsInterface):

    def __init__(self):
        super().__init__("ec2", "2016-11-15")
    
    def CreateSecurityGroup(self, region: str, **kwargs) -> dict:
        """
        Given a region and request arguments, creates a security group
        """

        resp = self.post(region, "CreateSecurityGroup", **kwargs)
        return resp["CreateSecurityGroupResponse"]

    def DescribeSecurityGroups(self, region: str) -> list:
        """
        Given a region, returns a list of all security groups available in that region
        """

        resp = self.get(region, "DescribeSecurityGroups")
        return resp["DescribeSecurityGroupsResponse"]

    def DeleteSecurityGroup(self, region: str, **kwargs) -> dict:
        """
        Given a region and request arguments, deletes a security group
        """

        resp = self.post(region, "DeleteSecurityGroup", **kwargs)
        return resp["DeleteSecurityGroupResponse"]
