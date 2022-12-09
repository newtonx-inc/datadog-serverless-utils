import functools
import logging
import sys

from ddtrace import patch_all, tracer

logger = logging.getLogger(__name__)


def datadog_serverless(error_return_value=None):
    """
    Decorator that sends an error trace to DataDog when the decorated function raises an exception.
    DataDog must be set up.
    This is especially useful for ephemeral execution environments, such as Cloud Functions,
    where the Datadog tracer does not have a chance to send the telemetry data before the execution is finished.

    :param error_return_value: Value to return if the decorated function raises an exception
    :return: Whatever the decorated function returns if it raises no exception, otherwise return error_return_value
    """

    def decorator_datadog_serverless(fn):
        @functools.wraps(fn)
        def wrapper_datadog_serverless(*args, **kwargs):
            patch_all()

            res = error_return_value
            try:
                res = fn(*args, **kwargs)
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                logger.exception(exc_value)

                # Get root span
                root_span = tracer.current_root_span()
                print(f'Current root span: {root_span}')
                print(f'Current tags on root span: {root_span.get_tags()}')

                # Set exception
                root_span.set_exc_info(exc_type, exc_value, exc_traceback)
            finally:
                # Flush tracer
                print("Flushing tracer...")
                tracer.flush()
                return res

        return wrapper_datadog_serverless

    return decorator_datadog_serverless
