from awskit.interface import AwsInterface


class S3(AwsInterface):

    def __init__(self):
        super().__init__("s3", "2006-03-01")
    
    def CreateBucket(self, region: str, **kwargs) -> dict:
        """
        """

        resp = self.post(region, "CreateBucket", **kwargs)
        return resp["CreateSecurityGroupResponse"]
