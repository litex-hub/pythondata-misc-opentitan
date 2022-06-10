import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12638"
version_tuple = (0, 0, 12638)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12638")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12496"
data_version_tuple = (0, 0, 12496)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12496")
except ImportError:
    pass
data_git_hash = "a83bf2d5807a8841599e7643e40c849b89d59fef"
data_git_describe = "v0.0-12496-ga83bf2d58"
data_git_msg = """\
commit a83bf2d5807a8841599e7643e40c849b89d59fef
Author: Viswanadha Bazawada <viswanadha.bazawada@ensilica.com>
Date:   Thu May 26 09:44:25 2022 +0100

    [I2C/DV] I2c Agent Driver Host Mode Tasks
    
    - Added Interface Tasks Host Start Stop RStart Data And Nack
    - Added Tasks To Drive Host Item I2C Driver
    
    Signed-off-by: Viswanadha Bazawada <viswanadha.bazawada@ensilica.com>

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
