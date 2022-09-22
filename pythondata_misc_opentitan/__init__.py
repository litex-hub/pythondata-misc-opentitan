import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14384"
version_tuple = (0, 0, 14384)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14384")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14242"
data_version_tuple = (0, 0, 14242)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14242")
except ImportError:
    pass
data_git_hash = "468e69c56f627c66b7fe44b07ac43057afe22d25"
data_git_describe = "v0.0-14242-g468e69c56f"
data_git_msg = """\
commit 468e69c56f627c66b7fe44b07ac43057afe22d25
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Tue Sep 20 22:24:03 2022 +0000

    [flash_ctr,dv] Add more v2s tests
    
    - Add local escalation test
    - Update test plan with auto_gen csr tests for regwen and shadow
    - Remove unused arg from otf_direct_read
    - Add ctrl only option to random op send
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
