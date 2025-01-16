# controller_project_template

## Requirements
- Python 3.10+
- yaml

## References
- https://github.com/facebookresearch/home-robot/tree/main
- https://github.com/LeCAR-Lab/CoVO-MPC/tree/main
- https://github.com/stephane-caron/qpmpc/tree/main
- https://github.com/sea-bass/pyroboplan
- https://github.com/Simple-Robotics/aligator/tree/main
- https://github.com/LeCAR-Lab/dial-mpc/tree/main

## Considerations
- Assume each module (`src/control`, `src/state_estimation`, etc) are maintained by different teams
  - We are fine with some code duplications (e.g. `ControllerParamsBuilder`) across these modules as each team might have customizations of their own
  - ...Unless the code structure becomes incomprehensible to certain degree
- Should we keep config files in a separate folder instead of putting them in module folder?

## Note
- Use `tap` to hadle configs? so that type hint for config args can be simplified
- Consider a ROS 2 system arch?

## Todo
### Control module template
- [x] Add Draft structure
- [x] Implement factory pattern
- [x] Write documents
- [ ] Testing
  - [x] Write tests for controller classes
  - [x] Write tests for factories
- [ ] Exception Handling
  - [ ] Add parameter validation exceptions
  - [ ] Add runtime exceptions
### Estimation module template
- [x] Draft observer structure
- [x] Implement observer pattern
- [ ] Tessting
### Planning module template
- [ ] Draft observer structure
- [ ] Implement ??? pattern
- [ ] Tessting
### System Integration
- [ ] Integration Tests
  - [ ] End-to-end controller tests
  - [ ] Configuration loading tests
- [ ] GitHub Actions CI
  - [x] Add linting and code formatting (ruff)
  - [ ] Add type checking (mypy)
  - [ ] Set up code coverage reporting
- [ ] Package Management
  - [x] Set up setup.py/project.toml
  - [ ] Define dependencies
  - [ ] Provide minimal Docker environment


## Memo
- `ruff format`
- `ruff check` or `ruff check --fix`