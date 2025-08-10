# automation_aws

This project automates the scheduled start and stop of specific AWS EC2 instances using GitHub Actions and Python.

## Features

- Automatically starts and stops EC2 instances based on a schedule (Lima time).
- Targets instances by tag (`base-server`, `keycloak-server`).
- Uses GitHub Actions for orchestration and AWS credentials from repository secrets.

## Prerequisites

- AWS account with EC2 instances tagged appropriately.
- GitHub repository with the following secrets configured:
  - `AWS_ACCESS_KEY`
  - `AWS_SECRET_ACCESS_KEY`

## Setup

1. Clone this repository.
2. Ensure your EC2 instances have the tags:
   - `Name: base-server`
   - `Name: keycloak-server`
3. Add your AWS credentials as GitHub secrets.
4. Review and adjust the schedule in `.github/workflows/ec2_scheduler_shutdown.yml` as needed.

## Usage

### Scheduled Automation

The workflow runs automatically:
- **Start instances:** Monday to Saturday at 5:00 AM Lima time (10:00 AM UTC)
- **Stop instances:** Tuesday to Saturday and Sunday at 9:00 PM Lima time (2:00 AM UTC)

### Manual Trigger

You can also trigger the workflow by pushing to the `main` branch for testing.

## Workflow Details

See `.github/workflows/ec2_scheduler_shutdown.yml` for the automation logic. The workflow:
- Installs dependencies
- Configures AWS credentials
- Determines whether to start or stop instances based on the schedule
- Runs `manage_ec2.py` with the appropriate action

## Python Script

`manage_ec2.py` manages EC2 instances:
- Starts or stops instances based on command-line argument (`start` or `stop`)
- Filters instances by tag and state

## License

MIT License

## Author

Yomar
