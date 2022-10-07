import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14615"
version_tuple = (0, 0, 14615)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14615")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14473"
data_version_tuple = (0, 0, 14473)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14473")
except ImportError:
    pass
data_git_hash = "ff78583a353573257ab27fe9e445db4a0a2c147a"
data_git_describe = "v0.0-14473-gff78583a35"
data_git_msg = """\
commit ff78583a353573257ab27fe9e445db4a0a2c147a
Author: Jade Philipoom <jadep@google.com>
Date:   Fri Sep 16 10:32:19 2022 +0200

    [crypto] Remove DMEM pointers from Ibex-side ECDSA-P256 code.
    
    Modify the Ibex code to match the new DMEM interface for ECDSA-P256.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
