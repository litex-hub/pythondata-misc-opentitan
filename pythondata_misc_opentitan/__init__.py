import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14569"
version_tuple = (0, 0, 14569)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14569")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14427"
data_version_tuple = (0, 0, 14427)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14427")
except ImportError:
    pass
data_git_hash = "cf36305f59649e5ebd9c7d023dd34df4c80b7cd8"
data_git_describe = "v0.0-14427-gcf36305f59"
data_git_msg = """\
commit cf36305f59649e5ebd9c7d023dd34df4c80b7cd8
Author: Miles Dai <milesdai@google.com>
Date:   Mon Oct 3 13:18:09 2022 -0400

    [lint] Fix buildifier linting issues
    
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
