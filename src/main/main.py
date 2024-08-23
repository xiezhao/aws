import boto3
import requests
from requests_aws4auth import AWS4Auth

# 使用 STS Assume Role 获取临时凭证
client = boto3.client('sts')

# 假设角色并获取临时凭证
assumed_role = client.assume_role(
    RoleArn='arn:aws:iam::202329666608:role/opensearch-master-role',  # 替换为你的角色 ARN
    RoleSessionName='opensearch-master'
)

credentials = assumed_role['Credentials']

# 使用临时凭证创建 AWS4Auth 对象
auth = AWS4Auth(
    credentials['AccessKeyId'],
    credentials['SecretAccessKey'],
    'ap-east-1',  # 替换为你的 AWS 区域
    'es',  # OpenSearch 服务
    session_token=credentials['SessionToken']
)

# OpenSearch 域的 HTTPS 端点
opensearch_host = 'https://search-demo-nbw6jivviuknzo662g7tlwkn54.ap-east-1.es.amazonaws.com'  # 替换为你的 OpenSearch 端点

# 构建请求 URL
url = f'{opensearch_host}/_plugins/_security/api/rolesmapping/all_access'

# 设置请求头
headers = {"Content-Type": "application/json"}


# 发送签名的 GET 请求
response = requests.get(url, auth=auth)

# 输出响应状态码和响应内容
print(response.status_code)
print(response.text)
