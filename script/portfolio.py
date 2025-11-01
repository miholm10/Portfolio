# pip install diagrams

from diagrams import Cluster, Diagram
from diagrams.aws.general import User
from diagrams.onprem.vcs import Github
from diagrams.aws.mobile import Amplify
from diagrams.aws.network import CloudFront, Route53
from diagrams.aws.security import CertificateManager
from diagrams.aws.management import ManagementConsole
from diagrams.onprem.client import Users

with Diagram(
    "AWS Amplify Static Site Architecture",
    show=True,
    filename="amplify_static_site_architecture",
    direction="LR"
):
    developer = User("Local Development\n(PyCharm)")
    github = Github("GitHub Repository")

    with Cluster("AWS Cloud"):
        aws_console = ManagementConsole("AWS Console")

        with Cluster("us-east-1 Region"):
            with Cluster("VPC"):
                amplify = Amplify("AWS Amplify\n(Build + Deploy)")
                cloudfront = CloudFront("Amazon CloudFront\n(CDN)")
                route53 = Route53("Route 53\nCustom Domain")
                acm = CertificateManager("ACM\n(HTTPS Certificates)")

    end_users = Users("End Users\n(Global Access)")

    # Flow connections
    developer >> github >> amplify
    amplify >> cloudfront
    cloudfront >> route53
    cloudfront >> acm
    cloudfront >> end_users

print("docs generated successfully: amplify_static_site_architecture.png")