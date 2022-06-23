import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12798"
version_tuple = (0, 0, 12798)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12798")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12656"
data_version_tuple = (0, 0, 12656)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12656")
except ImportError:
    pass
data_git_hash = "0799e400076f71fdcdab19bbb0da27240c8e5b83"
data_git_describe = "v0.0-12656-g0799e40007"
data_git_msg = """\
commit 0799e400076f71fdcdab19bbb0da27240c8e5b83
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Jun 22 15:30:16 2022 -0400

    [sw/silicon_creator] Move gp init earlier to eliminate several jalr instructions
    
    This improves our resistance to FI since `jal` instructions use an
    immediate while `jalr` instructions use an additional register which can
    also be attacked.
    
    This commit also removes the line that resets `gp` (`x3`) to 0 since
    `gp` is initialized earlier now.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
