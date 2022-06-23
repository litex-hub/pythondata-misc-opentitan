import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12802"
version_tuple = (0, 0, 12802)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12802")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12660"
data_version_tuple = (0, 0, 12660)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12660")
except ImportError:
    pass
data_git_hash = "013c4d7d5cdfead5c71ba8a387567ff1ab71d708"
data_git_describe = "v0.0-12660-g013c4d7d5c"
data_git_msg = """\
commit 013c4d7d5cdfead5c71ba8a387567ff1ab71d708
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed May 11 17:12:22 2022 +0100

    [otbn,rtl] Add fault detection to controller req/ack interface
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
