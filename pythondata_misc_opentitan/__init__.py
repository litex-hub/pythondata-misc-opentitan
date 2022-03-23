import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11031"
version_tuple = (0, 0, 11031)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11031")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10905"
data_version_tuple = (0, 0, 10905)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10905")
except ImportError:
    pass
data_git_hash = "cf7df522acbb58bdf604302a36c580bc02550f0a"
data_git_describe = "v0.0-10905-gcf7df522a"
data_git_msg = """\
commit cf7df522acbb58bdf604302a36c580bc02550f0a
Author: Jade Philipoom <jadep@google.com>
Date:   Mon Mar 21 19:45:41 2022 +0000

    [doc] Update "getting started" diagram to show software first.
    
    Because everyone needs to build software, the workflow seems easier if
    the software is built first, and then the different workflows branch off
    afterwards.
    
    Also adjusts the FPGA flow to more accurately describe the steps
    involved (bitstream must be loaded, and "loading" and "running" the
    software are not really separate steps).
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
