import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12460"
version_tuple = (0, 0, 12460)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12460")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12318"
data_version_tuple = (0, 0, 12318)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12318")
except ImportError:
    pass
data_git_hash = "e50daed06c513c52b725e4b650d3e0c1db9cf076"
data_git_describe = "v0.0-12318-ge50daed06"
data_git_msg = """\
commit e50daed06c513c52b725e4b650d3e0c1db9cf076
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue May 31 02:53:14 2022 -0700

    expanding FI to include round counter
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
