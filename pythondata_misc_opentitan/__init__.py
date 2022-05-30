import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12407"
version_tuple = (0, 0, 12407)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12407")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12267"
data_version_tuple = (0, 0, 12267)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12267")
except ImportError:
    pass
data_git_hash = "50f8a6ed18ef91ca889a6ccc51c588bff0389b54"
data_git_describe = "v0.0-12267-g50f8a6ed1"
data_git_msg = """\
commit 50f8a6ed18ef91ca889a6ccc51c588bff0389b54
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue May 24 11:00:19 2022 +0200

    [python-requirements.txt] Switch to chipwhisperer-minimal
    
    So far, we haven't touched the chipwhisperer version but we will soon
    have to update in order to re-enable FTDI MPSSE emulation and OpenOCD
    debugging on the CW310. See lowRISC/OpenTitan#10625. However, this isn't
    straightforward as more recent ChipWhisperer versions have dependencies
    that require Python 3.7 or newer (e.g. numpy), whereas OpenTitan
    requires Python 3.6 or newer.
    
    ChipWhisperer has now prepared a minimal ChipWhisperer version that only
    supports the CW310 but doesn't have these dependencies. As such
    chipwhisperer-minimal will allows us to track more recent versions
    ChipWhisperer while remaining on Python 3.6 for the moment (default for
    Ubuntu 18.04). This commit switches to using chipwhisperer-minimal.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
