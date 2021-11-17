import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8748"
version_tuple = (0, 0, 8748)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8748")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8636"
data_version_tuple = (0, 0, 8636)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8636")
except ImportError:
    pass
data_git_hash = "e7c2907b55cee05315ecb315386350c7bcae30d2"
data_git_describe = "v0.0-8636-ge7c2907b5"
data_git_msg = """\
commit e7c2907b55cee05315ecb315386350c7bcae30d2
Author: Weicai Yang <weicai@google.com>
Date:   Mon Nov 15 17:01:10 2021 -0800

    [dv] Update cip to support instr_type better
    
    1. Fix finish_item calling item.randomize(sth), which invokes
    post_randomize again
    2. instr_type is part of a_user. Removed the replicated variable and
    added set/get_instr_type functions
    
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
