import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13052"
version_tuple = (0, 0, 13052)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13052")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12910"
data_version_tuple = (0, 0, 12910)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12910")
except ImportError:
    pass
data_git_hash = "34d4c8c424c3e666a667280d60e6c1a23f68ae05"
data_git_describe = "v0.0-12910-g34d4c8c424"
data_git_msg = """\
commit 34d4c8c424c3e666a667280d60e6c1a23f68ae05
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Fri Jul 8 13:25:04 2022 +0100

    [test, hmac] Merge the tests `hmac_enc` and `hmac_irq`
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
