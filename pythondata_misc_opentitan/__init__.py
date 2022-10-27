import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14980"
version_tuple = (0, 0, 14980)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14980")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14838"
data_version_tuple = (0, 0, 14838)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14838")
except ImportError:
    pass
data_git_hash = "d850f024af6cfc0d9a7877f394374775d2e848c0"
data_git_describe = "v0.0-14838-gd850f024af"
data_git_msg = """\
commit d850f024af6cfc0d9a7877f394374775d2e848c0
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Oct 24 23:27:04 2022 +0200

    [test] Add DV component for AES masking off test, add it to the testplan
    
    This commit adds the AES masking off test to the testplan. As the
    masking itself is transparent to software, a DV component is added to
    probe into AES and verify that 1) all prerequisites are met to switch
    off the masking and 2) that the second share of the state as well as
    mask input and output of SubBytes are all zero, i.e., masking is indeed
    switched off.
    
    This is related to lowRISC/OpenTitan#14240.
    
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
