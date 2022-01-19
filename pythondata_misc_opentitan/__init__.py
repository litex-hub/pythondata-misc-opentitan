import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9640"
version_tuple = (0, 0, 9640)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9640")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9518"
data_version_tuple = (0, 0, 9518)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9518")
except ImportError:
    pass
data_git_hash = "87b2e32abcc9bd9ab5b0e4a1ff3c07de7b17c1f1"
data_git_describe = "v0.0-9518-g87b2e32ab"
data_git_msg = """\
commit 87b2e32abcc9bd9ab5b0e4a1ff3c07de7b17c1f1
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Jan 19 09:37:43 2022 -0800

    [dv/lc_ctrl] Fix jtag_map related failure
    
    This PR fixes jtag_map null failure by adding a runtime switch.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
