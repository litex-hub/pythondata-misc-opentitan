import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14750"
version_tuple = (0, 0, 14750)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14750")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14608"
data_version_tuple = (0, 0, 14608)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14608")
except ImportError:
    pass
data_git_hash = "f403427bedb97c2a36cb4b3ba95eceaf470f60d5"
data_git_describe = "v0.0-14608-gf403427bed"
data_git_msg = """\
commit f403427bedb97c2a36cb4b3ba95eceaf470f60d5
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 13 22:40:06 2022 -0700

    [spi_device/dv] Update seq to utilize tpm level interrupt
    
    Exit loop without finishing reading all the requests and rely on interrupt to fire again.
    
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
