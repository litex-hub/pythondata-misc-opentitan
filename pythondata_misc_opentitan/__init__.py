import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13085"
version_tuple = (0, 0, 13085)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13085")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12943"
data_version_tuple = (0, 0, 12943)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12943")
except ImportError:
    pass
data_git_hash = "204e8157ec65ae698d92e49e5679771966125828"
data_git_describe = "v0.0-12943-g204e8157ec"
data_git_msg = """\
commit 204e8157ec65ae698d92e49e5679771966125828
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Mon Jul 11 05:48:37 2022 -0700

    added test + interface for FI on aes_control_FSM
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
