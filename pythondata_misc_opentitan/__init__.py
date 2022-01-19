import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9623"
version_tuple = (0, 0, 9623)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9623")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9501"
data_version_tuple = (0, 0, 9501)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9501")
except ImportError:
    pass
data_git_hash = "610e719dc85413520501a0aac552df1d6e1cc34d"
data_git_describe = "v0.0-9501-g610e719dc"
data_git_msg = """\
commit 610e719dc85413520501a0aac552df1d6e1cc34d
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue Jan 18 14:46:27 2022 +0000

    [sw,tests] Add the chip level test `chip_sw_aon_timer_sleep_wdog_bite_reset`
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
