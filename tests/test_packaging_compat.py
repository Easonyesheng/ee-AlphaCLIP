import ast
from pathlib import Path


def test_pkg_resources_is_not_imported_by_package_or_setup():
    repo_root = Path(__file__).resolve().parents[1]
    paths = [
        repo_root / "setup.py",
        repo_root / "alpha_clip" / "alpha_clip.py",
    ]

    for path in paths:
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
                assert "pkg_resources" not in names
            elif isinstance(node, ast.ImportFrom):
                assert node.module != "pkg_resources"
