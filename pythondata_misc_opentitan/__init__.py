import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5857"
version_tuple = (0, 0, 5857)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5857")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5762"
data_version_tuple = (0, 0, 5762)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5762")
except ImportError:
    pass
data_git_hash = "071e62a3a221357a033dec34f5854958f1f2b91e"
data_git_describe = "v0.0-5762-g071e62a3a"
data_git_msg = """\
commit 071e62a3a221357a033dec34f5854958f1f2b91e
Author: Weicai Yang <weicai@google.com>
Date:   Mon Apr 12 18:14:22 2021 -0700

    [dv] Update tl_agent to not always allow abort a_valid
    
    Most likely our host won't abort a_valid. Don't always allow abort, so
    that if device doesn't respond, let it hang rather than abort and re-send
    request
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
