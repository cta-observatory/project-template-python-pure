def test_version():
    from template import __version__

    assert __version__ != "0.0.0"
