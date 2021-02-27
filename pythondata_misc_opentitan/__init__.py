import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5171"
version_tuple = (0, 0, 5171)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5171")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5080"
data_version_tuple = (0, 0, 5080)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5080")
except ImportError:
    pass
data_git_hash = "64b6d9b7c0143aeeccabb53cf3a3e173962215f4"
data_git_describe = "v0.0-5080-g64b6d9b7c"
data_git_msg = """\
commit 64b6d9b7c0143aeeccabb53cf3a3e173962215f4
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Feb 10 22:02:47 2021 -0800

    [dvsim] Alphabetize top_earlgrey_sim_cfgs.hjson
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
