import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5227"
version_tuple = (0, 0, 5227)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5227")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5136"
data_version_tuple = (0, 0, 5136)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5136")
except ImportError:
    pass
data_git_hash = "a6f582993cf4368aab54cf865341deeff9115003"
data_git_describe = "v0.0-5136-ga6f582993"
data_git_msg = """\
commit a6f582993cf4368aab54cf865341deeff9115003
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 2 14:02:47 2021 -0800

    [tlul] block writes and reads on errors in adapter_reg
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
