# -*- coding: utf-8 -*-

import os
import unittest
import time
from intercom import Intercom
from intercom import Event
from intercom import User

Intercom.personal_access_token = os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN')


class Issue72Test(unittest.TestCase):

    def test(self):
        User.create(email='me@example.com')
        # no exception here as empty response expected
        data = {
            'event_name': 'Eventful 1',
            'created_at': int(time.time()),
            'email': 'me@example.com'
        }
        Event.create(**data)
