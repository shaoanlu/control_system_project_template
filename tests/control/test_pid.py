from src.control.pid import PID, PIDParams

def test_pid():
    params = PIDParams(kp=1.0, ki=0.1, kd=0.01)
    pid = PID(params)
    error = 1.0
    dt = 0.1
    output = pid.control(error, dt)
    assert output == 1.1, f"Expected output to be 1.1, but got {output}"
    print("Test passed!")