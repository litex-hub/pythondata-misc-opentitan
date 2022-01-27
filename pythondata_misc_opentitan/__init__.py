import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9847"
version_tuple = (0, 0, 9847)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9847")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9723"
data_version_tuple = (0, 0, 9723)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9723")
except ImportError:
    pass
data_git_hash = "79d1e7a4d3e48a817ffa7a5eaa28b07e16969bf0"
data_git_describe = "v0.0-9723-g79d1e7a4d"
data_git_msg = """\
commit 79d1e7a4d3e48a817ffa7a5eaa28b07e16969bf0
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Jan 24 23:48:35 2022 -0800

    [dif/alert_handler] Add static asserts for multireg layouts.
    
    Several CSRs for both alerts and local alerts are organized as
    multiregs, enabling easy DIF development. However, there is currently no
    mechanism to indicate of the multireg layout of said CSRs ever changes.
    This commit adds static asserts to check these multireg layouts.
    
    This partially addresses a task in #9899.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
