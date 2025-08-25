import json
from pathlib import Path


def test_counts_reasonable():
    metrics_path = Path(__file__).parents[1] / "results" / "metrics.json"
    metrics = json.loads(metrics_path.read_text())
    counts = metrics["counts"]
    assert sum(counts.values()) == metrics["shots"]
    assert set(counts.keys()).issuperset({"0", "1"})
