import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10656"
version_tuple = (0, 0, 10656)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10656")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10530"
data_version_tuple = (0, 0, 10530)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10530")
except ImportError:
    pass
data_git_hash = "2ed086ff5f6667491b9c019de2e6122ad6fa2572"
data_git_describe = "v0.0-10530-g2ed086ff5"
data_git_msg = """\
commit 2ed086ff5f6667491b9c019de2e6122ad6fa2572
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Mar 1 16:05:16 2022 -0800

    [tlul] adjust tlul_sram_byte enable condition
    
    Previously, the tlul_sram_byte module was enabled whenever an adapter sram
    allowed both byte access and checked for integrity.
    
    This is not the correct enable condition. The tlul_sram_byte is meant to
    generate correct integrity when the downstream memory actually stores
    full word integrity and requires a read modified write for byte accesses.
    
    If a module simply checks for integrity, it does not say anything about
    whether the downstream module stores integrity and whether byte writes require
    a read modified write.
    
    Instead, change the condition to byte access AND data integrity passthrough are
    enabled. Data integrity passthrough implies the downstream memory will make use of
    extra integrity in some way and thus requires correct read modified write handling
    on byte accesses.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
