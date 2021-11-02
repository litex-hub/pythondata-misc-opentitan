import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8571"
version_tuple = (0, 0, 8571)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8571")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8459"
data_version_tuple = (0, 0, 8459)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8459")
except ImportError:
    pass
data_git_hash = "0a345f9331a47c2179b353259e288d12eab13cc1"
data_git_describe = "v0.0-8459-g0a345f933"
data_git_msg = """\
commit 0a345f9331a47c2179b353259e288d12eab13cc1
Author: Weicai Yang <weicai@google.com>
Date:   Mon Nov 1 11:44:58 2021 -0700

    [dv] Update TL intg testplan
    
    Merged tl_intg_err_mem_subword_cg into tl_intg_err_cg as memory doesn't
    exist in all IPs. This cg is only enabled when the IP contains memory.
    No need to have a separate entry for it.
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
