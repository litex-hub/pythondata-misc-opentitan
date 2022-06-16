import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12714"
version_tuple = (0, 0, 12714)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12714")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12572"
data_version_tuple = (0, 0, 12572)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12572")
except ImportError:
    pass
data_git_hash = "5123a71ac14d869cfa60e442cdd5c103278330e8"
data_git_describe = "v0.0-12572-g5123a71ac"
data_git_msg = """\
commit 5123a71ac14d869cfa60e442cdd5c103278330e8
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Jun 15 00:23:56 2022 -0700

    [dv/clkmgr] Fix trans test
    
    Check with SVA whether the transactional clocks are running.
    Add some extra wait cycles prior to reading hint_status to account
    for idle count and synchronization.
    Some trivial formatting changes for verible.
    
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
