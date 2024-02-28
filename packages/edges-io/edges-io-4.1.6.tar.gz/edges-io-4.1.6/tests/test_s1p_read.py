from pathlib import Path

import numpy as np
from edges_io.io import S1P


def test_s1p_read(datadir: Path):
    fl = (
        datadir / "Receiver01_25C_2019_11_26_040_to_200MHz/S11/Ambient01/External01.s1p"
    )
    s1p = S1P(fl)

    assert np.all(np.iscomplex(s1p.s11))
    assert len(s1p.s11) == len(s1p.freq)


def test_s1_read_db(datadir: Path):
    fl = datadir / "s11_db.s1p"
    s1p = S1P(fl, check=False)

    assert np.all(np.iscomplex(s1p.s11))
    assert len(s1p.s11) == len(s1p.freq)


def test_s2p_read(datadir: Path):
    fl = datadir / "example.s2p"
    s2p, f = S1P.read(fl)
    assert s2p.shape == (len(f), 4)
