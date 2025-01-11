from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Type, Union

from src.control.base import BaseController, BaseControllerParams
from src.control.mpc import MPCParams, MPC
from src.control.pid import PIDParams, PID
from src.utils import load_dataclass_from_dict


class ParamsBuilder(ABC):
    """Abstract base class for parameter builders."""
    @abstractmethod
    def build(self, config: Dict[str, Any]) -> BaseControllerParams:
        pass

class MPCParamsBuilder(ParamsBuilder):
    def build(self, config: Dict[str, Any]) -> MPCParams:
        return load_dataclass_from_dict(
            dataclass=MPCParams,
            data_dict=config,
            convert_list_to_array=True
        )

class PIDParamsBuilder(ParamsBuilder):
    def build(self, config: Dict[str, Any]) -> PIDParams:
        return load_dataclass_from_dict(
            dataclass=PIDParams,
            data_dict=config,
            convert_list_to_array=False,
        )

class ConfigFactory:
    """
    To add a new controller type:
    1. Implement a new `ParamsBuilder` class.
    2. Add it to `params_builder_map`.
    """
    def __init__(self):
        self.params_builder_map: Dict[str, Type] = {
            "mpc": MPCParamsBuilder,
            "pid": PIDParamsBuilder,
        }

    def build(self, config: Dict):
        control_type = config["control_type"].lower()
        params_builder: ParamsBuilder = self.params_builder_map.get(control_type)
        if params_builder is None:
            raise ValueError(
                f"Invalid control type: {control_type}. "
                f"Valid types are: {list(self._builders.keys())}"
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
        self.controller_map: Dict[Type, Type] = {
            MPCParams: MPC,
            PIDParams: PID,
        }
        
    def build(self, params: BaseControllerParams) -> BaseController:
        controller_class = self.controller_map.get(params.__class__)
        if controller_class is None:
            raise ValueError(
                f"Unsupported parameter type: {params.__class__.__name__}. "
                f"Supported types are: {[cls.__name__ for cls in self.controller_map.keys()]}"
            )
        return controller_class(params)
