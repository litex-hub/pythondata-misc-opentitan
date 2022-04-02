import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11313"
version_tuple = (0, 0, 11313)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11313")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11187"
data_version_tuple = (0, 0, 11187)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11187")
except ImportError:
    pass
data_git_hash = "cea8d0b2e37d26f880e26c7127c50b84cce66e32"
data_git_describe = "v0.0-11187-gcea8d0b2e"
data_git_msg = """\
commit cea8d0b2e37d26f880e26c7127c50b84cce66e32
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Mar 25 10:06:44 2022 -0700

    [sensor_ctrl] Bump version to 1.0
    
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
