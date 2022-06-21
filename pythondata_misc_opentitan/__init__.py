import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12746"
version_tuple = (0, 0, 12746)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12746")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12604"
data_version_tuple = (0, 0, 12604)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12604")
except ImportError:
    pass
data_git_hash = "87828fd8a08cda12924cfe7eb59d3b69bc2dd802"
data_git_describe = "v0.0-12604-g87828fd8a0"
data_git_msg = """\
commit 87828fd8a08cda12924cfe7eb59d3b69bc2dd802
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Wed Jun 15 14:22:37 2022 +0100

    [doc] Add doc index for third_party folder
    
    Signed-off-by: Marno van der Maas <mvdmaas+git@lowrisc.org>

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
