import unittest
import json
import logging
import os

import lusid_scheduler
from lusid_scheduler import JobsApi
from fbnsdkutilities import ApiClientFactory

class LusidSchedulerTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        cls.api_factory = ApiClientFactory(lusid_scheduler, api_secrets_filename="secrets.json")
        cls.api = cls.api_factory.build(lusid_scheduler.api.JobsApi)

    def test_get_types(self):

        response = self.api.list_jobs().values
        self.assertGreaterEqual(len(response), 0, response)


if __name__ == '__main__':
    unittest.main()
