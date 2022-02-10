import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10228"
version_tuple = (0, 0, 10228)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10228")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10104"
data_version_tuple = (0, 0, 10104)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10104")
except ImportError:
    pass
data_git_hash = "d77447877a7e516ec5067f89554f6a12d6f4844f"
data_git_describe = "v0.0-10104-gd77447877"
data_git_msg = """\
commit d77447877a7e516ec5067f89554f6a12d6f4844f
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sun Jan 23 14:40:31 2022 -0800

    [entropy_src/dv] Add env. support for FW_OV pathway
    
    - Introduce scoreboarding checks for reading the "observe" FIFO
    - Creates an fw_ov test to probe this functionality
       - Currently only reads from the observe FIFO
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
