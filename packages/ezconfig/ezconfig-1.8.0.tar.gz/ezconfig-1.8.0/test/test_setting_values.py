import ezconfig.config
import testdata
import os
from pathlib import Path

def test_some_thing():
    test_fn = testdata.get_default_test_config_filename()
    test_dir = Path(test_fn).absolute().parent
    curr_dir = Path(__file__).absolute().parent

    config = ezconfig.config.Configuration(test_fn)
    config.set_override_basedir(curr_dir)

    assert test_dir != curr_dir

    assert config.get("static_stuff", "test_fn") == "../testdata/default.conf"
    correct_path = str(test_dir / "default.conf")
    assert config.get("static_stuff", "test_fn", is_filename =True) == correct_path

    config.override("static_stuff", "test_fn", "../default.conf")

    override_path = os.path.abspath(os.path.join(curr_dir, "..", "default.conf"))

    print(config.get("static_stuff", "test_fn", is_filename =True))
    assert config.get("static_stuff", "test_fn", is_filename =True) == override_path

    return
