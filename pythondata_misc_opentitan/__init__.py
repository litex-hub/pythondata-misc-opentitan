import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12723"
version_tuple = (0, 0, 12723)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12723")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12581"
data_version_tuple = (0, 0, 12581)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12581")
except ImportError:
    pass
data_git_hash = "89d481f1d745d410de26f2fd3bddef9a80403943"
data_git_describe = "v0.0-12581-g89d481f1d"
data_git_msg = """\
commit 89d481f1d745d410de26f2fd3bddef9a80403943
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Jun 15 13:47:25 2022 -0700

    [dv,rstmgr] Fix some sec_cm test failures
    
    Update the list of rstmgr_leaf_rst instances for design changes.
    Add some messages in check failures for ease of diagnostics.
    Formatting changes for verible.
    
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
