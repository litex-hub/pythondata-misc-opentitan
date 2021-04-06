import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5728"
version_tuple = (0, 0, 5728)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5728")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5633"
data_version_tuple = (0, 0, 5633)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5633")
except ImportError:
    pass
data_git_hash = "0d62c3c104417b714d6713444d2bef4815be9709"
data_git_describe = "v0.0-5633-g0d62c3c10"
data_git_msg = """\
commit 0d62c3c104417b714d6713444d2bef4815be9709
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Sun Mar 21 17:44:58 2021 -0700

    [entropy_src/rtl] increase health teset fail counter
    
    Allow a large number of health test fails with larger counter.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
