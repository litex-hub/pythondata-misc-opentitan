import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15057"
version_tuple = (0, 0, 15057)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15057")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14915"
data_version_tuple = (0, 0, 14915)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14915")
except ImportError:
    pass
data_git_hash = "f5e229c261a9cd9c49cc66f499a4c7ff4d98b1ab"
data_git_describe = "v0.0-14915-gf5e229c261"
data_git_msg = """\
commit f5e229c261a9cd9c49cc66f499a4c7ff4d98b1ab
Author: Miles Dai <milesdai@google.com>
Date:   Wed Oct 26 15:07:42 2022 -0400

    [bitstream] Update usr_access with the bitstream hash
    
    This prevents bitstreams that are spliced at the same time from
    having the same usr_access value.
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
