import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9340"
version_tuple = (0, 0, 9340)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9340")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9223"
data_version_tuple = (0, 0, 9223)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9223")
except ImportError:
    pass
data_git_hash = "92c57334f99f03b11830f3a8a58b2615f003fe33"
data_git_describe = "v0.0-9223-g92c57334f"
data_git_msg = """\
commit 92c57334f99f03b11830f3a8a58b2615f003fe33
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Thu Dec 23 08:56:34 2021 -0800

    [pwm/dv] adding pwm env
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
