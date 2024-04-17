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
