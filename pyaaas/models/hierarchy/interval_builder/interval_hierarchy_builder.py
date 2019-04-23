import copy

from pyaaas.models.hierarchy.grouping_based_hierarchy import GroupingBasedHierarchy
from pyaaas.models.hierarchy.interval_builder.interval import Interval


class IntervalHierarchyBuilder(GroupingBasedHierarchy):
    """
    Represents a specific strategy for creating a value generalization hierarchy
    """

    def __init__(self):
        super().__init__()
        self._intervals = {}

    @property
    def intervals(self):
        return list(copy.deepcopy(self._intervals))

    def add_interval(self, from_, to, label: str=None):
        """
        Add a interval to the builder
        from_ is inclusive, to is exclusive

        :param from_: create interval with and from this value
        :param to: create interval to this value
        :param label: (optional) set a string label for the interval
        :return: None

        """
        # using dict to enforce uniqueness and order
        self._intervals[Interval(from_, to, label)] = ""

    def _request_payload(self):
        return {
            "builder": {
                "type": "intervalBased",
                "intervals": [interval.payload() for interval in self._intervals.keys()],
                "levels": [level.payload() for level in self.levels]
            }
        }