import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10980"
version_tuple = (0, 0, 10980)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10980")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10854"
data_version_tuple = (0, 0, 10854)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10854")
except ImportError:
    pass
data_git_hash = "74cf437574da7a5e62d6caba563e38de407cb07c"
data_git_describe = "v0.0-10854-g74cf43757"
data_git_msg = """\
commit 74cf437574da7a5e62d6caba563e38de407cb07c
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 9 13:46:52 2022 -0800

    [hmac] Minor lint fix
    
    - re-code the flop since otherwise it causes a RESET_USE error
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
