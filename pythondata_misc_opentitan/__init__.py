import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10138"
version_tuple = (0, 0, 10138)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10138")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10014"
data_version_tuple = (0, 0, 10014)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10014")
except ImportError:
    pass
data_git_hash = "e76d655047f596d7ba11c89ffb5ff83b7f356bc4"
data_git_describe = "v0.0-10014-ge76d65504"
data_git_msg = """\
commit e76d655047f596d7ba11c89ffb5ff83b7f356bc4
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Feb 7 15:20:50 2022 -0800

    [lc_ctrl, dv] Add lc_ctrl_jtag_smoke to smoke regr
    
    This PR adds LC ctrl JTAG smoke test to the smoke suite run in CI. The
    reason for this addition is to ensure changes to the JTAG agent which is
    shared with other testbenches do not break the LC ctrl testbench.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
