import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8830"
version_tuple = (0, 0, 8830)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8830")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8718"
data_version_tuple = (0, 0, 8718)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8718")
except ImportError:
    pass
data_git_hash = "f975e54dd1fd411b2eb0bcf9eea473d9c453c264"
data_git_describe = "v0.0-8718-gf975e54dd"
data_git_msg = """\
commit f975e54dd1fd411b2eb0bcf9eea473d9c453c264
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Thu Nov 18 13:23:37 2021 +0000

    [sca] Use the function dif_edn_stop on the sca module
    
    FIX #5465
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
