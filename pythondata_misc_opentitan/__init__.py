import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15018"
version_tuple = (0, 0, 15018)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15018")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14876"
data_version_tuple = (0, 0, 14876)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14876")
except ImportError:
    pass
data_git_hash = "39eb0210e1bc6a378f052cbd43c41d502e1bac98"
data_git_describe = "v0.0-14876-g39eb0210e1"
data_git_msg = """\
commit 39eb0210e1bc6a378f052cbd43c41d502e1bac98
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Thu Oct 27 22:49:58 2022 +0200

    [aes, dv] Align and fix FI test sequences
    
    This commit aligns the different FI test sequences for the AES main FSM,
    the cipher core FSM and the CTR mode FSM. Thanks to this code
    re-alignment a bug inside aes_control_fi_vseq.sv has been identified and
    fixed which caused about 20% of these tests to fail.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
