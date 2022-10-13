import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14723"
version_tuple = (0, 0, 14723)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14723")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14581"
data_version_tuple = (0, 0, 14581)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14581")
except ImportError:
    pass
data_git_hash = "9d8916eaf5d016131f2f30e93e61b606abc7ef3b"
data_git_describe = "v0.0-14581-g9d8916eaf5"
data_git_msg = """\
commit 9d8916eaf5d016131f2f30e93e61b606abc7ef3b
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 12 14:26:49 2022 -0700

    [ci] add Xcelium DV tests to private CI
    
    This increases the number of Xcelium top-level DV tests run in private
    CI.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
