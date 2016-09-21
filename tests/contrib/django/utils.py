# 3rd party
from django.db import connections
from django.test import TestCase
from django.template import Template

# project
from ddtrace.tracer import Tracer
from ddtrace.contrib.django.conf import settings

# testing
from ...test_tracer import DummyWriter


# testing tracer
tracer = Tracer()
tracer.writer = DummyWriter()


class DjangoTraceTestCase(TestCase):
    """
    Base class that provides an internal tracer according to given
    Datadog settings. This class ensures that the tracer spans are
    properly reset after each run. The tracer is available in
    the ``self.tracer`` attribute.
    """
    def setUp(self):
        # assign the default tracer
        self.tracer = settings.DEFAULT_TRACER
        # empty the tracer spans from previous operations
        # such as database creation queries
        self.tracer.writer.spans = []

    def tearDown(self):
        # empty the tracer spans from test operations
        self.tracer.writer.spans = []
