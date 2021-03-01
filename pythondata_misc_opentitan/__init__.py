import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5178"
version_tuple = (0, 0, 5178)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5178")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5087"
data_version_tuple = (0, 0, 5087)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5087")
except ImportError:
    pass
data_git_hash = "afe9392899f54183d1fb807fda5cad3a0cff35ee"
data_git_describe = "v0.0-5087-gafe939289"
data_git_msg = """\
commit afe9392899f54183d1fb807fda5cad3a0cff35ee
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 1 10:13:08 2021 +0000

    [otbn] Fix missing operation docs for bn.sel
    
    The class name had a spare "r" in it (probably a copy-paste error from
    when I copied it from BNRSHI above). This doesn't matter in any way
    for the ISS, because decoding and tracing is driven by the "insn"
    class field (which had the right name). But it *does* matter for the
    connection with document extraction, which means that the BN.SEL entry
    in the docs was missing its Operation section.
    
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
