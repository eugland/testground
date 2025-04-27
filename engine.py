#!/usr/bin/env python
"""
Append commits described in <commits.json> to an existing Git repository.

Usage
------
python add_commits.py --json commits.json [--repo /path/to/repo] [--file rel/path.py]

• --json  : required, JSON list of {"message": "...", "content": "..."} entries
• --repo  : optional, defaults to the current directory
• --file  : optional, file to overwrite each commit, defaults to 'game.py'
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from git import Repo, Actor, InvalidGitRepositoryError

AUTHOR = Actor("Bisect Demo Bot", "demo@example.com")


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True, help="JSON file with commit list")
    ap.add_argument("--repo", default=".", help="Path to existing repo (cwd default)")
    ap.add_argument("--file", default="game.py", help="Repo-relative file to write")
    return ap.parse_args()


def ensure_repo(path: Path) -> Repo:
    try:
        return Repo(path)
    except InvalidGitRepositoryError:
        sys.exit(f"Error: {path} is not a Git repository. Initialise it first.")


def load_commits(json_path: Path):
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
        assert isinstance(data, list)
    except Exception as exc:
        sys.exit(f"Invalid JSON commit list: {exc}")
    for entry in data:
        if not {"message", "content"} <= entry.keys():
            sys.exit("Each JSON object must contain 'message' and 'content'")
    return data


def append_commits(repo: Repo, target_file: Path, commits):
    rel_path = str(target_file.relative_to(repo.working_tree_dir))
    for idx, entry in enumerate(commits, 1):
        target_file.write_text(entry["content"], encoding="utf-8")
        repo.index.add([rel_path])
        repo.index.commit(entry["message"], author=AUTHOR)
        print(f"[{idx}/{len(commits)}] committed: {entry['message']}")
        time.sleep(0.3)  # keep distinct timestamps


def main():
    args = parse_args()
    repo = ensure_repo(Path(args.repo).resolve())
    target = repo.working_tree_dir / Path(args.file)

    commits = load_commits(Path(args.json).resolve())
    append_commits(repo, target, commits)

    print("\nDone. You can now run `git log --oneline` or start `git bisect`.")


if __name__ == "__main__":
    main()
