import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14766"
version_tuple = (0, 0, 14766)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14766")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14624"
data_version_tuple = (0, 0, 14624)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14624")
except ImportError:
    pass
data_git_hash = "c5f7bfefb64eee68205111b5b7abff7f086a4e0d"
data_git_describe = "v0.0-14624-gc5f7bfefb6"
data_git_msg = """\
commit c5f7bfefb64eee68205111b5b7abff7f086a4e0d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Oct 14 16:17:10 2022 -0700

    [dv/otp_ctrl] Fix scb X value
    
    This PR fixes scb X value because I missed the part to assign the value
    from interface.
    Thanks Sri for finding these.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
