from typing import Callable, NamedTuple
import pygame


__all__ = [
  "EauTimer"
]


TimerAlarm = NamedTuple('TimerAlarm', [("milliseconds", int), ("callback", Callable[[], None])])


class TimerTask:
  __slots__ = (
    "milliseconds",
    "interval",
    "callback",
    "times_executed"
  )

  def __init__(self, milliseconds: int, interval: int, cb: Callable[[int], bool]) -> None:
    self.milliseconds = milliseconds
    self.interval = interval
    self.callback = cb
    self.times_executed = 0

  def execute(self):
    self.times_executed += 1
    return self.callback(self.interval * self.times_executed)


class EauTimer:
  __slots__ = (
    "_ticks",
    "milliseconds",
    "alarms",
    "tasks",
    "paused"
  )

  def __init__(self) -> None:
    self._ticks = pygame.time.get_ticks()
    self.milliseconds: int = 0
    self.alarms: list[TimerAlarm] = []
    self.tasks: list[TimerTask] = []
    self.paused = False

  @property
  def seconds(self) -> float:
    return self.milliseconds / 1000

  def update(self) -> None:
    if self.paused:
      return
    curr_ticks = pygame.time.get_ticks()
    self.milliseconds += curr_ticks - self._ticks
    self._check_alarms()
    self._check_tasks()
    self._ticks = curr_ticks

  def set_alarm(self, milliseconds: int, cb: Callable[[], None]) -> None:
    self.alarms.append(TimerAlarm(milliseconds=self.milliseconds + milliseconds, callback=cb))

  def _check_alarms(self):
    for alarm in self.alarms:
      if alarm.milliseconds <= self.milliseconds:
        alarm.callback()
        self.alarms.remove(alarm)

  def set_task(self, milliseconds: int, cb: Callable[[int], bool]) -> None:
    self.tasks.append(TimerTask(self.milliseconds + milliseconds, milliseconds, cb))

  def _check_tasks(self):
    for task in self.tasks:
      if task.milliseconds <= self.milliseconds:
        if not task.execute():
          self.tasks.remove(task)
        else:
          task.milliseconds = self.milliseconds + task.interval

  def pause(self):
    self.paused = True

  def unpause(self):
    self._ticks = pygame.time.get_ticks()
    self.paused = False

  def stop(self):
    self.alarms.clear()
    self.tasks.clear()
    del self.alarms
    del self.tasks
    self.paused = True
    del self
