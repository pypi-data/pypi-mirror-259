from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol, Union

import typer
from iterfzf import iterfzf  # type: ignore
from rich.console import Console

from .provider import Issue
from .title_parser import parse_issue_title

if TYPE_CHECKING:
    from collections.abc import Sequence

console = Console()


class IssueSelecter(Protocol):
    ten_latest_prompt: str
    manual_prompt: str
    refresh_prompt: str

    def select_issue_dialog(self, issues: "Sequence[Issue]") -> Union[Issue, str]:
        ...


@dataclass(frozen=True)
class DefaultIssueSelecter(IssueSelecter):
    ten_latest_prompt: str = "Recent"
    manual_prompt: str = "Manual"
    refresh_prompt: str = "Refresh..."

    def _show_entry_dialog(self) -> str:
        return typer.prompt("Title")

    def _show_selection_dialog(self, issues: "Sequence[Issue]") -> str:
        issue_titles = [f"{issue.title.content} #{issue.entity_id}" for issue in issues]
        selection: str = iterfzf(
            [self.manual_prompt, *issue_titles, self.refresh_prompt, self.ten_latest_prompt]
        )  # type: ignore
        return selection

    def select_issue_dialog(self, issues: "Sequence[Issue]") -> Union[Issue, str]:
        selected_issue_title = self._show_selection_dialog(issues=issues)

        if selected_issue_title in [self.refresh_prompt, self.ten_latest_prompt]:
            return selected_issue_title

        if selected_issue_title == self.manual_prompt:
            selected_issue_title = self._show_entry_dialog()
            parsed_title = parse_issue_title(selected_issue_title)
            return Issue(entity_id=None, title=parsed_title, description="")

        return next(issue for issue in issues if issue.title.content in selected_issue_title)
