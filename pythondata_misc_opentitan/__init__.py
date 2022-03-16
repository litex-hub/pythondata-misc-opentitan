import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10913"
version_tuple = (0, 0, 10913)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10913")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10787"
data_version_tuple = (0, 0, 10787)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10787")
except ImportError:
    pass
data_git_hash = "998bb559bfd720bacc3cbecc5a0dec45902dfafe"
data_git_describe = "v0.0-10787-g998bb559b"
data_git_msg = """\
commit 998bb559bfd720bacc3cbecc5a0dec45902dfafe
Author: Weicai Yang <weicai@google.com>
Date:   Mon Mar 14 15:49:19 2022 -0700

    [dv] Add valid/ready req/ack coverage for push_pull agent
    
    Sample all the combination of valid/ready or req/ack
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
