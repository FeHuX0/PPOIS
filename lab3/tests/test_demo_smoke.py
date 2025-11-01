
import builtins
from io import StringIO
import sys

from main import run_demo

def test_run_demo_smoke(monkeypatch):
    # Capture stdout to ensure the demo runs without exceptions and prints key lines
    buf = StringIO()
    monkeypatch.setattr(sys, "stdout", buf)
    run_demo()
    out = buf.getvalue()
    assert "Biodiversity richness score" in out
    assert "Alert severity:" in out
    assert "Migration distance for toucan" in out
