import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14811"
version_tuple = (0, 0, 14811)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14811")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14669"
data_version_tuple = (0, 0, 14669)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14669")
except ImportError:
    pass
data_git_hash = "9ca43a9f2dbfa676a6c5b38857eb024704bafe65"
data_git_describe = "v0.0-14669-g9ca43a9f2d"
data_git_msg = """\
commit 9ca43a9f2dbfa676a6c5b38857eb024704bafe65
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Oct 18 10:50:43 2022 -0700

    [dv/jtag_riscv_agent] Fix rv_dm activation error
    
    This PR fixes the nightly regression failure due to rv_dm activation
    failure.
    Because rv_dm activation consists a series of steps, so initially I
    forget to assign the final status to return to the activation sequence.
    This error is caught by `DV_CHECK` macro updates.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
