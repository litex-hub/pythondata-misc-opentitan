import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9500"
version_tuple = (0, 0, 9500)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9500")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9382"
data_version_tuple = (0, 0, 9382)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9382")
except ImportError:
    pass
data_git_hash = "f8e2a738f7ec6e6259b0a9934732af20fd100c81"
data_git_describe = "v0.0-9382-gf8e2a738f"
data_git_msg = """\
commit f8e2a738f7ec6e6259b0a9934732af20fd100c81
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Mon Jan 10 10:48:14 2022 +0000

    [sw,tests] Add the chip level test `chip_sw_aon_timer_wakeup_irq`
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
