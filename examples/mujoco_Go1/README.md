# Adoptingg The Template to Make A New PPO Policy For Mujoco Go1 Tasks

## File Description
- `ppo.py`: this file is a wrapper for PPO agen in brax to fit the interface of the repo template
- `env_wrapper.py` this file is a wrapper to mujoco env to fit the interface of the repo template
- `demo.py`: the demo script. Result is shown below

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
python3 examples/mujoco_Go1Handstand/demo.py  --env_name Go1Handstand
# or
python3 examples/mujoco_Go1Handstand/demo.py  --env_name Go1JoystickFlatTerrain
```