import inspect

from roboquant.journals.journal import Journal


class BasicJournal(Journal):
    """Tracks a number of basic metrics:
    - total number of events, items, signals and orders until that time
    - total pnl percentage

    This journal adds little overhead to a run, both CPU and memory wise.
    """

    def __init__(self):
        self.items = 0
        self.orders = 0
        self.signals = 0
        self.events = 0
        self.pnl = 0.0
        self.__first_equity = None

    def track(self, event, account, signals, orders):
        if self.__first_equity is None:
            self.__first_equity = account.equity

        self.items += len(event.items)
        self.orders += len(orders)
        self.events += 1
        self.signals += len(signals)
        self.pnl = account.equity / self.__first_equity - 1.0

    def __repr__(self) -> str:
        result = f"""
            events : {self.events}
            items  : {self.items}
            signals: {self.signals}
            orders : {self.orders}
            pnl    : {self.pnl * 100:_.2f}%
        """
        return inspect.cleandoc(result)
