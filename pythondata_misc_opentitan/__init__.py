import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5158"
version_tuple = (0, 0, 5158)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5158")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5067"
data_version_tuple = (0, 0, 5067)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5067")
except ImportError:
    pass
data_git_hash = "d55bc6cd71c30f6027cb3b90cde5ef27f5ed3eba"
data_git_describe = "v0.0-5067-gd55bc6cd7"
data_git_msg = """\
commit d55bc6cd71c30f6027cb3b90cde5ef27f5ed3eba
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Fri Feb 26 12:24:44 2021 +0000

    [sw, dif] Fix spelling of 'occurred' in all DIFs and template
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
