import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14705"
version_tuple = (0, 0, 14705)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14705")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14563"
data_version_tuple = (0, 0, 14563)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14563")
except ImportError:
    pass
data_git_hash = "d19d492fcac39fe201469b3935c9cb11c979d5a9"
data_git_describe = "v0.0-14563-gd19d492fca"
data_git_msg = """\
commit d19d492fcac39fe201469b3935c9cb11c979d5a9
Author: Ziv Hershman <ziv.hershman@nuvoton.com>
Date:   Wed Oct 12 14:24:19 2022 +0300

    [ast] update doc
    
    Signed-off-by: Ziv Hershman <ziv.hershman@nuvoton.com>

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
