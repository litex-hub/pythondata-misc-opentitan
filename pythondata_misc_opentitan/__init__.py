import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10413"
version_tuple = (0, 0, 10413)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10413")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10287"
data_version_tuple = (0, 0, 10287)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10287")
except ImportError:
    pass
data_git_hash = "5cb04a7b86aa50a091f27f2a14d3a9f6bb569d60"
data_git_describe = "v0.0-10287-g5cb04a7b8"
data_git_msg = """\
commit 5cb04a7b86aa50a091f27f2a14d3a9f6bb569d60
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Sat Feb 12 17:11:33 2022 -0800

    [entropy_src] Document & Implement THRESHOLD_SCOPE
    
    - Documents the THRESHOLD_SCOPE register
    - Updates the AdaptP and Markov health tests.  The tests now operate on
      the same scope (either by-line or by-sum) depending on the value of
      THRESHOLD_SCOPE.
    - Adds new DV environment configurations and scoreboarding updates to
      reflect the new RTL changes.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
    Co-authored-by: rasmus-madsen <53917183+rasmus-madsen@users.noreply.github.com>

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
