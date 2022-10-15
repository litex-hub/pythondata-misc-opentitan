import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14761"
version_tuple = (0, 0, 14761)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14761")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14619"
data_version_tuple = (0, 0, 14619)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14619")
except ImportError:
    pass
data_git_hash = "dcedef98780b50578aaf3a6f71d3491aae14387c"
data_git_describe = "v0.0-14619-gdcedef9878"
data_git_msg = """\
commit dcedef98780b50578aaf3a6f71d3491aae14387c
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Oct 11 16:58:52 2022 -0700

    [dv/top] Add option to automatically set rom_exec_en
    
    - addresses #15371
    - allows a test to automatically set rom_exec_en when apply_reset
      is called.
    
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
