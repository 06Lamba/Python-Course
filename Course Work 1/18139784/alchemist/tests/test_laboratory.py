import yaml
import pytest
import os
from ..laboratory import Laboratory


def read_fixture(fix):
    with open(os.path.join(os.path.dirname(__file__), 'fixtures',
                           fix)) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
    return fixtures


@pytest.mark.parametrize("fixture1", read_fixture('fixtures_pos.yml'))
def test_run_full_experiment1(fixture1):
    Lab = Laboratory()
    answer1, answer2 = fixture1.pop('answer')
    shelf1, shelf2, count = Lab.run_full_experiment(fixture1)
    assert [sorted(shelf1), sorted(shelf2)] == [sorted(answer1),
                                                sorted(answer2)]


@pytest.mark.parametrize("fixture2", read_fixture('fixtures_neg.yml'))
def test_run_full_experiment2(fixture2):
    Lab = Laboratory()
    with pytest.raises(ValueError):
        Lab.run_full_experiment(fixture2)
