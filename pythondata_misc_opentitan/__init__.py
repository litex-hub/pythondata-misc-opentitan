import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5212"
version_tuple = (0, 0, 5212)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5212")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5121"
data_version_tuple = (0, 0, 5121)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5121")
except ImportError:
    pass
data_git_hash = "69367b391965d542ea600e90efdf7439886d09dc"
data_git_describe = "v0.0-5121-g69367b391"
data_git_msg = """\
commit 69367b391965d542ea600e90efdf7439886d09dc
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Mar 2 09:39:23 2021 -0800

    [dvsim] Add fileset_partner to FuseSoC
    
    This adds the `--fileset_partner` flag to FuseSoC as an example
    to `vendor_chip_sim_cfg_example.hjson`.
    
    By default, the open source implementation is selected (using the
    negation of `fileset_partner` flag). If `fileset_partner` flag is set,
    FuseSoC selects that implementation instead.
    
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
