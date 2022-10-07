import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14626"
version_tuple = (0, 0, 14626)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14626")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14484"
data_version_tuple = (0, 0, 14484)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14484")
except ImportError:
    pass
data_git_hash = "760a0b635e060d1b7a2087aede139fca9bd6da98"
data_git_describe = "v0.0-14484-g760a0b635e"
data_git_msg = """\
commit 760a0b635e060d1b7a2087aede139fca9bd6da98
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Oct 7 12:31:12 2022 -0700

    [dv/chip] Remove uart agent coverage in chip level
    
    Branch from PR #15325, this PR skips creating the uart agent functional
    coverage for chip level testing.
    Thanks @sri and @weicai for the suggetions!
    
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
