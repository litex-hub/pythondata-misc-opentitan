import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9645"
version_tuple = (0, 0, 9645)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9645")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9523"
data_version_tuple = (0, 0, 9523)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9523")
except ImportError:
    pass
data_git_hash = "2a0f1efbbae9f38cf6e601ff5b06d56cbb9638a3"
data_git_describe = "v0.0-9523-g2a0f1efbb"
data_git_msg = """\
commit 2a0f1efbbae9f38cf6e601ff5b06d56cbb9638a3
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jan 18 23:20:48 2022 -0800

    [dv/clkmgr] Declare V2
    
    The action items from the clkmgr v2 review are taken care of, except
    the following:
    - Disable exclusions related to full chip: I coded disabling these
      exclusions and found many common csr tests failing because of
      other missing exclusions. It seems due to a bug in exclusion management.
    - Fix missing coverage in prim_mubi4_sync: I can take care of this once
      the UNR flow is up, and the missing coverage is obviously unreachable.
    - Add a test that holds the clock and then releases. It seems unnecessary,
      since nothing new will really be tested.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
