import unittest
from typing import Any, Dict
import numpy as np
from dataclasses import dataclass, field, KW_ONLY

from src.control.algorithm.base import BaseController, BaseControllerParams, BaseParamsBuilder
from src.control.algorithm.pid import PID, PIDParams
from src.control.algorithm.mpc import MPC, MPCParams
from src.control.controller_factory import ConfigFactory, ControllerFactory

# Create dummy classes for testing

@dataclass
class DummyParams(BaseControllerParams):
    _: KW_ONLY  # Make all following fields keyword-only
    value: int
    algorithm_type: str = field(default="dummy")

class DummyParamsBuilder(BaseParamsBuilder):
    @staticmethod
    def build(config: Dict[str, Any]) -> DummyParams:
        return DummyParams(value=config.get("value", 0))
    
class DummyController(BaseController):
    def __init__(self, params):
        self.params = params

    def control(self, state: np.ndarray, **kwargs) -> np.ndarray:
        pass

class TestFactories(unittest.TestCase):
    def setUp(self):
        self.config_factory = ConfigFactory()
        self.controller_factory = ControllerFactory()

        # Add dummy classes to the factories' maps
        self.config_factory.register_map("dummy", DummyParamsBuilder)
        self.controller_factory.register_map(DummyParams, DummyController)
        self.controller_factory.config_factory = self.config_factory
        
        # Create sample configs
        self.dummy_config = {
            "algorithm_type": "dummy",
            "value": 42
        }
        self.mpc_config = {
            "algorithm_type": "mpc",
            "Q": np.eye(2),
            "R": np.eye(1)
        }
        self.pid_config = {
            "algorithm_type": "pid",
            "kp": 1.0,
            "ki": 0.1,
            "kd": 0.01
        }

    def test_config_factory_with_dummy(self):
        # Test building dummy params
        params = self.config_factory.build(self.dummy_config)
        self.assertIsInstance(params, DummyParams)
        self.assertEqual(params.value, 42)
        self.assertEqual(params.algorithm_type, "dummy")

    def test_config_factory_with_mpc(self):
        # Test building MPC params
        params = self.config_factory.build(self.mpc_config)
        self.assertIsInstance(params, MPCParams)
        self.assertTrue(np.array_equal(params.Q, np.eye(2)))
        self.assertTrue(np.array_equal(params.R, np.eye(1)))
        self.assertEqual(params.algorithm_type, "mpc")

    def test_config_factory_with_pid(self):
        # Test building PID params from config dictionary
        params = self.config_factory.build(self.pid_config)

        # No error should be raised and the params should match the config
        self.assertIsInstance(params, PIDParams)
        self.assertEqual(params.kp, 1.0)
        self.assertEqual(params.ki, 0.1)
        self.assertEqual(params.kd, 0.01)
        self.assertEqual(params.algorithm_type, "pid")

    def test_config_factory_invalid_type(self):
        # Test invalid algorithm type
        invalid_config = {"algorithm_type": "invalid"}
        with self.assertRaises(ValueError):
            self.config_factory.build(invalid_config)

    def test_controller_factory_with_dummy(self):
        # Test building dummy controller from params
        params = DummyParams(value=42)
        controller = self.controller_factory.build(params)
        self.assertIsInstance(controller, DummyController)
        
        # Test building dummy controller from dict
        params_dict = {"value": 42, "algorithm_type": "dummy"}
        controller = self.controller_factory.build_from_dict(params_dict)
        self.assertIsInstance(controller, DummyController)


    def test_controller_factory_with_mpc(self):
        # Test building MPC controller from params
        params = MPCParams(Q=np.eye(2), R=np.eye(1))
        controller = self.controller_factory.build(params)
        self.assertIsInstance(controller, MPC)

        # Test building MPC controller from dict
        params_dict = {"Q": np.eye(2), "R": np.eye(1), "algorithm_type": "mpc"}
        controller = self.controller_factory.build_from_dict(params_dict)
        self.assertIsInstance(controller, MPC)

    def test_controller_factory_with_pid(self):
        # Test building PID controller from params
        params = PIDParams(kp=1.0, ki=0.1, kd=0.01)
        controller = self.controller_factory.build(params)
        self.assertIsInstance(controller, PID)
        
        # Test building PID controller from dict
        params_dict = {"kp": 1.0, "ki": 0.1, "kd": 0.01, "algorithm_type": "pid"}
        controller = self.controller_factory.build_from_dict(params_dict)
        self.assertIsInstance(controller, PID)

    def test_controller_factory_invalid_params(self):
        # Test invalid parameter type
        class InvalidParams(BaseControllerParams):
            algorithm_type = "invalid_params"
        
        invalid_params = InvalidParams()
        with self.assertRaises(ValueError):
            self.controller_factory.build(invalid_params)

if __name__ == '__main__':
    unittest.main()