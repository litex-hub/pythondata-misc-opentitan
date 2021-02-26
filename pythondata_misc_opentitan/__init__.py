import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5153"
version_tuple = (0, 0, 5153)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5153")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5062"
data_version_tuple = (0, 0, 5062)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5062")
except ImportError:
    pass
data_git_hash = "eb9498ccf5210981b45d8415c96ad586ac05df50"
data_git_describe = "v0.0-5062-geb9498ccf"
data_git_msg = """\
commit eb9498ccf5210981b45d8415c96ad586ac05df50
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Tue Feb 2 08:33:29 2021 -0800

    [ spi_host, doc] Initial spec draft
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
