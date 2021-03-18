import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5448"
version_tuple = (0, 0, 5448)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5448")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5353"
data_version_tuple = (0, 0, 5353)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5353")
except ImportError:
    pass
data_git_hash = "263165193173262dd701517a99da0f271f830222"
data_git_describe = "v0.0-5353-g263165193"
data_git_msg = """\
commit 263165193173262dd701517a99da0f271f830222
Author: Udi Jonnalagadda <udij@google.com>
Date:   Wed Mar 17 16:45:59 2021 -0700

    [dv/sram] refactor sram_zero_delays
    
    this PR refactors how zero delays are set in the SRAM TL agent,
    tying it to the main zero_delays knob in the CSR TL agent.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
