import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15040"
version_tuple = (0, 0, 15040)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15040")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14898"
data_version_tuple = (0, 0, 14898)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14898")
except ImportError:
    pass
data_git_hash = "e57d7fecfb4dd1607715b5983ab320214744439e"
data_git_describe = "v0.0-14898-ge57d7fecfb"
data_git_msg = """\
commit e57d7fecfb4dd1607715b5983ab320214744439e
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Oct 25 11:26:40 2022 -0700

    [top-level,test] add initial power virus test boilerplate
    
    This adds the boilerplate code for the power virus test to partially
    address #14814. Since this test will be rather large/complex, it will be
    committed in pieces over time. This initial commit contains a basic test
    checklist (that will be added-to/improved over time) and basic
    configurations for the pinmux, gpio, and adc_ctrl peripherals.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
