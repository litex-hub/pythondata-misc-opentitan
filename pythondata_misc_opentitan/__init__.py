import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8404"
version_tuple = (0, 0, 8404)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8404")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8292"
data_version_tuple = (0, 0, 8292)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8292")
except ImportError:
    pass
data_git_hash = "68e725548787e1ed52332a3b5ac9c5c37dac75be"
data_git_describe = "v0.0-8292-g68e725548"
data_git_msg = """\
commit 68e725548787e1ed52332a3b5ac9c5c37dac75be
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Oct 22 00:37:16 2021 +0000

    [dv,sw] Use `*_irq_acknowledge_all()` in PLIC test.
    
    This commit replaces the manual MMIO writes to the IRQ state registers
    to clear all interrupts for a specific IP with the newly added DIF
    equivalent in the `plic_all_irqs_test.c`.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
