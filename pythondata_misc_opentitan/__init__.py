import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8539"
version_tuple = (0, 0, 8539)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8539")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8427"
data_version_tuple = (0, 0, 8427)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8427")
except ImportError:
    pass
data_git_hash = "814c6158da551068264a5b163f7e4b993d4b9c33"
data_git_describe = "v0.0-8427-g814c6158d"
data_git_msg = """\
commit 814c6158da551068264a5b163f7e4b993d4b9c33
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Oct 21 15:07:16 2021 -0700

    [top] Add missing sensor_ctrl test plan item.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    Update hw/top_earlgrey/data/chip_testplan.hjson
    
    Co-authored-by: Srikrishna Iyer <46467186+sriyerg@users.noreply.github.com>

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
