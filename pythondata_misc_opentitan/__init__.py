import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9813"
version_tuple = (0, 0, 9813)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9813")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9691"
data_version_tuple = (0, 0, 9691)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9691")
except ImportError:
    pass
data_git_hash = "d6e91619f67258464ec8f3a3ba68dfa19f7319fd"
data_git_describe = "v0.0-9691-gd6e91619f"
data_git_msg = """\
commit d6e91619f67258464ec8f3a3ba68dfa19f7319fd
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Thu Jan 20 19:53:12 2022 -0800

    [sw/rom] Updates to sec_mmio hardening
    
    * Introduce launder32 and HARDENED_CHECK to sec_mmio.
    * Remove shutdown callback function.
    * Remove expensive modulus operation.
    * Remove direct use of volatile.
    * Add checks to sec_mmio_init function to ensure counters are properly
      initialized.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
