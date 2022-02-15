import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10323"
version_tuple = (0, 0, 10323)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10323")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10197"
data_version_tuple = (0, 0, 10197)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10197")
except ImportError:
    pass
data_git_hash = "a4e8721132e8e259d0bcf9359fc90244a9d3637e"
data_git_describe = "v0.0-10197-ga4e872113"
data_git_msg = """\
commit a4e8721132e8e259d0bcf9359fc90244a9d3637e
Author: Alexander Williams <awill@google.com>
Date:   Tue Feb 15 09:06:24 2022 -0800

    [flash_ctrl/dif] Fix word_count handling for erase
    
    The word_count / words_remaining handling was forbidding erase
    operations from completing, as the transaction functions required a
    nonzero word_count and activity on the FIFOs to reduce it to 0 before
    completion.
    
    Exempt erase operations from needing any specific word_count, and set
    words_remaining to 0.
    
    Co-authored-by: Dave Williams <dave.williams@ensilica.com>
    Signed-off-by: Alexander Williams <awill@google.com>

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
