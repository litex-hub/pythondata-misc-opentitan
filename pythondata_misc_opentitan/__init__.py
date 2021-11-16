import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8734"
version_tuple = (0, 0, 8734)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8734")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8622"
data_version_tuple = (0, 0, 8622)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8622")
except ImportError:
    pass
data_git_hash = "cb1c9d002eff37909bb870d704246f804d2364c6"
data_git_describe = "v0.0-8622-gcb1c9d002"
data_git_msg = """\
commit cb1c9d002eff37909bb870d704246f804d2364c6
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Nov 15 17:18:25 2021 -0800

    [chip dv] Add support for tiled RAM instances
    
    - Adds support for attaching multiple mem backdoor util instances for
    multiply-tiled RAMs in the design.
    - Number of tiles for main / ret SRAM is a runtime setting that is set
    to 1 in the open source testbench with a generic model.
    - Extended class can set it to whatever the correct value is for that
    environment.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
