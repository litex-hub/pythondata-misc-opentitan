import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5498"
version_tuple = (0, 0, 5498)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5498")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5403"
data_version_tuple = (0, 0, 5403)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5403")
except ImportError:
    pass
data_git_hash = "44bf5faa653143c768261e99f80edf1125486b02"
data_git_describe = "v0.0-5403-g44bf5faa6"
data_git_msg = """\
commit 44bf5faa653143c768261e99f80edf1125486b02
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Mar 19 11:32:26 2021 -0700

    [fpv/rv_plic] Fix compile error from auto-gen csr_fpv_assert core file
    
    This PR fixes a fusesoc dependency error from auto-generated
    csr_fpv_assertion core file.
    In `ip_block.py` we assume all IP core file names are
    `lowrisc:ip:{block_name}`. However, for rv_plic, it is called
    `lowrisc:ip:rv_plic_example`. So in hjson file, I added the core name to
    avoid fusesoc compile error.
    
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
