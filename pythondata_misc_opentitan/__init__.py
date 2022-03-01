import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10611"
version_tuple = (0, 0, 10611)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10611")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10485"
data_version_tuple = (0, 0, 10485)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10485")
except ImportError:
    pass
data_git_hash = "07eee9d8ed75473309090c5a35de545d5cecdbf6"
data_git_describe = "v0.0-10485-g07eee9d8e"
data_git_msg = """\
commit 07eee9d8ed75473309090c5a35de545d5cecdbf6
Author: Viswanadha Bazawada <viswanadha.bazawada@ensilica.com>
Date:   Mon Feb 7 14:41:42 2022 +0000

    [spi_host/dv] Enhanced Smoke Test
    
    - Added Speed Test
    - Added Constraints to Segment Item
    - Added Quad And Dual To Device Resp Seq
    - Added Tag For Cover Points To Speed Test
    - Added Sw Reset Test
    - Added Performance Test
    - Added Spi Monitor Update Dual And Quad Mode
    
    Signed-off-by: Viswanadha Bazawada <viswanadha.bazawada@ensilica.com>

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
