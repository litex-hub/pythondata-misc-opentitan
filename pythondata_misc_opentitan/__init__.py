import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12859"
version_tuple = (0, 0, 12859)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12859")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12717"
data_version_tuple = (0, 0, 12717)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12717")
except ImportError:
    pass
data_git_hash = "e248e9403c2643fa921d75639510020a2d0c2bde"
data_git_describe = "v0.0-12717-ge248e9403c"
data_git_msg = """\
commit e248e9403c2643fa921d75639510020a2d0c2bde
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Mon Jun 27 20:46:07 2022 +0000

    [flash_ctrl,dv] non-otf timeout fix
    
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
