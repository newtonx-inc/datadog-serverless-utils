# -*- coding: utf-8 -*-
from unittest.mock import patch, MagicMock

import ddtrace

from src.utils import datadog_serverless


class TestDatadogServerless:
    @patch.object(ddtrace.Tracer, "flush")
    def test_datadog_serverless_decorator_with_exception(self, mocked_ddtrace_flush: MagicMock):
        error_return_value = "test_return_value"

        @datadog_serverless(error_return_value=error_return_value)
        def test_method():
            raise Exception()

        return_value = test_method()
        assert (
            return_value == error_return_value
        ), "Returned value should be the same as the one provided for error return"
        mocked_ddtrace_flush.assert_called_once_with()
