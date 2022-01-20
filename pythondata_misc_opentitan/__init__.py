import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9653"
version_tuple = (0, 0, 9653)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9653")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9531"
data_version_tuple = (0, 0, 9531)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9531")
except ImportError:
    pass
data_git_hash = "46f9bb4a35d6594489ab1992babbfb8dfb24508f"
data_git_describe = "v0.0-9531-g46f9bb4a3"
data_git_msg = """\
commit 46f9bb4a35d6594489ab1992babbfb8dfb24508f
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Thu Jan 6 13:24:54 2022 -0800

    [csrng/dv] Updated testplan, Added cfg cover group
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
