
```shell

aws iam create-role --role-name ecs-opensearch --assume-role-policy-document file://assume-role-policy.json

arn:aws:iam::202329666608:role/ecs-opensearch


aws iam create-policy \
    --policy-name opensearch-curd \
    --policy-document file://opensearch-curd.json

{
    "Policy": {
        "PolicyName": "opensearch-curd",
        "PolicyId": "ANPAS6G6JWQYHDYRDARAJ",
        "Arn": "arn:aws:iam::202329666608:policy/opensearch-curd",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2024-08-22T01:20:11+00:00",
        "UpdateDate": "2024-08-22T01:20:11+00:00"
    }
}


aws iam attach-role-policy --role-name ecs-opensearch --policy-arn arn:aws:iam::202329666608:policy/opensearch-curd

```

```shell
PUT /sample-index1

{
  "mappings": {
    "properties": {
      "age": {
        "type": "integer"
      }
    }
  },
  "aliases": {
    "sample-alias1": {}
  }
}


GET /sample-index1


```