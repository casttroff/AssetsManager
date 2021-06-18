import logging

class OnlyFilter(logging.Filter):
  """
    Filter only when levelno is equals to pre-established one.
  """

  def __init__(self, levelno):
    super(OnlyFilter, self).__init__()
    self.levelno = eval(levelno)

  def filter(self, record):
    return record.levelno == self.levelno

class LessThanFilter(logging.Filter):
  """
    Filter only when levelno is less than pre-established one.
  """

  def __init__(self, levelno):
    super(LessThanFilter, self).__init__()
    self.levelno = eval(levelno)

  def filter(self, record):
    return record.levelno < self.levelno
