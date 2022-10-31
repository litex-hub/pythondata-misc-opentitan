import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15052"
version_tuple = (0, 0, 15052)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15052")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14910"
data_version_tuple = (0, 0, 14910)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14910")
except ImportError:
    pass
data_git_hash = "c3f641335183c7a9502908db8041865f7c15b0f7"
data_git_describe = "v0.0-14910-gc3f6413351"
data_git_msg = """\
commit c3f641335183c7a9502908db8041865f7c15b0f7
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Oct 28 17:14:01 2022 +0200

    [aes, dv] Correct mapping of CIPHER.CTR.REDUN countermeasure in testplan
    
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
