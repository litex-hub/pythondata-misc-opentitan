import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12961"
version_tuple = (0, 0, 12961)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12961")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12819"
data_version_tuple = (0, 0, 12819)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12819")
except ImportError:
    pass
data_git_hash = "644a2f9edb1b70c959499938ab8ea6343945dc99"
data_git_describe = "v0.0-12819-g644a2f9edb"
data_git_msg = """\
commit 644a2f9edb1b70c959499938ab8ea6343945dc99
Author: Drew Macrae <drewmacrae@google.com>
Date:   Thu Jun 30 14:33:24 2022 -0400

    [ci] isolate check-generated.sh from previous corruption of repo
    
    If we reorder jobs we can find the first step of this test is sensitive
    to the state of the git repo and can fail. by cleaning up before we run
    it will become more reliable.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
