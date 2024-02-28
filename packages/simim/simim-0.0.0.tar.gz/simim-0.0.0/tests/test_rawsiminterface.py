import os
import simim
import simim._paths

def test_import():
    """Make sure setupsimim is available"""
    print(dir(simim))
    assert 'setupsimim' in dir(simim)

def test_path_init():
    """Check that the resources path exists"""
    p = simim._paths._paths()
    print(p.root_file)
    assert os.path.exists(p.root_file)
