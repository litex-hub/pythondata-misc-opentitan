import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11270"
version_tuple = (0, 0, 11270)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11270")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11144"
data_version_tuple = (0, 0, 11144)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11144")
except ImportError:
    pass
data_git_hash = "f3ff88a9d3df10aa2aef2db208065bbfdb8acdb3"
data_git_describe = "v0.0-11144-gf3ff88a9d"
data_git_msg = """\
commit f3ff88a9d3df10aa2aef2db208065bbfdb8acdb3
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Fri Apr 1 12:08:34 2022 +0100

    [dv,tcl] Merge Coverage Databases with union_all
    
    This argument enables to merge different coverage databases with
    different testbench structures to tie together as a single coverage
    database. Necessary for Ibex DV because we want to see the numbers
    for both riscv-dv and core_ibex coverage databases.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
