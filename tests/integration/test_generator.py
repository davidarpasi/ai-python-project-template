import shutil
import subprocess
from pathlib import Path

import pytest
import yaml
from copier import run_copy, run_update

ROOT = Path(__file__).resolve().parents[2]


def git(directory: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(directory), *args], check=True, capture_output=True)


def initialise(directory: Path) -> None:
    git(directory, "init", "-b", "main")
    git(directory, "config", "user.name", "Template test")
    git(directory, "config", "user.email", "template-test@example.invalid")
    git(directory, "add", ".")
    git(directory, "commit", "-m", "Initial test fixture")


def test_generated_names_answers_and_update(tmp_path: Path) -> None:
    source = tmp_path / "source"
    source.mkdir()
    shutil.copy(ROOT / "copier.yml", source / "copier.yml")
    shutil.copytree(ROOT / "template", source / "template")
    initialise(source)
    git(source, "tag", "v0.1.0")
    destination = tmp_path / "service"
    run_copy(
        str(source),
        destination,
        data={
            "project_name": "Network Helper",
            "project_slug": "network-helper",
            "package_name": "network_helper",
            "project_description": "A test fixture.",
        },
        vcs_ref="v0.1.0",
        defaults=True,
        quiet=True,
    )
    answers = yaml.safe_load((destination / ".copier-answers.yml").read_text())
    assert answers["package_name"] == "network_helper"
    assert answers["_src_path"] == str(source)
    assert answers["_commit"] == "v0.1.0"
    assert (destination / "src/network_helper/__main__.py").is_file()
    assert not list(destination.rglob("*.jinja"))
    initialise(destination)
    (source / "template/template-update.txt").write_text("A template update.\n")
    git(source, "add", ".")
    git(source, "commit", "-m", "Add update fixture")
    git(source, "tag", "v0.2.0")
    run_update(destination, vcs_ref="v0.2.0", defaults=True, quiet=True, overwrite=True)
    assert (destination / "template-update.txt").read_text() == "A template update.\n"
    assert (
        yaml.safe_load((destination / ".copier-answers.yml").read_text())["package_name"]
        == "network_helper"
    )


@pytest.mark.parametrize(
    "field,value",
    [
        ("project_slug", "../escape"),
        ("project_slug", "invalid name"),
        ("package_name", "bad-name"),
        ("package_name", "class"),
    ],
)
def test_invalid_names_are_rejected(tmp_path: Path, field: str, value: str) -> None:
    with pytest.raises(ValueError, match="Validation error"):
        run_copy(str(ROOT), tmp_path / "invalid", data={field: value}, defaults=True, quiet=True)
