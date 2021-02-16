import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5016"
version_tuple = (0, 0, 5016)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5016")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4925"
data_version_tuple = (0, 0, 4925)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4925")
except ImportError:
    pass
data_git_hash = "30d23802d054518738cbaa78393995274d5602ac"
data_git_describe = "v0.0-4925-g30d23802d"
data_git_msg = """\
commit 30d23802d054518738cbaa78393995274d5602ac
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Feb 16 10:11:21 2021 +0100

    [top] Re-align top_englishbreakfast with top_earlgrey
    
    The most prominent changes are:
    - Move pinmux from main crossbar to peripheral crossbar.
    - Re-align instance names (uart -> uart0, add _aon suffixes).
    - Re-align base addresses (ram_ret_aon, usbdev, sensor_ctrl_aon,
      ast_wrapper).
    - Re-align top_englishbreakfast.hjson to ease future diffs.
    
    This resolves lowRISC/OpenTitan#5242.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
