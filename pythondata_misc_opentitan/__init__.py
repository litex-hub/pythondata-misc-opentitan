import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9598"
version_tuple = (0, 0, 9598)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9598")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9476"
data_version_tuple = (0, 0, 9476)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9476")
except ImportError:
    pass
data_git_hash = "95be8e6722ed33dbcfc8757d7e06734af168f1f5"
data_git_describe = "v0.0-9476-g95be8e672"
data_git_msg = """\
commit 95be8e6722ed33dbcfc8757d7e06734af168f1f5
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Jan 14 18:11:43 2022 -0800

    [dif/alert_handler] Add X macros to simplify DIF code.
    
    The alert handler has a list of classes and local alerts that are
    converted to enums, that are used in several case statement. This commit
    adds X macros to improve the maintainability (in the case that the
    hardware changes and additional local alerts or classes are added), and
    readability of the alert handler DIF code.
    
    This commit was added in response to a review comment in #10040.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
