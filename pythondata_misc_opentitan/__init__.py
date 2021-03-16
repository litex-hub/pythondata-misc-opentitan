import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5408"
version_tuple = (0, 0, 5408)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5408")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5313"
data_version_tuple = (0, 0, 5313)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5313")
except ImportError:
    pass
data_git_hash = "25468b4a8a6b3dc53f87a0ccdfb7fde34c1ef657"
data_git_describe = "v0.0-5313-g25468b4a8"
data_git_msg = """\
commit 25468b4a8a6b3dc53f87a0ccdfb7fde34c1ef657
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 11 15:20:10 2021 +0000

    [dv] Get blocks with multiple device interfaces working with chip DV
    
    The big change here is that we might now generate several *_ral_pkg.sv
    files for a block: one per device interface. To support this,
    gen_dv.py now has a loop over device interfaces (just like gen_rtl.py
    and gen_fpv.py).
    
    What's more, we have the same problem as gen_fpv where we need to list
    the generated files in the core file properly. To get that right, we
    pull core file generation out of ralgen.py and put it into gen_fpv,
    where we know what files we've created.
    
    Finally (and this is the biggest part of the patch), we split up the
    top-level and block-level versions of uvm_reg.sv.tpl. The top-level
    and block-level templates share functions from uvm_reg_base.sv.tpl,
    and I think the result is a bit easier to follow. There's also a
    liberal sprinking of big "##"-style comments to try to make the
    template code a bit easier to follow.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
