from __future__ import annotations

from typing import Tuple

from pabutools.utils import Numeric
from pabutools.election import Project
from pabutools.rules.budgetallocation import AllocationDetails


class ProjectLoss(Project):
    """
    Class used to represent the projects and how much budget they lost due to other projects being picked.
    This extends the :py:class:`~pabutools.election.instance.Project` and thus represents the project itself.

    Parameters
    ----------
        project: :py:class:`~pabutools.election.instance.Project`
            Project for which analytics is calculated.
        supporters_budget: :py:class:`~pabutools.utils.Numeric`
            The collective budget of the project supporters when project was considered by a rule.
        budget_lost: dict[:py:class:`~pabutools.election.instance.Project`, :py:class:`~pabutools.utils.Numeric`]
            Describes the amount of budget project supporters spent on other projects prior to this
            projects' consideration.

    Attributes
    ----------
        supporters_budget: :py:class:`~pabutools.utils.Numeric`
            The collective budget of the project supporters when project was considered by rule.
        budget_lost: dict[:py:class:`~pabutools.election.instance.Project`, :py:class:`~pabutools.utils.Numeric`]
            Describes the amount of budget project supporters spent on other projects prior to this
            projects' consideration.
    """

    def __init__(
        self,
        project: Project,
        supporters_budget: Numeric,
        budget_lost: dict[Project, Numeric],
    ):
        Project.__init__(
            self, project.name, project.cost, project.categories, project.targets
        )
        self.supporters_budget: Numeric = supporters_budget
        self.budget_lost: dict[Project, Numeric] = budget_lost

    def total_budget_lost(self) -> Numeric:
        """
        Returns the total budget spent by project supporters on prior projects.

        Returns
        -------
            :py:class:`~pabutools.utils.Numeric`
                The total budget spent.
        """
        return sum(self.budget_lost.values())

    def __str__(self):
        return f"ProjectLoss[{self.name}, {float(self.supporters_budget)}, {self.total_budget_lost()}]"

    def __repr__(self):
        return f"ProjectLoss[{self.name}, {float(self.supporters_budget)}, {self.total_budget_lost()}]"


def calculate_project_loss(
    allocation_details: AllocationDetails, verbose: bool = False
) -> list[ProjectLoss]:
    """Returns a list of :py:class:`~pabutools.analysis.projectloss.ProjectLoss` objects for the projects.

    Parameters
    ----------
        allocation_details: :py:class:`~pabutools.rules.budgetallocation.AllocationDetails`
            The details of the budget allocation considered.
        verbose: bool, optional
            (De)Activate the display of additional information.
            Defaults to `False`.

    Returns
    -------
        list[:py:class:`~pabutools.analysis.projectloss.ProjectLoss`]
            List of :py:class:`~pabutools.analysis.projectloss.ProjectLoss` objects.

    """
    if not all(
        hasattr(allocation_details, attr)
        for attr in ["iterations", "initial_budget_per_voter", "voter_multiplicity"]
    ):
        raise ValueError(
            "Provided budget allocation details do not support calculating project loss. The allocation_details "
            "should have an 'iterations', 'initial_budget_per_voter' and 'voter_multiplicity' attributes."
        )
    if len(allocation_details.iterations) == 0:
        if verbose:
            print(f"Rule did not have any iterations, returning empty list")
        return []

    project_losses = []
    voter_count = len(allocation_details.iterations[0].voters_budget)
    voter_multiplicity = allocation_details.voter_multiplicity
    voter_spendings: dict[int, list[Tuple[Project, Numeric]]] = {}
    for idx in range(voter_count):
        voter_spendings[idx] = []

    current_voters_budget = [
        allocation_details.initial_budget_per_voter for _ in range(voter_count)
    ]

    for iteration in allocation_details.iterations:
        if verbose:
            print(
                f"Considering: {iteration.project.name}, status: {iteration.was_picked}"
            )
        budget_lost = {}
        for idx in iteration.supporter_indices:
            spending = voter_spendings[idx]
            for project, spent in spending:
                if project not in budget_lost.keys():
                    budget_lost[project] = 0
                budget_lost[project] = (
                    budget_lost[project] + spent * voter_multiplicity[idx]
                )
        project_losses.append(
            ProjectLoss(
                iteration.project,
                sum(
                    current_voters_budget[i] * voter_multiplicity[i]
                    for i in iteration.supporter_indices
                ),
                budget_lost,
            )
        )
        if iteration.was_picked:
            for supporter_idx in iteration.supporter_indices:
                voter_spendings[supporter_idx].append(
                    (
                        iteration.project,
                        current_voters_budget[supporter_idx]
                        - iteration.voters_budget[supporter_idx],
                    )
                )
            current_voters_budget = iteration.voters_budget

    return project_losses
