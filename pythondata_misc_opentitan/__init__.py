import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8762"
version_tuple = (0, 0, 8762)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8762")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8650"
data_version_tuple = (0, 0, 8650)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8650")
except ImportError:
    pass
data_git_hash = "0e0c1a99f5a45584017d42bc8cba0aa376745908"
data_git_describe = "v0.0-8650-g0e0c1a99f"
data_git_msg = """\
commit 0e0c1a99f5a45584017d42bc8cba0aa376745908
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Nov 17 22:10:34 2021 +0000

    [kmac] Use Empty signal from FIFO
    
    The issue has been discussed in #9202
    
    KMAC MsgFIFO sees the FIFO depth to calculate the empty status of SYNC
    FIFO. When the logic writes data and the receiver acked the read data at
    the same time and the FIFO has been empty already, the empty status
    won't be de-asserted as the `depth` wont be increased.
    
    The issue is that SW will not get the fifo empty event due to the
    behavior described above if the receiver logic is faster than the SW.
    
    This commit revises the msgfifo logic to see the `rvalid` as an
    inversion of the empty status. The scenario above will lower the `empty`
    signal with the fix.
    
    Co-Authored-by: Cindy Chen <chencindy@opentitan.org>
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
