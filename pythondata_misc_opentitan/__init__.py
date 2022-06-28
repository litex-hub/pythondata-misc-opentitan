import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12870"
version_tuple = (0, 0, 12870)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12870")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12728"
data_version_tuple = (0, 0, 12728)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12728")
except ImportError:
    pass
data_git_hash = "f49dd4327667018ef3e52ce47adcadf5a312435f"
data_git_describe = "v0.0-12728-gf49dd43276"
data_git_msg = """\
commit f49dd4327667018ef3e52ce47adcadf5a312435f
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Fri Jun 24 14:49:18 2022 +0100

    [doc] Add section on dealing with emails from GitHub
    
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
