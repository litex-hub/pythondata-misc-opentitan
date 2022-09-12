import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14131"
version_tuple = (0, 0, 14131)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14131")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13989"
data_version_tuple = (0, 0, 13989)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13989")
except ImportError:
    pass
data_git_hash = "14626b98175da2bd514eee989628a5bf9b21c7e5"
data_git_describe = "v0.0-13989-g14626b9817"
data_git_msg = """\
commit 14626b98175da2bd514eee989628a5bf9b21c7e5
Author: Alexander Williams <awill@google.com>
Date:   Wed Aug 31 09:23:03 2022 -0700

    [otp_ctrl/dif] Fix up lock reg handling
    
    Update for regwen change from rw1c to rw0c. Also, use the check trigger
    lock for check triggers and the check lock for check configuration.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
