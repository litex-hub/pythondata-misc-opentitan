import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13049"
version_tuple = (0, 0, 13049)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13049")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12907"
data_version_tuple = (0, 0, 12907)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12907")
except ImportError:
    pass
data_git_hash = "1adf9f1d8ba2fe5f9f85115a1e1fd7964b3bf61b"
data_git_describe = "v0.0-12907-g1adf9f1d8b"
data_git_msg = """\
commit 1adf9f1d8ba2fe5f9f85115a1e1fd7964b3bf61b
Author: Andres Meza <anmeza@ucsd.edu>
Date:   Fri Jun 3 13:33:05 2022 -0700

    [otp_ctrl] Prevent broadcast of scrambler's input/intermediate values
    
    The scrambler broadcasts initial inputs, intermediate scrambling
    results, and final scrambling results to its data output.
    
    This commit adds an additional condition that only enables the final
    scrambling results or a safe default value (as recommended in the OT’s
    Secure Hardware Design Guidelines) to be broadcast to the data output.
    
    Signed-off-by: Andres Meza <anmeza@ucsd.edu>

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
