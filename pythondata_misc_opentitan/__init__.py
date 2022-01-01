import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9309"
version_tuple = (0, 0, 9309)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9309")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9192"
data_version_tuple = (0, 0, 9192)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9192")
except ImportError:
    pass
data_git_hash = "f46b05f8f3f45276ff36d65b8d4151a9dfc9c5d4"
data_git_describe = "v0.0-9192-gf46b05f8f"
data_git_msg = """\
commit f46b05f8f3f45276ff36d65b8d4151a9dfc9c5d4
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Tue Dec 28 16:43:25 2021 -0800

    [entropy_src, dv] New RNG failure seqeunces
    
    In order to improve the testing of health checks this commit introduces
    a new entropy_src_base_rng_seq.  This sequence is an extension of the
    push_pull_indefinite_host_seq, but it provides new methods to control
    (and predict) the randomization of the RNG data.
    
    There are now three modes of operation for the RNG sequence:
    - Typical: Of the three modes this is the highest entropy. In this
      base class, this typical entropy is ideal however a derived class
      could be made to generate weaker entropy
    - Soft failure: the entropy of the RNG sequence is degraded either
      through bias or correlations in the output stream.  In the base
      class however, the soft failure mode is the same as typical.
    - Hard failure: In this mode one or more bits becomes "stuck",
      which is a complete failure of the RNG stream.
    
    Entry into the soft or hard failure modes is random.
    There are two vairables hard_mtbf, and soft_mtbf (mean time before
    failure) which control average time before failing into one of
    these states.  If the parent vseq identifies that the RNG
    sequence has encountered a failure (perhaps through an alert)
    it can call the reset_rng sequence.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
