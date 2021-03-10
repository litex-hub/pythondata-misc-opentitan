import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5317"
version_tuple = (0, 0, 5317)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5317")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5222"
data_version_tuple = (0, 0, 5222)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5222")
except ImportError:
    pass
data_git_hash = "cfcfbce85e182c127b8c4be5cd8bf531e0a4d927"
data_git_describe = "v0.0-5222-gcfcfbce85"
data_git_msg = """\
commit cfcfbce85e182c127b8c4be5cd8bf531e0a4d927
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 9 14:14:30 2021 +0000

    [reggen] Promote FOO_SIZE to an int unsigned in *_reg_pkg.sv
    
    With the previous version of the code, there was a problem if the last
    window happened to finish on the same power of 2 boundary as the
    block's address space. In that case, we ended up with something like
    
        parameter logic [9:0] BLOCK_FOO_SIZE = 10'd1024;
    
    which is, of course, zero.
    
    It turns out that the only code in the tree that uses these _SIZE
    parameters is using them to compute int parameters (rather than
    something involving the address width). As such, we can just promote
    the parameter to an int unsigned, fixing various width mismatches as a
    bonus!
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
