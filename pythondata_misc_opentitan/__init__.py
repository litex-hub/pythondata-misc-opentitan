import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13198"
version_tuple = (0, 0, 13198)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13198")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13056"
data_version_tuple = (0, 0, 13056)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13056")
except ImportError:
    pass
data_git_hash = "780788efc8dc7669dbc7314a6026f8bacbc46f7e"
data_git_describe = "v0.0-13056-g780788efc8"
data_git_msg = """\
commit 780788efc8dc7669dbc7314a6026f8bacbc46f7e
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Wed Jul 20 14:27:30 2022 -0700

    [entropy_src/dv] Redefine bins for cntr coverpoints
    
    Creates:
    - A coverpoint with two bins for the counter types with only one
      instance.
    - Three cps with four bins each for the HT's that have one cntr
      instance per line.
    - A coverpoint with 16 bins for the bucket test counters.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
