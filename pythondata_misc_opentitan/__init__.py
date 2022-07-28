import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13312"
version_tuple = (0, 0, 13312)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13312")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13170"
data_version_tuple = (0, 0, 13170)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13170")
except ImportError:
    pass
data_git_hash = "314afa2068a991bdb60e9a42f8c3e2dec39e472c"
data_git_describe = "v0.0-13170-g314afa2068"
data_git_msg = """\
commit 314afa2068a991bdb60e9a42f8c3e2dec39e472c
Author: Michael Schaffner <msf@google.com>
Date:   Wed Jul 27 18:47:57 2022 -0700

    [kmac] Remove outdated comment
    
    As discussed in https://github.com/lowRISC/opentitan/issues/12429#issuecomment-1125258307
    this comment is not actually true, hence it is removed in this commit.
    
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
