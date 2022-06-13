import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12655"
version_tuple = (0, 0, 12655)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12655")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12513"
data_version_tuple = (0, 0, 12513)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12513")
except ImportError:
    pass
data_git_hash = "ff74d05dabd00325ef2eec7d99ba7afe141063a8"
data_git_describe = "v0.0-12513-gff74d05da"
data_git_msg = """\
commit ff74d05dabd00325ef2eec7d99ba7afe141063a8
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Jun 7 10:57:04 2022 -0700

    chore(cdc): Alert Handler PING/ACK waivers
    
    Alert handler sender/receiver follows handshake mechanism with
    differential signal method. The request(ping) and ack are converted into
    level so that slow-to-fast clock 2FF sync error can be ignored.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
