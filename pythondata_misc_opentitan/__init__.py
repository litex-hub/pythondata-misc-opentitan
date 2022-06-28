import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12866"
version_tuple = (0, 0, 12866)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12866")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12724"
data_version_tuple = (0, 0, 12724)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12724")
except ImportError:
    pass
data_git_hash = "9b6225e63885b551f432a6f89189f9f4383e09ce"
data_git_describe = "v0.0-12724-g9b6225e638"
data_git_msg = """\
commit 9b6225e63885b551f432a6f89189f9f4383e09ce
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Wed Jun 22 16:03:30 2022 +0100

    [otbn, dv] Maps testcases to V2S countermeasures
    
    This commit maps existing testcases to V"S countermeasures
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
