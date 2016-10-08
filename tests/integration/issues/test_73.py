# -*- coding: utf-8 -*-
"""
How do I record when a User has started a new session?
"""

import os
import unittest
from intercom import Intercom
from intercom import User

Intercom.personal_access_token = os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN')


class Issue73Test(unittest.TestCase):

    def test(self):
        user = User.create(email='bingo@example.com')
        # store current session count
        session_count = user.session_count

        # register a new session
        user.new_session = True
        user.save()

        # count has increased by 1
        self.assertEquals(session_count + 1, user.session_count)

        # register a new session
        user.new_session = True
        user.save()

        # count has increased by 1
        self.assertEquals(session_count + 2, user.session_count)
