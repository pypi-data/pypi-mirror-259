import abc

from runloop.manifest.manifest import FunctionInvocation


class Scheduler(abc.ABC):
    """The Runloop Scheduler provides the ability to schedule `function` invocation at a given time in the future.
    # TODO: Flesh out use cases, consider place among other event primitives.
    """

    def schedule_at_time(self, function_invocation: FunctionInvocation, scheduled_time_ms: int):
        """Schedule a function to be executed."""
        raise NotImplementedError()
