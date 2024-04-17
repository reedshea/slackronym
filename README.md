<p align="center">
    <img src="logo.jpg" width="150">
</p>

# slackronym

Simple AWS Lambda function for looking up acronyms with a Slack `slash` command.


## Getting started

To get this Slack integration up and running, you will need to:

1.  Fork this repository
2.  Add GitHub Actions secrets to your new repository to allow deployment to
    your AWS environment. See below for more details.
3.  Update `acronyms.csv` with your organization's acronyms
4.  Deploy the app to AWS using the included GitHub Actions workflow. There
    should be a Function URL available in the `slackronym` Lambda function.
5.  Create and install a Slack app that uses a "slash command" to send requests
    to that Function URL


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

* Create a user in AWS IAM. Save the `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY` in GitHub Actions Secrets.
* Attach an IAM policy to the user that is similar to the JSON below (or
ideally more tightly scoped):

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
