import credit_pd
from credit_pd import config


def test_version():
    assert credit_pd.__version__


def test_split_years_do_not_overlap():
    sets = [set(config.TRAIN_YEARS), set(config.VALID_YEARS), set(config.TEST_YEARS)]
    assert not (sets[0] & sets[1] or sets[0] & sets[2] or sets[1] & sets[2])
