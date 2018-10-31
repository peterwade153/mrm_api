import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.events_ratios_fixtures import (
    event_ratio_query,
    event_ratio_response
)

sys.path.append(os.getcwd())


class TestEventRatios(BaseTestCase):

    def test_events_checkins_to_bookings_ratio(self):
        """
        Test that an event can be checked into with correct details
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_query,
            event_ratio_response
        )
