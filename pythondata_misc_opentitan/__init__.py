import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9311"
version_tuple = (0, 0, 9311)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9311")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9194"
data_version_tuple = (0, 0, 9194)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9194")
except ImportError:
    pass
data_git_hash = "27685eff1a0dab971c32b94c1f04a53e54442097"
data_git_describe = "v0.0-9194-g27685eff1"
data_git_msg = """\
commit 27685eff1a0dab971c32b94c1f04a53e54442097
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Dec 10 18:58:04 2021 +0000

    [otbn,util] Combine information- and control- flow to analyze OTBN.
    
    Adds analysis tools that construct information-flow graphs for
    subroutines or whole programs.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
