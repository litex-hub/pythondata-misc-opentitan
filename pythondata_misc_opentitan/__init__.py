import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12711"
version_tuple = (0, 0, 12711)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12711")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12569"
data_version_tuple = (0, 0, 12569)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12569")
except ImportError:
    pass
data_git_hash = "12e9c1b5ef3ded27a76c7ae9567f2688f0902226"
data_git_describe = "v0.0-12569-g12e9c1b5e"
data_git_msg = """\
commit 12e9c1b5ef3ded27a76c7ae9567f2688f0902226
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon Jun 13 15:28:18 2022 +0000

    [dv,flash_ctrl] Add stress_all test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
