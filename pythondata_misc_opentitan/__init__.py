import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5823"
version_tuple = (0, 0, 5823)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5823")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5728"
data_version_tuple = (0, 0, 5728)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5728")
except ImportError:
    pass
data_git_hash = "c1227938a29e89417ac2aabcf1ce86cffe754872"
data_git_describe = "v0.0-5728-gc1227938a"
data_git_msg = """\
commit c1227938a29e89417ac2aabcf1ce86cffe754872
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sun Nov 15 21:18:59 2020 -0800

    [ pwm, rtl ] Initial implementation for PWM
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
