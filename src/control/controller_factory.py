import numpy as np
from typing import Dict, Union

from src.control.mpc import MPCParams, MPC
from src.control.pid import PIDParams, PID
from src.utils import load_dataclass_from_dict

class ConfigFactory:
    def __init__(self, config: Dict):
        self.config = config

    def build(self):
        if self.config["control_type"].lower() == "mpc":
            return self._build_mpc()
        elif self.config["control_type"].lower() == "pid":
            return self._build_pid()
        else:
            raise ValueError(f"Invalid control type: {self.config['control_type']}")
        
    def _build_mpc(self):
        return load_dataclass_from_dict(
            dataclass=MPCParams,
            data_dict=self.config,
            convert_list_to_array=True
        )
    def _build_pid(self):
        # return PIDParams(
        #     control_type="pid",
        #     kp=self.config["kp"],
        #     ki=self.config["ki"],
        #     kd=self.config["kd"]
        # )
        return load_dataclass_from_dict(
            dataclass=PIDParams,
            data_dict=self.config,
            convert_list_to_array=False,
        )
    
class ControllerFactory:
    """
    Example usage:
        config = load_yaml(path_to_config_file)
        controller_config = ConfigFactory(config).build()
        controller = ControllerFactory().build(controller_config)
    """
    def __init__(self):
        pass
        
    def build(self, config: Union[MPCParams, PIDParams]):
        if config.control_type == "mpc":
            return MPC(config)
        elif config.control_type == "pid":
            return PID(config)
        else:
            raise ValueError(f"Invalid control type: {config.control_type}")
