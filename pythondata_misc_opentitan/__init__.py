import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11445"
version_tuple = (0, 0, 11445)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11445")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11319"
data_version_tuple = (0, 0, 11319)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11319")
except ImportError:
    pass
data_git_hash = "b670be80eefb83408568167c82c3f2dd255adcdd"
data_git_describe = "v0.0-11319-gb670be80e"
data_git_msg = """\
commit b670be80eefb83408568167c82c3f2dd255adcdd
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Apr 6 21:34:26 2022 -0700

    [lc_ctrl] Add more details to countermeasure testplan
    
    This addresses #11731 and #11919.
    
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
