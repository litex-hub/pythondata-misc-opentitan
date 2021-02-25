import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5143"
version_tuple = (0, 0, 5143)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5143")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5052"
data_version_tuple = (0, 0, 5052)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5052")
except ImportError:
    pass
data_git_hash = "d34bf23e5c3dc80a50acc213dfa82f6dba6f487e"
data_git_describe = "v0.0-5052-gd34bf23e5"
data_git_msg = """\
commit d34bf23e5c3dc80a50acc213dfa82f6dba6f487e
Author: Weicai Yang <weicai@google.com>
Date:   Wed Feb 24 14:39:24 2021 -0800

    [keymgr/dv] Add invalid cmd/fsm vseq
    
    force design internal signal cmd/fsm to trigger fault error
    disable scb in this seq as kmac transaction may be terminated earlier
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
