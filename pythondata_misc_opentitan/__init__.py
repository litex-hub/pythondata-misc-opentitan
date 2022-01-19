import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9619"
version_tuple = (0, 0, 9619)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9619")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9497"
data_version_tuple = (0, 0, 9497)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9497")
except ImportError:
    pass
data_git_hash = "998c9bf6deb9ac91d496ba0536a5e3cb0b5200eb"
data_git_describe = "v0.0-9497-g998c9bf6d"
data_git_msg = """\
commit 998c9bf6deb9ac91d496ba0536a5e3cb0b5200eb
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Jan 18 14:55:30 2022 -0800

    [dv/clkmgr] Add SVA for cg_en_o outputs
    
    Add code to disable exclusions from clkmgr.hjson for IP testing, since
    they are intended for full chip tests.
    - Don't call that code since there are unexpected side-effects from
    exclusion management.
    Also minor fix in clkmgr_bind.
    
    Fixes #9946
    
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
