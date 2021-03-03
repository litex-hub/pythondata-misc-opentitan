import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5225"
version_tuple = (0, 0, 5225)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5225")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5134"
data_version_tuple = (0, 0, 5134)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5134")
except ImportError:
    pass
data_git_hash = "11e4d89943abecc79361d3b46d38b0a64cbd5b84"
data_git_describe = "v0.0-5134-g11e4d8994"
data_git_msg = """\
commit 11e4d89943abecc79361d3b46d38b0a64cbd5b84
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Mar 2 12:00:02 2021 -0800

    [otp_ctrl] Always attempt to program all LC words in presence of errors
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
