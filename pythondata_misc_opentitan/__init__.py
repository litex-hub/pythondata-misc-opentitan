import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14725"
version_tuple = (0, 0, 14725)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14725")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14583"
data_version_tuple = (0, 0, 14583)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14583")
except ImportError:
    pass
data_git_hash = "e5de5869cfd24ec6d23d19b2f75e89f7d9a61b7d"
data_git_describe = "v0.0-14583-ge5de5869cf"
data_git_msg = """\
commit e5de5869cfd24ec6d23d19b2f75e89f7d9a61b7d
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 12 18:41:55 2022 -0700

    [test_rom] enable icache / Ibex security features
    
    This updates the test ROM to enable the icache (and other cpuctrl
    controlled Ibex security features) based on the OTP-stored configuration
    word.
    
    This fixes #12883.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
