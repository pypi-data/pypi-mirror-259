"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 31/12/2023
@Description  :
"""

import argparse
from pathlib import Path

from ..rich_logger import set_up_logging
from .readme_handler import MarkdownHandler


def print_help() -> None:
    help_text = """
    Usage:
    poetry run markdown --root ROOT
    generate_nav  --title TITLE
    modify_recent --num_commits  --title TITLE
    convert_wiki_links
    """
    print(help_text)


def main(args=None) -> None:
    set_up_logging()
    parser = argparse.ArgumentParser(
        description="Markdown Handling Tool", add_help=False
    )
    parser.add_argument(
        "action",
        help="Action to perform",
        choices=["generate_nav", "modify_recent", "convert_wiki_links"],
        nargs="?",
    )
    parser.add_argument("--output", help="Output markdown file", type=str)
    parser.add_argument("--dir", help="Target directory", type=str)
    parser.add_argument("--title", help="Title for the section in markdown", type=str)
    parser.add_argument(
        "--num_commits", help="Number of commits for recent modifications", type=int
    )
    parser.add_argument(
        "--root", help="Root directory", type=str, default=Path.cwd().as_posix()
    )
    parser.add_argument(
        "-h", "--help", action="store_true", help="Show this help message and exit"
    )

    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    if args.help or args.action is None:
        print_help()
        return

    handler = MarkdownHandler(args.root)

    if args.action == "generate_nav":
        handler.generate_nav_links(args.title)
    elif args.action == "modify_recent":
        handler.generate_recently_modified_from_git(args.num_commits, args.title)
    elif args.action == "convert_wiki_links":
        handler.convert_wiki_links_in_dir()


if __name__ == "__main__":
    main()
