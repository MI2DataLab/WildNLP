from wildnlp.datasets import SampleDataset
from wildnlp.aspects import Reverser


def test_apply_reverser():
    dataset = SampleDataset()
    dataset.load()

    modified = dataset.apply(Reverser())

    assert len(modified) == 2
    assert modified[0].split()[0] == "gninnaM"
