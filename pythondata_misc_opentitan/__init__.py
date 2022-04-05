import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11368"
version_tuple = (0, 0, 11368)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11368")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11242"
data_version_tuple = (0, 0, 11242)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11242")
except ImportError:
    pass
data_git_hash = "4d80330c6d13e4c8490bf5f8e4f0a9727ac5759d"
data_git_describe = "v0.0-11242-g4d80330c6"
data_git_msg = """\
commit 4d80330c6d13e4c8490bf5f8e4f0a9727ac5759d
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Apr 4 13:04:41 2022 +0200

    [kmac] Ignore entropy refresh requests when running in SW entropy mode
    
    When running in EDN entropy mode, software can manually request the
    entropy to be refreshed from EDN.
    
    If instead running in SW entropy mode, SW provides the entropy via CSRs.
    SW is still able to request the entropy to be refreshed. Prior to this
    commit, the design would then go into the StRandEdn state and request
    fresh entropy from EDN, but the entropy received from EDN would be
    ignored. Instead, the LFSR would be reseeded using the value provided by
    SW via CSRs. If SW "forgot" to update the CSRs, the LFSR
    would be reseeded using the same value. This is a bit counter-intuitive
    and can be exploitet for SCA. It's safer to just ignore these requests
    when running in SW entropy mode.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
