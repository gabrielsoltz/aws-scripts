# Generate AWS Arns

aws_account_id = ""
aws_region = ""
aws_resource_id = ""
ResourceType = ""


def generate_arn(ResourceType, aws_account_id, aws_region, aws_resource_id):
    arn_construct = {
        "AwsEc2Vpc": "arn:aws:ec2:%s:%s:vpc:%s" % (aws_account_id, aws_region, aws_resource_id),
        "AwsCertificateManagerCertificate": "arn:aws:acm:%s:%s:certificate/%s" % (aws_account_id, aws_region, aws_resource_id),

    }
    return arn_construct[ResourceType]