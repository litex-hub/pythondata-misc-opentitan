import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9585"
version_tuple = (0, 0, 9585)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9585")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9463"
data_version_tuple = (0, 0, 9463)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9463")
except ImportError:
    pass
data_git_hash = "8a2c0aba06fc49162943be2fc6e97dcdc73f14da"
data_git_describe = "v0.0-9463-g8a2c0aba0"
data_git_msg = """\
commit 8a2c0aba06fc49162943be2fc6e97dcdc73f14da
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Jan 17 14:57:51 2022 +0000

    [dv,rstmgr] Fix mubi check in rstmgr_cascading_sva_if
    
    The type of scanmode_i changed to mubi4_t in ee8c4bf171 but it looks
    like we didn't update its uses to the new type.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
