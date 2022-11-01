import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15088"
version_tuple = (0, 0, 15088)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15088")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14946"
data_version_tuple = (0, 0, 14946)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14946")
except ImportError:
    pass
data_git_hash = "0871f2865370a2ab572448115f4d4ecb7758b391"
data_git_describe = "v0.0-14946-g0871f28653"
data_git_msg = """\
commit 0871f2865370a2ab572448115f4d4ecb7758b391
Author: Miles Dai <milesdai@google.com>
Date:   Wed Oct 19 14:56:31 2022 -0400

    [test] Add shutdown redaction tests
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
