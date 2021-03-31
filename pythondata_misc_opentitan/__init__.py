import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5652"
version_tuple = (0, 0, 5652)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5652")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5557"
data_version_tuple = (0, 0, 5557)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5557")
except ImportError:
    pass
data_git_hash = "a46be154ebbcb7b0d5e310b5510a4ac700adc9df"
data_git_describe = "v0.0-5557-ga46be154e"
data_git_msg = """\
commit a46be154ebbcb7b0d5e310b5510a4ac700adc9df
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Wed Mar 31 15:52:54 2021 +0100

    [otbn] Remove WIP marker from documentation
    
    The OTBN specification/documentation is mostly consistent, well-written,
    tested and implemented, so there is no more need for a big warning sign
    at the beginning. This aligns OTBN with all other IP blocks in OpenTitan,
    none of which have a similar warning.
    
    Of course, there's always more to do and OTBN (like all other IP blocks
    in OpenTitan) isn't "done" yet. These improvements will happen as evolutions
    to the current design.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
