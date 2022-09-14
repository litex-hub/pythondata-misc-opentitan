import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14180"
version_tuple = (0, 0, 14180)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14180")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14038"
data_version_tuple = (0, 0, 14038)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14038")
except ImportError:
    pass
data_git_hash = "bf9bd4a1f1cbd0a2ba7645106df7e1dea5e2a678"
data_git_describe = "v0.0-14038-gbf9bd4a1f1"
data_git_msg = """\
commit bf9bd4a1f1cbd0a2ba7645106df7e1dea5e2a678
Author: Weicai Yang <weicai@google.com>
Date:   Tue Sep 13 11:53:15 2022 -0700

    [chip, dv] Fix chip_sw_keymgr_key_derivation
    
    Addressed #14835
    fixed SW and SV key version mismatch
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
