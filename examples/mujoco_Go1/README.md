# Adoptingg The Template to Make A New PPO Policy For Mujoco Go1 Tasks

## File Description
- `ppo.py`: Implement a MLP network as well as the `Controller` interfaces based on the repo template
- `env_wrapper.py` A wrapper to mujoco env to the `Env` interface of the repo template
- `demo.py`: The demo script. Result is shown below.

## Result
![](ppo_Go1Handstand.gif) ![](ppo_Go1JoystickFlatTerrain.gif)

## Requirements
- `mujoco`
- `mujoco_mjx`
- `brax`
- `mujoco_playground`
- `mediapy`
- `tqdm`

## Installation
```bash
pip install mujoco mujoco_mjx brax playground mediapy
```

## Execution
```bash
# navigate to root folder of the repo
python3 examples/mujoco_Go1/demo.py  --env_name Go1Handstand
# or
python3 examples/mujoco_Go1/demo.py  --env_name Go1JoystickFlatTerrain
```

In Google Colab
```bash
# Installation
...
# clone this repo
!git clone https://github.com/shaoanlu/control_system_project_template.git

# navigate to repo root
%cd control_system_project_template

# run the demo
!PYTHONPATH="/content/control_system_project_template" python examples/mujoco_Go1/demo.py --env_name Go1Handstand
# or 
!PYTHONPATH="/content/control_system_project_template" python examples/mujoco_Go1/demo.py --env_name Go1JoystickFlatTerrain
# or copy-paste demo.py to a Colab cell
```