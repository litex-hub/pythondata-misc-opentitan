import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9617"
version_tuple = (0, 0, 9617)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9617")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9495"
data_version_tuple = (0, 0, 9495)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9495")
except ImportError:
    pass
data_git_hash = "3cc8d5a6c5cd222b32ef3ee0464b3650c8b80e15"
data_git_describe = "v0.0-9495-g3cc8d5a6c"
data_git_msg = """\
commit 3cc8d5a6c5cd222b32ef3ee0464b3650c8b80e15
Author: Michael Schaffner <msf@google.com>
Date:   Thu Jan 13 16:36:36 2022 -0800

    [aes/syn] Update GTECH flow for AES wrapper
    
    This separate synthesis target for the AES wrapper is only intended to
    produce a mapping of the wrapper alone. The motivation for synthesizing
    AES and the wrapper separately is that we can ensure that no sort of
    optimization takes place across the hierarchy boundary between them (the
    wrapper is TB code whereas the AES is actual synthesizable code).
    
    In order to achieve this we just remove the aes module from the working
    lib after elaboration.
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
