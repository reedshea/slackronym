# slackronym

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. The AWS resources are defined in the `template.yaml` file in this project. 

## Use the SAM CLI to build and test locally

Build the application with the `sam build` command.

```bash
slackronym$ sam build
```

Run functions locally and invoke them with the `sam local invoke` command.

```bash
slackronym$ sam local invoke SlackronymFunction --event events/event.json
```

## Tests

Tests are defined in the `tests` folder in this project.

```bash
slackronym$ pytest
```


## Deploy the sample application using GitHub Actions

* Create a user in AWS IAM. Save the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in GitHub Actions Secrets.
* Create another GitHub Actions Secret for `AWS_REGION`, like `us-east-1`
* Attach an IAM policy to the user that is similar to the JSON below (or ideally more tightly scoped):

```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": [
				"iam:AttachRolePolicy",
				"iam:CreateRole",
				"iam:DeleteRole",
				"iam:DetachRolePolicy",
				"iam:PassRole",
				"iam:GetRole",
				"iam:PutRolePolicy",
				"iam:TagRole",
				"cloudformation:CreateChangeSet",
				"cloudformation:DeleteStack",
				"cloudformation:DescribeStacks",
				"cloudformation:UpdateStack",
				"cloudformation:CreateStack",
				"cloudformation:ExecuteChangeSet",
				"cloudformation:DescribeChangeSet",
				"cloudformation:DescribeStackEvents",
				"s3:CreateBucket",
				"s3:PutObject",
				"s3:GetObject",
				"s3:ListBucket",
				"lambda:*"
			],
			"Resource": "*"
		}
	]
}
```