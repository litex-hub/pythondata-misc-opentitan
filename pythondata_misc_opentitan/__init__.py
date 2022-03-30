import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11212"
version_tuple = (0, 0, 11212)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11212")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11086"
data_version_tuple = (0, 0, 11086)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11086")
except ImportError:
    pass
data_git_hash = "bcc253584a7c105cbf5231846fdf3fed4c000597"
data_git_describe = "v0.0-11086-gbcc253584"
data_git_msg = """\
commit bcc253584a7c105cbf5231846fdf3fed4c000597
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Mar 25 22:29:57 2022 -0700

    [doc] Expand the sec_cm_dv_framework documentation
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
