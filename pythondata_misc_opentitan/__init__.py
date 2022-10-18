import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14791"
version_tuple = (0, 0, 14791)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14791")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14649"
data_version_tuple = (0, 0, 14649)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14649")
except ImportError:
    pass
data_git_hash = "d336486bcfc32a009f8f20d621c6ceac930ffdd9"
data_git_describe = "v0.0-14649-gd336486bcf"
data_git_msg = """\
commit d336486bcfc32a009f8f20d621c6ceac930ffdd9
Author: Michael Schaffner <msf@google.com>
Date:   Mon Oct 17 15:32:10 2022 -0700

    [test] Increase SW timeout for ping_timeout test
    
    This is a fix for addressing #15280.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
