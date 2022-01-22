import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9713"
version_tuple = (0, 0, 9713)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9713")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9591"
data_version_tuple = (0, 0, 9591)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9591")
except ImportError:
    pass
data_git_hash = "1e47333bb2ff22b05be24cb8068cc9e4de764f9a"
data_git_describe = "v0.0-9591-g1e47333bb"
data_git_msg = """\
commit 1e47333bb2ff22b05be24cb8068cc9e4de764f9a
Author: Guillermo Maturana <maturana@google.com>
Date:   Fri Jan 21 17:25:23 2022 -0800

    [dv/pwrmgr] Fix SVA assertion for spec changes
    
    Expect all clocks off in deep sleep.
    
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
