import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8724"
version_tuple = (0, 0, 8724)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8724")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8612"
data_version_tuple = (0, 0, 8612)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8612")
except ImportError:
    pass
data_git_hash = "eca0e5ab490a4d35d71e68967f51fae5e4f1a6f8"
data_git_describe = "v0.0-8612-geca0e5ab4"
data_git_msg = """\
commit eca0e5ab490a4d35d71e68967f51fae5e4f1a6f8
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Oct 29 10:51:59 2021 +0100

    [dv] Slightly generalise run_stress_all_with_rand_reset_vseq
    
    This task was originally designed for running stress sequences,
    selected by plusarg. More recently, we taught it to take an optional
    sequence argument, which would be used instead of the stress sequence.
    
    Tidy things up a bit, moving the generic stuff that takes a sequence
    to a new task (run_seq_with_rand_reset_vseq) and putting the plusargs
    handling in a wrapper task.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
