import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5168"
version_tuple = (0, 0, 5168)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5168")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5077"
data_version_tuple = (0, 0, 5077)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5077")
except ImportError:
    pass
data_git_hash = "93f12ea8c42de02112c730bb28727008df658ee1"
data_git_describe = "v0.0-5077-g93f12ea8c"
data_git_msg = """\
commit 93f12ea8c42de02112c730bb28727008df658ee1
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Feb 25 15:19:20 2021 +0000

    [otbn] Remove enable_i input from otbn_core_model
    
    The previous code had a race in the initial blocks when used in
    otbn.sv. The obvious way to fix this in the SystemVerilog code would
    be to call otbn_model_init() just before we first call
    otbn_model_step. Unfortunately, you can't do that (for Verilator, at
    least) because that ends up mixing blocking and non-blocking
    assignments.
    
    Rather than think hard about how to do this properly in Verilog, we
    can just put in a simple layer of indirection in the C++ and only
    start the subprocess when we see start_i for the first time.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
