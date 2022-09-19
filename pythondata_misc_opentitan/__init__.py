import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14292"
version_tuple = (0, 0, 14292)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14292")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14150"
data_version_tuple = (0, 0, 14150)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14150")
except ImportError:
    pass
data_git_hash = "b2267c8b3b30662107ce189ce6455973fe766034"
data_git_describe = "v0.0-14150-gb2267c8b3b"
data_git_msg = """\
commit b2267c8b3b30662107ce189ce6455973fe766034
Author: Eli Kim <eli@opentitan.org>
Date:   Thu Sep 15 16:50:58 2022 -0700

    feat(chip): PINMUX Retention mode configuration
    
    This commit adds a test code configuring the PAD retention modes in
    PINMUX in `chip_sw_sleep_pin_mio_dio_val` test.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
