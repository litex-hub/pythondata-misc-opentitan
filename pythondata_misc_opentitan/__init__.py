import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14849"
version_tuple = (0, 0, 14849)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14849")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14707"
data_version_tuple = (0, 0, 14707)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14707")
except ImportError:
    pass
data_git_hash = "47a8e09c9b519069615bb32a0c976a92302c9bb8"
data_git_describe = "v0.0-14707-g47a8e09c9b"
data_git_msg = """\
commit 47a8e09c9b519069615bb32a0c976a92302c9bb8
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Tue Oct 18 21:21:10 2022 -0400

    [site] Update lowRISC registered office address
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

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
