import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12825"
version_tuple = (0, 0, 12825)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12825")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12683"
data_version_tuple = (0, 0, 12683)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12683")
except ImportError:
    pass
data_git_hash = "4bbb3434d86d75a4464c2a5e5e710ae8162dc9f6"
data_git_describe = "v0.0-12683-g4bbb3434d8"
data_git_msg = """\
commit 4bbb3434d86d75a4464c2a5e5e710ae8162dc9f6
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Jun 23 15:58:13 2022 -0400

    [rv_compliance] Update riscv compliance tests to 1.0
    
    This change updates the riscv compliances tests to 1.0 to fix the
    access violation bugs in I-SB-01 and I-SH-01.
    
    See https://github.com/riscv-non-isa/riscv-arch-test/pull/104 for more
    details.
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
