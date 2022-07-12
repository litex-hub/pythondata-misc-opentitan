import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13028"
version_tuple = (0, 0, 13028)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13028")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12886"
data_version_tuple = (0, 0, 12886)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12886")
except ImportError:
    pass
data_git_hash = "85bb174a344bdc725fecb981c370c1af799a61a7"
data_git_describe = "v0.0-12886-g85bb174a34"
data_git_msg = """\
commit 85bb174a344bdc725fecb981c370c1af799a61a7
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Jun 24 17:27:18 2022 -0700

    [flash_ctrl] Minor tweak of arbitration behavior
    
    - make the arbitration count 5
    - only select new fill buffer when there is no match on request
    
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
