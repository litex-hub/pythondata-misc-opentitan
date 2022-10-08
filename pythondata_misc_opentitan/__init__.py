import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14630"
version_tuple = (0, 0, 14630)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14630")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14488"
data_version_tuple = (0, 0, 14488)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14488")
except ImportError:
    pass
data_git_hash = "c2a8c64ccbca39707be7883dfd2f8c1100813730"
data_git_describe = "v0.0-14488-gc2a8c64ccb"
data_git_msg = """\
commit c2a8c64ccbca39707be7883dfd2f8c1100813730
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Oct 7 17:55:28 2022 -0700

    [dv/kmac] Masked kmac exclusion checksum update
    
    Due to design changes by adding a state, this PR updates the terminal
    state exclusion checksum and transition values.
    
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
