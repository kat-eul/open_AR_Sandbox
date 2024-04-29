# calibrate_sensor_server.py
from bokeh.plotting import curdoc
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from sandbox import _calibration_dir, set_logger
from sandbox.sensor import CalibSensor
logger = set_logger(__name__)

sensor_type = "kinect_v2"

calib_proj = _calibration_dir + 'my_projector_calibration.json'
module = CalibSensor(calibprojector = calib_proj, name = sensor_type)

widget = module.calibrate_sensor()
current = widget.get_root()
curdoc().add_root(current)