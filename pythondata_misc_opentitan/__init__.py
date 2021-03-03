import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5226"
version_tuple = (0, 0, 5226)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5226")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5135"
data_version_tuple = (0, 0, 5135)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5135")
except ImportError:
    pass
data_git_hash = "efaa97eb056324fec332981139a3370db290679a"
data_git_describe = "v0.0-5135-gefaa97eb0"
data_git_msg = """\
commit efaa97eb056324fec332981139a3370db290679a
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Mar 2 12:00:02 2021 -0800

    [ast] AscenLint fixes and new analog typedef
    
    Co-authored-by: Jacob Levy <jacob.levy@opentitan.org>
    Signed-off-by: Michael Schaffner <msf@opentitan.org>
    Signed-off-by: Jacob Levy <jacob.levy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
