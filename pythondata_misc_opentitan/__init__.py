import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5642"
version_tuple = (0, 0, 5642)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5642")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5547"
data_version_tuple = (0, 0, 5547)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5547")
except ImportError:
    pass
data_git_hash = "58c0c4bed88beab02800a235adc09e2104ba39ab"
data_git_describe = "v0.0-5547-g58c0c4bed"
data_git_msg = """\
commit 58c0c4bed88beab02800a235adc09e2104ba39ab
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 29 16:07:45 2021 +0100

    [aon_timer,dv] Initial DV document
    
    This fills out the document template, describing the overall structure
    of the DV environment and the rough plan of how things will work.
    Details are likely to change as we come to implement the scoreboard
    and test sequences.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
