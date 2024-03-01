from efootprint.abstract_modeling_classes.explainable_objects import ExplainableQuantity, ExplainableHourlyUsage
from efootprint.constants.sources import Sources
from efootprint.abstract_modeling_classes.source_objects import SourceValue
from efootprint.constants.units import u
from efootprint.core.service import Service

import unittest
from unittest.mock import MagicMock, patch, PropertyMock


class TestService(unittest.TestCase):
    def setUp(self):
        self.server = MagicMock()
        self.storage = MagicMock()
        self.server.name = "server"
        self.storage.name = "storage"
        self.base_ram = SourceValue(4 * u.GB, Sources.HYPOTHESIS)
        self.base_cpu = SourceValue(2 * u.core, Sources.HYPOTHESIS)
        self.service = Service("Test Service", self.server, self.storage, self.base_ram, self.base_cpu)
        self.service.dont_handle_input_updates = True

    def test_service_initialization(self):
        self.assertEqual(self.service.name, "Test Service")
        self.assertEqual(self.service.server, self.server)
        self.assertEqual(self.service.storage, self.storage)
        self.assertEqual(self.service.base_ram_consumption, self.base_ram)
        self.assertEqual(self.service.base_cpu_consumption, self.base_cpu)
        self.assertEqual(ExplainableHourlyUsage([0 * u.GB] * 24, " "), self.service.hour_by_hour_ram_need)
        self.assertEqual(ExplainableHourlyUsage([0 * u.core] * 24, " "), self.service.hour_by_hour_cpu_need)
        self.assertEqual(ExplainableQuantity(0 * u.TB / u.year, " "), self.service.storage_needed)

    def test_service_invalid_ram_consumption(self):
        invalid_ram = SourceValue(4 * u.min)
        with self.assertRaises(ValueError):
            Service("Invalid RAM Service", self.server, self.storage, invalid_ram)

    def test_service_invalid_cpu_consumption(self):
        invalid_cpu = SourceValue(2 * u.min)
        with self.assertRaises(ValueError):
            Service("Invalid CPU Service", self.server, self.storage, self.base_ram, invalid_cpu)

    def test_update_storage_needed(self):
        usage_pattern1 = MagicMock()
        usage_pattern1.user_journey_freq = ExplainableQuantity(10 * u.user_journey / u.day, "uj_freq")
        usage_pattern2 = MagicMock()
        usage_pattern2.user_journey_freq = ExplainableQuantity(100 * u.user_journey / u.day, "uj_freq")
        
        uj_step1 = MagicMock()
        uj_step1.service = self.service
        uj_step1.data_upload = ExplainableQuantity(1 * u.MB / u.user_journey, "data_upload")
        uj_step1.usage_patterns = [usage_pattern1]
        uj_step2 = MagicMock()
        uj_step2.service = self.service
        uj_step2.data_upload = ExplainableQuantity(3 * u.MB / u.user_journey, "data_upload")
        uj_step2.usage_patterns = [usage_pattern2]

        with patch.object(self.service, "modeling_obj_containers", [uj_step1, uj_step2]):
            self.service.update_storage_needed()
            self.assertEqual(
                round((310 * u.MB / u.day).to(u.TB / u.year), 3), round(self.service.storage_needed.value, 3))

    def test_update_hour_by_hour_ram_need(self):
        uj_step = MagicMock()
        uj_step.service = self.service
        uj_step.ram_needed = ExplainableQuantity(1.8 * u.GB, "ram_needed")
        uj_step.request_duration = ExplainableQuantity(10 * u.min, "request_duration")

        uj_step2 = MagicMock()
        uj_step2.service = self.service
        uj_step2.ram_needed = ExplainableQuantity(0.6 * u.GB, "ram_needed")
        uj_step2.request_duration = ExplainableQuantity(10 * u.min, "request_duration")

        usage_pattern = MagicMock()
        usage_pattern.user_journey.duration = ExplainableQuantity(1 * u.hour, "uj_duration")
        usage_pattern.nb_user_journeys_in_parallel_during_usage = ExplainableQuantity(
            10 * u.user_journey, "parallel_uj")
        usage_pattern.utc_time_intervals = ExplainableHourlyUsage(
            [1 * u.dimensionless] * 24, "utc_time_intervals")

        for elt in [uj_step, uj_step2]:
            elt.usage_patterns = [usage_pattern]

        with patch.object(self.service, "modeling_obj_containers", [uj_step, uj_step2]):
            self.service.update_hour_by_hour_ram_need()

            self.assertEqual(
                [4 * u.GB] * 24,
                [round(elt, 2) for elt in self.service.hour_by_hour_ram_need.value])

    def test_update_hour_by_hour_cpu_need(self):
        uj_step = MagicMock()
        uj_step.service = self.service
        uj_step.cpu_needed = ExplainableQuantity(1.8 * u.core, "cpu_needed")
        uj_step.request_duration = ExplainableQuantity(10 * u.min, "request_duration")

        uj_step2 = MagicMock()
        uj_step2.service = self.service
        uj_step2.cpu_needed = ExplainableQuantity(0.6 * u.core, "cpu_needed")
        uj_step2.request_duration = ExplainableQuantity(10 * u.min, "request_duration")

        usage_pattern = MagicMock()
        usage_pattern.user_journey.duration = ExplainableQuantity(1 * u.hour, "uj_duration")
        usage_pattern.nb_user_journeys_in_parallel_during_usage = ExplainableQuantity(
            10 * u.user_journey, "uj_in_parallel")
        usage_pattern.utc_time_intervals = ExplainableHourlyUsage([1 * u.dimensionless] * 24, "utc time intervals")

        for elt in [uj_step, uj_step2]:
            elt.usage_patterns = [usage_pattern]

        with patch.object(self.service, "modeling_obj_containers", [uj_step, uj_step2]):
            self.service.update_hour_by_hour_cpu_need()

            self.assertEqual(
                [4 * u.core] * 24,
                [round(elt, 2) for elt in self.service.hour_by_hour_cpu_need.value])

    def test_self_delete_should_raise_error_if_self_has_associated_uj_steps(self):
        uj_step = MagicMock()
        uj_step.name = "uj_step"
        self.service.modeling_obj_containers = [uj_step]
        with self.assertRaises(PermissionError):
            self.service.self_delete()

    def test_self_delete_removes_backward_links_and_recomputes_server_and_storage(self):
        with patch.object(Service, "mod_obj_attributes", new_callable=PropertyMock) as mock_mod_obj_attributes:
            mock_mod_obj_attributes.return_value = [self.server, self.storage]
            self.server.modeling_obj_containers = [self.service]
            self.storage.modeling_obj_containers = [self.service]
            self.service.self_delete()
            self.assertEqual([], self.server.modeling_obj_containers)
            self.assertEqual([], self.storage.modeling_obj_containers)
            self.server.launch_attributes_computation_chain.assert_called_once()
            self.storage.launch_attributes_computation_chain.assert_called_once()


if __name__ == '__main__':
    unittest.main()
