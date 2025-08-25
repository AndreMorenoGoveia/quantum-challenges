import json
from pathlib import Path


def test_bv_result():
    # Load metrics.json from the results directory
    metrics_path = Path(__file__).resolve().parents[2] / 'results' / 'metrics.json'
    assert metrics_path.exists(), 'metrics.json not found in results directory'

    metrics = json.loads(metrics_path.read_text())
    shots = metrics.get('shots')
    counts = metrics.get('counts')

    # Ensure total counts equal number of shots
    assert sum(counts.values()) == shots

    # Verify that the expected secret bitstring appears in the counts
    expected_secret = '101'
    assert expected_secret in counts, f"Expected secret {expected_secret} not found in counts: {counts}"
