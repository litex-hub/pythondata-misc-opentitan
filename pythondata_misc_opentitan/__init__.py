import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12805"
version_tuple = (0, 0, 12805)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12805")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12663"
data_version_tuple = (0, 0, 12663)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12663")
except ImportError:
    pass
data_git_hash = "cbb0b97ba6f4452b8c36161d25a7d744ea486c32"
data_git_describe = "v0.0-12663-gcbb0b97ba6"
data_git_msg = """\
commit cbb0b97ba6f4452b8c36161d25a7d744ea486c32
Author: Marno van der Maas <mvdmaas+git@lowrisc.org>
Date:   Thu Jun 23 14:55:30 2022 +0100

    [otbn,dv] Fix reference to start secure wipe
    
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
