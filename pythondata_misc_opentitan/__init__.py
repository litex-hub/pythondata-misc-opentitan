import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12682"
version_tuple = (0, 0, 12682)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12682")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12540"
data_version_tuple = (0, 0, 12540)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12540")
except ImportError:
    pass
data_git_hash = "738a43665fa1a253f086ab412095430030b57532"
data_git_describe = "v0.0-12540-g738a43665"
data_git_msg = """\
commit 738a43665fa1a253f086ab412095430030b57532
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Jun 7 19:18:31 2022 -0700

    [top/spi_device] constraint and clock updates
    
    - refer to https://docs.google.com/presentation/d/14VfPqah-27uFUjkAS3WGbNxFH4EK-Y2PAvpjdHoUXn8/edit?usp=sharing for details.
    
    - move clock definition to pad instead of internal buffers
    - add generated clocks for cleaner hold-time handling
    - connect buffer output to sram clock mux
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
