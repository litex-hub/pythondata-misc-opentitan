import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14114"
version_tuple = (0, 0, 14114)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14114")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13972"
data_version_tuple = (0, 0, 13972)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13972")
except ImportError:
    pass
data_git_hash = "b05a44082aadb68759622caa3d819296a9327042"
data_git_describe = "v0.0-13972-gb05a44082a"
data_git_msg = """\
commit b05a44082aadb68759622caa3d819296a9327042
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Sep 6 09:17:44 2022 -0700

    [chip dv] Replace chip_if with individual interfaces
    
    This commit starts replacing the individual interfaces
    connected to the DUT in tb with the ones in chip_if.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>
    
    [dv, xbar_autogen] Minor update the topgen XBAR template
    
    Create and connect the rst_n wire.
    Use chip_if::clk_rst_if for driving reset in XBAR seqs.
    
    Squashed with chip level pinout commit.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
