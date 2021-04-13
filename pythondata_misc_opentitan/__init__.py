import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5850"
version_tuple = (0, 0, 5850)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5850")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5755"
data_version_tuple = (0, 0, 5755)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5755")
except ImportError:
    pass
data_git_hash = "ca40353361b0bcc80c7b6f4f93e0b6a0c0f0213b"
data_git_describe = "v0.0-5755-gca4035336"
data_git_msg = """\
commit ca40353361b0bcc80c7b6f4f93e0b6a0c0f0213b
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Tue Apr 13 09:15:28 2021 +0100

    Update to rebuilt device toolchain
    
    The previously used toolchain in version 20200904-1 was targeting Ubuntu
    16.04 or RHEL7 and newer. The version this commit switches to targets
    RHEL6/CentOS6 or newer.
    
    Beyond a rebuild to be more compatible with older Linux distributions
    nothing changed: the toolchain contains the same versions of GCC, clang,
    and all associated tools.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
