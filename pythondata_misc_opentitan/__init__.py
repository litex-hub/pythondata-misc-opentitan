import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15237"
version_tuple = (0, 0, 15237)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15237")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15095"
data_version_tuple = (0, 0, 15095)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15095")
except ImportError:
    pass
data_git_hash = "a09d5ca30df75679de69d417dbe40e2d3d899601"
data_git_describe = "v0.0-15095-ga09d5ca30d"
data_git_msg = """\
commit a09d5ca30df75679de69d417dbe40e2d3d899601
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Nov 4 01:53:34 2022 +0100

    [aes, dv] Depending on FI target signal, force different values
    
    For some FI target signals, forcing certain values doesn't have any
    impact on the functionality of the design. For example:
    - Forcing a 1 on a handshake signal that is only read if the FSM is
      anyway ready to proceed, or if the handshake is backed up by an
      additional local counter.
    - Forcing a 0 where multiple copies of the signal are OR-comibined
      together.
    This commit changes the FI tests to force values depending on the target
    signal.
    
    This resolves lowRISC/OpenTitan#13572.
    
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
