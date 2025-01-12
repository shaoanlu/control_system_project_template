from typing import Any, Dict, Type

from src.control.algorithm.base import BaseController, BaseControllerParams, BaseParamsBuilder
from src.control.algorithm.mpc import MPCParams, MPCParamsBuilder, MPC
from src.control.algorithm.pid import PIDParams, PIDParamsBuilder, PID


class ConfigFactory:
    """
    To add a new controller config type:
    1. Implement a new `ParamsBuilder` class.
    2. Add it to `params_builder_map`.
    """
    def __init__(self):
        self.params_builder_map: Dict[str, Type[BaseControllerParams]] = {
            "mpc": MPCParamsBuilder,
            "pid": PIDParamsBuilder,
        }

    def build(self, config: Dict[str, Any]):
        control_type = config["control_type"].lower()
        params_builder: BaseParamsBuilder = self.params_builder_map.get(control_type)
        if params_builder is None:
            raise ValueError(
                f"Invalid control type: {control_type}. "
                f"Valid types are: {list(self.params_builder_map.keys())}"
            )
        else:
            return params_builder.build(config)
    
class ControllerFactory:
    """
    Example usage:
        config = load_yaml(path_to_config_file)
        controller_params = ConfigFactory(config).build()
        controller = ControllerFactory().build(controller_params)
    
    To add a new controller type:
    1. Add it to `controller_map`.
    """
    def __init__(self):
        self.controller_map: Dict[Type[BaseControllerParams], Type[BaseController]] = {
            MPCParams: MPC,
            PIDParams: PID,
        }
        
    def build(self, params: BaseControllerParams) -> BaseController:
        controller_class = self.controller_map.get(type(params))
        if controller_class is None:
            raise ValueError(
                f"Unsupported parameter type: {params.__class__.__name__}. "
                f"Supported types are: {[cls.__name__ for cls in self.controller_map.keys()]}"
            )
        return controller_class(params)
