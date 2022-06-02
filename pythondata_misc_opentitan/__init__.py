import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12458"
version_tuple = (0, 0, 12458)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12458")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12316"
data_version_tuple = (0, 0, 12316)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12316")
except ImportError:
    pass
data_git_hash = "39634e0e1ad9ab125464cc8a626328f13df23b15"
data_git_describe = "v0.0-12316-g39634e0e1"
data_git_msg = """\
commit 39634e0e1ad9ab125464cc8a626328f13df23b15
Author: Guillermo Maturana <maturana@google.com>
Date:   Tue Mar 15 17:20:37 2022 -0700

    [dv/rstmgr] Disable unnecessary exclusions
    
    Disable CSR exclusions meant for full-chip only.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
