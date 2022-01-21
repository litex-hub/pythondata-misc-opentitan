import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9687"
version_tuple = (0, 0, 9687)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9687")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9565"
data_version_tuple = (0, 0, 9565)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9565")
except ImportError:
    pass
data_git_hash = "dce6eb7ea9e842b76e90e2360776bc17a7214f22"
data_git_describe = "v0.0-9565-gdce6eb7ea"
data_git_msg = """\
commit dce6eb7ea9e842b76e90e2360776bc17a7214f22
Author: Daniel Beitel <dbeitel@rivosinc.com>
Date:   Wed Jan 19 13:18:05 2022 -0800

    [sw,mask_rom] Rename manifest.S so it doesn't collide with manifest.c rule
    
    Signed-off-by: Daniel Beitel <dbeitel@rivosinc.com>

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
