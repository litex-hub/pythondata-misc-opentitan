import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5205"
version_tuple = (0, 0, 5205)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5205")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5114"
data_version_tuple = (0, 0, 5114)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5114")
except ImportError:
    pass
data_git_hash = "466585e351fbe8687445131a20317c465ca43c36"
data_git_describe = "v0.0-5114-g466585e35"
data_git_msg = """\
commit 466585e351fbe8687445131a20317c465ca43c36
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Mar 1 15:06:01 2021 -0800

    [top] First draft PR to enlarge memories
    
    - Enlarge memories to include ECC
    - Disable parity generation
    - tlul_adapter level and above still assume previous width
    - Follow-on PR will introduce more changes upstream
    
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
