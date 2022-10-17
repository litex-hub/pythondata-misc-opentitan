import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14783"
version_tuple = (0, 0, 14783)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14783")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14641"
data_version_tuple = (0, 0, 14641)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14641")
except ImportError:
    pass
data_git_hash = "f8c9972ec1c6f1e7365fa2b7321e4444f535cd5e"
data_git_describe = "v0.0-14641-gf8c9972ec1"
data_git_msg = """\
commit f8c9972ec1c6f1e7365fa2b7321e4444f535cd5e
Author: Eli Kim <eli@opentitan.org>
Date:   Thu Oct 13 16:17:16 2022 -0700

    refactor(spid): Remove unused mailbox_hit port
    
    Passthrough logic has `mailbox_hit_i` port to filter the read command
    hitting the mailbox space. However, that function is deprecated and the
    HW allows a Read command to cross the mailbox region and the
    passthrough.
    
    So, `intercept` data structure has `mbx` field to change the mux from
    Passthrough to internal datapath. While implementing the intercept, the
    `mailbox_hit_i` port supposes to be removed but tied.
    
    Issue has been reported by @weicaiyang
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
