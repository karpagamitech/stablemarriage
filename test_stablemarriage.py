import pytest
import stablemarriage

def test_huf(capfd):
    stablemarriage.main()
    out, err = capfd.readouterr()
    print(out)
    a="Woman  Man\n3   0\n4   2\n5   1\n"
    assert str(out) == a