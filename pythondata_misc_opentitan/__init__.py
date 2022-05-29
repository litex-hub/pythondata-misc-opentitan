import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12401"
version_tuple = (0, 0, 12401)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12401")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12261"
data_version_tuple = (0, 0, 12261)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12261")
except ImportError:
    pass
data_git_hash = "84869a3ca0106b994a80c358d06a2fafc2f5ef18"
data_git_describe = "v0.0-12261-g84869a3ca"
data_git_msg = """\
commit 84869a3ca0106b994a80c358d06a2fafc2f5ef18
Author: Michael Munday <mike.munday@lowrisc.org>
Date:   Fri May 27 16:35:54 2022 +0100

    [COMMITTERS] Update committer list to add Douglas Reis
    
    The Technical Committee has granted committer status to Douglas.
    Congratulations Douglas, thank you for all your hard work on the
    project so far.
    
    Also, remove Miguel Young de la Sota from the COMMITTERS and
    CODEOWNERS lists as he is no longer working on the project. Thanks
    for all your contributions over the years Miguel!
    
    Signed-off-by: Michael Munday <mike.munday@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
