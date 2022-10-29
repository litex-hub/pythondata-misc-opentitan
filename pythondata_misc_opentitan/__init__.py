import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15038"
version_tuple = (0, 0, 15038)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15038")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14896"
data_version_tuple = (0, 0, 14896)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14896")
except ImportError:
    pass
data_git_hash = "d08861804d912f28b37443ccaa249e1f61e28a91"
data_git_describe = "v0.0-14896-gd08861804d"
data_git_msg = """\
commit d08861804d912f28b37443ccaa249e1f61e28a91
Author: Michael Schaffner <msf@google.com>
Date:   Fri Oct 28 16:19:21 2022 -0700

    [tlul] Add comment regarding refactor to tlul_adapter_reg
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
