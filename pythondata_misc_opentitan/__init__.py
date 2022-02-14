import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10290"
version_tuple = (0, 0, 10290)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10290")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10164"
data_version_tuple = (0, 0, 10164)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10164")
except ImportError:
    pass
data_git_hash = "686e47a3f7c2f72cb6b915209921a98a857652ed"
data_git_describe = "v0.0-10164-g686e47a3f"
data_git_msg = """\
commit 686e47a3f7c2f72cb6b915209921a98a857652ed
Author: Nigel Scales <nigel.scales@gmail.com>
Date:   Tue Oct 19 15:46:28 2021 +0100

    [adc_ctrl/dv] Added adc_ctrl_filters_polled test
    
    - Added test adc_ctrl_filters_polled
    - Added test sequence adc_ctrl_filters_polled_vseq.sv
    Configures DUT in mormal power mode and ensures filter_status register
    works accoring to the model in the scoreboard
    - Added filters model to the scoreboard
    - Added power up time assertion and control
    - Temporary disable of power up time assertion for smoke test
    
    Signed-off-by: Nigel Scales <nigel.scales@gmail.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
