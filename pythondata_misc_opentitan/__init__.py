import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12486"
version_tuple = (0, 0, 12486)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12486")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12344"
data_version_tuple = (0, 0, 12344)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12344")
except ImportError:
    pass
data_git_hash = "b83afe85e411b68cd10da9f265994eede6597b78"
data_git_describe = "v0.0-12344-gb83afe85e"
data_git_msg = """\
commit b83afe85e411b68cd10da9f265994eede6597b78
Author: Michael Schaffner <msf@opentitan.org>
Date:   Thu Jun 2 12:47:43 2022 +0200

    [otbn] Minor lint fix
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
