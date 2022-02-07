import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10096"
version_tuple = (0, 0, 10096)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10096")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9972"
data_version_tuple = (0, 0, 9972)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9972")
except ImportError:
    pass
data_git_hash = "f8391443973820b26e9cdca77a569b7ff5e5b12a"
data_git_describe = "v0.0-9972-gf83914439"
data_git_msg = """\
commit f8391443973820b26e9cdca77a569b7ff5e5b12a
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Sun Feb 6 10:35:02 2022 -0800

    [aes/dv] added nist vectors to testplan
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
