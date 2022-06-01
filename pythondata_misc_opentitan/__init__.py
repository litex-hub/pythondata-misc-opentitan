import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12432"
version_tuple = (0, 0, 12432)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12432")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12290"
data_version_tuple = (0, 0, 12290)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12290")
except ImportError:
    pass
data_git_hash = "217a0168ba118503c166a9587819e3811eeb0c0c"
data_git_describe = "v0.0-12290-g217a0168b"
data_git_msg = """\
commit 217a0168ba118503c166a9587819e3811eeb0c0c
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue May 31 15:18:17 2022 +0100

    [dif, rv_core_ibex] Add rnd api
    
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
