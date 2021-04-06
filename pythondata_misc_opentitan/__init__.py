import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5716"
version_tuple = (0, 0, 5716)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5716")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5621"
data_version_tuple = (0, 0, 5621)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5621")
except ImportError:
    pass
data_git_hash = "3ce3f7743be2075561554cf18176ba283941ccfd"
data_git_describe = "v0.0-5621-g3ce3f7743"
data_git_msg = """\
commit 3ce3f7743be2075561554cf18176ba283941ccfd
Author: Weicai Yang <weicai@google.com>
Date:   Fri Apr 2 16:59:38 2021 -0700

    [dv] Support multi-ral (part 1)
    
    1. create a queue for names of ral models. RAL models will be created
    automatically based the names
    2. excl_item is generated in reg_block, don't need to supply this from
    outside. Clean this up to support multi-ral
    
    CSR seq, multiple TL agents, scb update will come in next PR
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
