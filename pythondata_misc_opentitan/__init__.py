import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14191"
version_tuple = (0, 0, 14191)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14191")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14049"
data_version_tuple = (0, 0, 14049)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14049")
except ImportError:
    pass
data_git_hash = "63f72f5423d46526f9611ba98678d2430c52b0b7"
data_git_describe = "v0.0-14049-g63f72f5423"
data_git_msg = """\
commit 63f72f5423d46526f9611ba98678d2430c52b0b7
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Sep 9 18:52:39 2022 -0700

    [top/dv] shorten sensor_ctrl_alert_test
    
    fixes #14844
    
    randomize the events tested each time and increase the number
    of reseeds
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
