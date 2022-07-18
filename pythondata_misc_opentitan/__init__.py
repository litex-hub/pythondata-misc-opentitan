import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13154"
version_tuple = (0, 0, 13154)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13154")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13012"
data_version_tuple = (0, 0, 13012)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13012")
except ImportError:
    pass
data_git_hash = "717a66e5a51dc81764dc2388741bd1b4fba5d4e4"
data_git_describe = "v0.0-13012-g717a66e5a5"
data_git_msg = """\
commit 717a66e5a51dc81764dc2388741bd1b4fba5d4e4
Author: Weicai Yang <weicai@google.com>
Date:   Fri Jul 15 16:19:40 2022 -0700

    [spi_device/dv] Update for passthrough
    
    1. support testing invalid opcodes
    2. support dummy cycles
    3. a few fixes
    4. rename op_code -> opcode
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
