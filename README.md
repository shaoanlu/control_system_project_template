# controller_project_template

## References
- https://github.com/facebookresearch/home-robot/tree/main
- https://github.com/LeCAR-Lab/CoVO-MPC/tree/main
- https://github.com/stephane-caron/qpmpc/tree/main
- https://github.com/Simple-Robotics/aligator/tree/main
- https://github.com/utiasDSL/safe-control-gym/tree/main
- https://github.com/LeCAR-Lab/dial-mpc/tree/main

## Considerations
- Assume each module (`src/control`, `src/state_estimation`, etc) are maintained by different teams
  - We are fine with some code duplications (e.g. `ParamsBuilder`) across these modules as each team has customizations of teir own
  - Unless the code structure becomes incomprehensible to certain degree
- Should we keep config files in a separate folder instead of putting them in module folder?

## Note
- Use `tap` to hadle configs? so that type hint for config args can be simplified
