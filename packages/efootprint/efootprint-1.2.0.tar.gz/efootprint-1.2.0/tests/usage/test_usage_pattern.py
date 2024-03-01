from efootprint.abstract_modeling_classes.explainable_objects import ExplainableHourlyUsage
from efootprint.constants.countries import Countries
from efootprint.constants.sources import Sources
from efootprint.abstract_modeling_classes.source_objects import SourceValue, SourceObject
from efootprint.core.usage.usage_pattern import UsagePattern
from efootprint.constants.units import u

import unittest
from unittest.mock import MagicMock, patch


class TestUsagePattern(unittest.TestCase):
    def setUp(self):
        self.storage = MagicMock()
        self.server = MagicMock()
        self.service1 = MagicMock()
        self.service2 = MagicMock()

        user_journey = MagicMock()
        user_journey.duration = SourceValue(2.0 * u.min / u.user_journey, label="duration")
        user_journey.data_upload = SourceValue(2.0 * u.MB / u.user_journey, label="data_upload")
        user_journey.data_download = SourceValue(3.0 * u.MB / u.user_journey, label="data_download")

        user_journey.services = [self.service1, self.service2]
        population = MagicMock()
        population.nb_devices = SourceValue(10000 * u.user, label="population")
        population.country = Countries.FRANCE()

        network = MagicMock()

        self.usage_pattern = UsagePattern(
            "usage_pattern", user_journey, population, network,
            user_journey_freq_per_user=SourceValue(10 * u.user_journey / (u.user * u.year)),
            time_intervals=SourceObject([[8, 16]], Sources.USER_DATA)
        )

    def test_check_time_intervals_validity(self):
        self.usage_pattern.check_time_intervals_validity([[0, 5], [6, 10], [15, 20]])

    def test_invalid_start_time(self):
        with self.assertRaises(ValueError):
            self.usage_pattern.check_time_intervals_validity([[5, 3], [7, 10]])

    def test_interval_overlap(self):
        with self.assertRaises(ValueError):
            self.usage_pattern.check_time_intervals_validity([[0, 5], [4, 10]])

    def test_update_usage_time_fraction(self):
        hourly_usage = ExplainableHourlyUsage([1 * u.dimensionless] * 2 + [0 * u.dimensionless] * 22, "hourly usage")
        with patch.object(self.usage_pattern, "hourly_usage", hourly_usage):
            self.usage_pattern.update_usage_time_fraction()
            self.assertEqual((2 / 24) * u.dimensionless, self.usage_pattern.usage_time_fraction.value)

    def test_update_hourly_usage(self):
        with patch.object(self.usage_pattern, "time_intervals", SourceObject([[0, 5], [6, 10], [15, 20]])):
            self.usage_pattern.update_hourly_usage()

            for i in range(24):
                if 0 <= i < 5 or 6 <= i < 10 or 15 <= i < 20:
                    self.assertEqual(self.usage_pattern.hourly_usage.value[i], 1 * u.dimensionless)
                else:
                    self.assertEqual(self.usage_pattern.hourly_usage.value[i], 0 * u.dimensionless)

    def test_services(self):
        self.assertEqual([self.service1, self.service2], self.usage_pattern.services)


if __name__ == '__main__':
    unittest.main()
