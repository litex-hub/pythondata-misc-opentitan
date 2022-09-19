import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14287"
version_tuple = (0, 0, 14287)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14287")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14145"
data_version_tuple = (0, 0, 14145)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14145")
except ImportError:
    pass
data_git_hash = "c80a2e2e1bc2cb727ae82cb5c00c666a677c191f"
data_git_describe = "v0.0-14145-gc80a2e2e1b"
data_git_msg = """\
commit c80a2e2e1bc2cb727ae82cb5c00c666a677c191f
Author: Michael Schaffner <msf@google.com>
Date:   Fri Sep 16 14:54:43 2022 -0700

    [test/rv_plic] Add a hart_id check to the test
    
    This additional check makes sure that the configured PLIC target
    ID corresponds to the hart ID of the processor this is executed on.
    To be used in single-hart systems only.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
