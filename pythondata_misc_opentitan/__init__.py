import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14303"
version_tuple = (0, 0, 14303)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14303")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14161"
data_version_tuple = (0, 0, 14161)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14161")
except ImportError:
    pass
data_git_hash = "bf10cf94cc2fd0082450aaa6a7f4a256d58a0d0d"
data_git_describe = "v0.0-14161-gbf10cf94cc"
data_git_msg = """\
commit bf10cf94cc2fd0082450aaa6a7f4a256d58a0d0d
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue Sep 20 09:02:24 2022 +0100

    [dv, entropy_src] Fix the test chip_sw_entropy_src_fuse_en_fw_read_test
    
    Add a mandatory configuration for the function `dif_entropy_src_configure()`.
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
