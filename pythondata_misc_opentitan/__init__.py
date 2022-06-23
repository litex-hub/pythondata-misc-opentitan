import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12817"
version_tuple = (0, 0, 12817)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12817")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12675"
data_version_tuple = (0, 0, 12675)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12675")
except ImportError:
    pass
data_git_hash = "261fab5ec4e62d5ef7b83bb870631d233c2eebf5"
data_git_describe = "v0.0-12675-g261fab5ec4"
data_git_msg = """\
commit 261fab5ec4e62d5ef7b83bb870631d233c2eebf5
Author: Weicai Yang <weicai@google.com>
Date:   Tue Jun 21 13:49:19 2022 -0700

    [chip, dv] Fix keymgr_key_derivation build error
    
    also rename `keymgr_key_derivation` to `keymgr_key_derivation_test` so
    that it's aligned with other tests
    
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
