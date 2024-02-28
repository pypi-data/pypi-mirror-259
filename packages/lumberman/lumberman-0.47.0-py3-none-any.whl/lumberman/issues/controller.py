from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from rich.progress import Progress, SpinnerColumn, TextColumn

if TYPE_CHECKING:
    from collections.abc import Sequence

    from .provider import Issue, IssueProvider
    from .selecter import IssueSelecter


@dataclass(frozen=True)
class IssueController:
    view: "IssueSelecter"
    provider: "IssueProvider"
    in_progress_label: str

    def _get_latest_issues(self) -> "Sequence[Issue]":
        with Progress(
            SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True
        ) as progress:
            progress.add_task("Getting latest issues", start=True)
            latest_issues = self.provider.get_latest_issues(
                in_progress_label=self.in_progress_label
            )

        if not latest_issues:
            return []

        return latest_issues

    def _get_my_issues(self) -> "Sequence[Issue]":
        with Progress(
            SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True
        ) as progress:
            progress.add_task("Getting issues assigned to you", start=True)
            my_issues = self.provider.get_issues_assigned_to_me(
                in_progress_label=self.in_progress_label
            )

        return my_issues

    def label_issue_in_progress(self, issue: "Issue"):
        self.provider.label_issue(issue, label=self.in_progress_label)

    def select_issue(self, issues: Optional["Sequence[Issue]"] = None) -> "Issue":
        if not issues:
            issues = [*self._get_my_issues(), *self._get_latest_issues()]

        selected_issue = self.view.select_issue_dialog(issues)

        if selected_issue is self.view.refresh_prompt:
            return self.select_issue()
        if selected_issue is self.view.ten_latest_prompt:
            return self.select_issue(self._get_latest_issues())
        if isinstance(selected_issue, str):
            raise NotImplementedError(f"Command {selected_issue} not implemented")

        return selected_issue
