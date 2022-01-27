import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9840"
version_tuple = (0, 0, 9840)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9840")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9718"
data_version_tuple = (0, 0, 9718)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9718")
except ImportError:
    pass
data_git_hash = "a5d6d35cc265b5a0e0903fbf32f8df8bd1b7e4d4"
data_git_describe = "v0.0-9718-ga5d6d35cc"
data_git_msg = """\
commit a5d6d35cc265b5a0e0903fbf32f8df8bd1b7e4d4
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Jan 26 14:06:06 2022 -0500

    [sw/silicon_creator] Generate an exception if USE_SW_RSA OTP value is invalid
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
