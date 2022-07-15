import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13099"
version_tuple = (0, 0, 13099)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13099")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12957"
data_version_tuple = (0, 0, 12957)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12957")
except ImportError:
    pass
data_git_hash = "db28d6d3b29bd99de8680dbd476ebdc88927186b"
data_git_describe = "v0.0-12957-gdb28d6d3b2"
data_git_msg = """\
commit db28d6d3b29bd99de8680dbd476ebdc88927186b
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Jul 11 15:41:53 2022 -0700

    [top/cw310] Add cw310 to lint
    
    - this lint is mainly for integration checking, as it is as
      assumed that top_earlgrey lint is done separately and that
      ast also behaves correctly.
    
    - we've been bitten multiple times by integration mistakes
      that manifest as FPGA test failures, so hopefully this will
      help us address some of the low hanging fruits.
    
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
