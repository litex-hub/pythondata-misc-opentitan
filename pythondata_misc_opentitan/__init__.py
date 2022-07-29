import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13332"
version_tuple = (0, 0, 13332)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13332")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13190"
data_version_tuple = (0, 0, 13190)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13190")
except ImportError:
    pass
data_git_hash = "909424e7e8504c5c7872e3e488bfd5b4628a5005"
data_git_describe = "v0.0-13190-g909424e7e8"
data_git_msg = """\
commit 909424e7e8504c5c7872e3e488bfd5b4628a5005
Author: Weicai Yang <weicai@google.com>
Date:   Thu Jul 28 17:44:54 2022 -0700

    [sram/dv] Fix lc_esc test
    
    lc escalation no longer gates the sram access, update scb for update
    simplify the sequence to avoid driving lc_esc and issue sram access at the same time
    as it's hard to predict due to async timing
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
