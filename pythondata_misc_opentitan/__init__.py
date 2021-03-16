import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5397"
version_tuple = (0, 0, 5397)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5397")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5302"
data_version_tuple = (0, 0, 5302)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5302")
except ImportError:
    pass
data_git_hash = "c5faffb268237a3f08515d0845d6652c27765dfa"
data_git_describe = "v0.0-5302-gc5faffb26"
data_git_msg = """\
commit c5faffb268237a3f08515d0845d6652c27765dfa
Author: Cindy Chen <chencindy@google.com>
Date:   Mon Mar 15 13:33:40 2021 -0700

    [dv/chip] solve same_csr_outstanding_timeout
    
    This PR fixes same_csr_outstanding timeout issue. The timeout is reached
    mainly because there are too many resets in this sequence.
    We removed the reset when writing to wen_regs by manually calling the
    function to lock lockable regs.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

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
