import numpy as np
from typing import Dict, Union

from src.control.mpc import MPCParams, MPC
from src.control.pid import PIDParams, PID

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
        return MPCParams(
            control_type="mpc",
            Q=np.array(self.config["mpc"]["Q"]),
            R=np.array(self.config["mpc"]["R"])
        )
    def _build_pid(self):
        return PIDParams(
            control_type="pid",
            kp=self.config["pid"]["kp"],
            ki=self.config["pid"]["ki"],
            kd=self.config["pid"]["kd"]
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
