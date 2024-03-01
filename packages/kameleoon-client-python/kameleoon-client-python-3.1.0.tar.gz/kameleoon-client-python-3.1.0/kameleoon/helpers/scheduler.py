"""Helper class for scheduling multiple repetitive jobs"""

import time
from logging import Logger
from typing import Any, Callable, Dict, Optional
from kameleoon.helpers.repeat_timer import RepeatTimer


class Scheduler:
    """
    `Scheduler` is a helper class for scheduling multiple repetitive jobs.

    The usage order:
    1. Initialize an instance of `Scheuler`
    2. Schedule multiple jobs with `schedule_job` method
    3. Get an instance of `RepeatTimer` which will trigger job execution, with `timer` method
    4. Start the timer
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        self.__jobs: Dict[str, Scheduler.Job] = {}
        self.__logger = logger

    def schedule_job(self, key: str, interval: float, func: Callable[[], Any]) -> None:
        """
        Schedules a job.

        Should be called before the timer is started.
        """
        self.__jobs[key] = Scheduler.Job(time.time(), interval, func)

    def timer(self) -> RepeatTimer:
        """
        Retunrns an instance of `RepeatTimer` which will trigger job execution, with `timer` method.

        Should not be called more than once.
        """
        interval = self.__get_new_interval()
        return RepeatTimer(interval, self.__trigger)

    def __get_new_interval(self) -> float:
        now = time.time()
        return max(0.0, min(job.next_trigger_time for job in self.__jobs.values()) - now)

    def __trigger(self) -> float:
        now = time.time()
        for key, job in self.__jobs.items():
            if job.next_trigger_time <= now:
                try:
                    job.trigger()
                except Exception as err:  # pylint: disable=W0703
                    if self.__logger:
                        self.__logger.error(f"Error occurred within '{key}' job: {err}")
        return self.__get_new_interval()

    class Job:
        """`Job` represents a scheduled job"""

        def __init__(self, now: float, interval: float, func: Callable[[], Any]) -> None:
            self.interval = interval
            self.func = func
            self.next_trigger_time = now + interval

        def trigger(self) -> None:
            """Schedules the next execution and calls the function"""
            self.next_trigger_time += self.interval
            self.func()
