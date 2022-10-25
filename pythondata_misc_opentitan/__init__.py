import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14936"
version_tuple = (0, 0, 14936)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14936")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14794"
data_version_tuple = (0, 0, 14794)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14794")
except ImportError:
    pass
data_git_hash = "a6b908283fccba3f8b6b44052c6ad87276dc21e8"
data_git_describe = "v0.0-14794-ga6b908283f"
data_git_msg = """\
commit a6b908283fccba3f8b6b44052c6ad87276dc21e8
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Mon Oct 24 20:19:17 2022 +0100

    [dv] Run more iterations of the otbn escalate test
    
    This is required to hit FSM coverage goals
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
