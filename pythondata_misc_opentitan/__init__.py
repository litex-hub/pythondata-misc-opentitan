import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14151"
version_tuple = (0, 0, 14151)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14151")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14009"
data_version_tuple = (0, 0, 14009)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14009")
except ImportError:
    pass
data_git_hash = "f4a8a3af6ec38c27fc0ec7a57ec29d962d2c75e5"
data_git_describe = "v0.0-14009-gf4a8a3af6e"
data_git_msg = """\
commit f4a8a3af6ec38c27fc0ec7a57ec29d962d2c75e5
Author: Weicai Yang <weicai@google.com>
Date:   Fri Sep 2 23:06:39 2022 -0700

    [spi_device/dv] Update spi agent for CSB
    
    Update agent to be able to control CSB via an item, rather than just via
    agent_cfg, so that we could start TPM seq across with flash seq, as they use
    different CSB.
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
