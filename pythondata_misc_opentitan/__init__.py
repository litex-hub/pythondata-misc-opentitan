import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11519"
version_tuple = (0, 0, 11519)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11519")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11393"
data_version_tuple = (0, 0, 11393)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11393")
except ImportError:
    pass
data_git_hash = "3dc8bdded961c577da61135ff38c45900f268c62"
data_git_describe = "v0.0-11393-g3dc8bdded"
data_git_msg = """\
commit 3dc8bdded961c577da61135ff38c45900f268c62
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Apr 11 16:54:20 2022 +0100

    [kmac_app_agent] Support hosts that don't spot constant shares
    
    This code was originally designed for keymgr, which has a check to
    make sure that no share is all zeros or all ones. The ROM controller
    doesn't have such a check, so we need to tweak the agent slightly.
    
    Without this change, setting err_rsp_pct to 100 in the config might
    still result in a KMAC response whose rsp_error field is zero.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
