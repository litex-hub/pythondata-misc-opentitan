import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14537"
version_tuple = (0, 0, 14537)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14537")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14395"
data_version_tuple = (0, 0, 14395)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14395")
except ImportError:
    pass
data_git_hash = "c01f7b0ffa2d34c33750433fdb41e55db5f997e4"
data_git_describe = "v0.0-14395-gc01f7b0ffa"
data_git_msg = """\
commit c01f7b0ffa2d34c33750433fdb41e55db5f997e4
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Fri Sep 23 22:36:27 2022 +0100

    [top-test] entropy_src_csrng_test
    
    Adds entropy_src_csrng_test, which tests the CSRNG interrupt request interrupt
    whenever a seed or reseed operation is triggered by the CSRNG software
    interface, or by EDN0/EDN1.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
