import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14739"
version_tuple = (0, 0, 14739)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14739")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14597"
data_version_tuple = (0, 0, 14597)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14597")
except ImportError:
    pass
data_git_hash = "b3f3b128c77846c8cd3d094f51138d9ebc1e0423"
data_git_describe = "v0.0-14597-gb3f3b128c7"
data_git_msg = """\
commit b3f3b128c77846c8cd3d094f51138d9ebc1e0423
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Oct 12 11:31:03 2022 -0700

    [dv,chip] Add chip_sw_random_sleep_all_wake_ups
    
    Fixes #14166
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
