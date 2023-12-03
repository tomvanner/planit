from sqlalchemy import Column, DateTime, event, func


class TimeStampMixin(object):
    """Adds timestamps for when a record was created and updated."""

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())

    @staticmethod
    def _updated_at(mapper, connection, target):
        target.updated_at = func.now()

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, "before_update", cls._updated_at)