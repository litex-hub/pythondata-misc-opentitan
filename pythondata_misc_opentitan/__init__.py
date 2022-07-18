import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13152"
version_tuple = (0, 0, 13152)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13152")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13010"
data_version_tuple = (0, 0, 13010)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13010")
except ImportError:
    pass
data_git_hash = "b661fb6b73d30758e1c893bdc49e55ec44ac7401"
data_git_describe = "v0.0-13010-gb661fb6b73"
data_git_msg = """\
commit b661fb6b73d30758e1c893bdc49e55ec44ac7401
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Jul 15 19:04:00 2022 -0700

    [sw/dif] Add a dif function to grab current state
    
    - add a testutil function to wait until a certain entropy state
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    fix
    
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
