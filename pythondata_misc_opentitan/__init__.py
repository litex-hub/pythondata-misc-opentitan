import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14900"
version_tuple = (0, 0, 14900)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14900")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14758"
data_version_tuple = (0, 0, 14758)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14758")
except ImportError:
    pass
data_git_hash = "bd9f6d0199af9e3358289c0b3a3900921afe8d02"
data_git_describe = "v0.0-14758-gbd9f6d0199"
data_git_msg = """\
commit bd9f6d0199af9e3358289c0b3a3900921afe8d02
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Oct 21 11:10:12 2022 -0700

    [flash_ctrl] Handle faulted reads
    
    In the current design, if a read were faulted to a non-existant location
    AFTER the memory properties check, the return data could be unknown
    and that makes the assertions go wild.
    
    Since we are already detecting for this type of attack, use the same signals
    to force the returning data and error conditions to a known value.
    
    This removes the need for DV to individually turn off asertions for this
    case.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
