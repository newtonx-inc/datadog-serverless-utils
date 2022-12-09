# DataDog Serverless Utils
Utilities for integration between serverless execution environments and DataDog

## Error Tracking for Serverless Execution Environments
Serverless execution environments (e.g. Cloud Functions) are finished by the cloud provider as soon as the execution
finished. Sometimes, the DataDog tracer [(ddtrace)](https://ddtrace.readthedocs.io/en/stable/) does not 
have a chance to send the collected traces especially when it ends abruptly due to an unhandled exception.

This library offers a decorator to make sure ddtrace can send the telemetry data before the execution ends.

### Setup

Make sure ddtrace config is correctly set up as mentioned on the [docs](https://ddtrace.readthedocs.io/en/stable/installation_quickstart.html#tracing). 

### Usage

Decorate your function as follows and voilà!

```
from datadog_serverless_utils import datadog_serverless


@datadog_serverless
def main():
    ...
```

A return value can be specified for the case when the decorated function raises an unhandled exception via the parameter `error_return_value`:

```
@datadog_serverless(error_return_value="my_value")
def main():
    ...
```
