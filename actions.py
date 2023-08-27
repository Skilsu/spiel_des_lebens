from abc import ABC, abstractmethod

ACTIONS_Vorlage = [{"act with more steps": False,
                    "add_money": 0,
                    "pause": False,
                    "set_income": 0,
                    "more_steps": 0,  # -1 = planned, 0 = stay, number = go directed
                    "add_insurance": None,  # "car", "fire", "life"
                    "lose_insurance": None,
                    "payday": False,
                    "marriage": False,
                    "buy_statussymbol": False,
                    "income_if_0": 0,
                    "job": None,
                    "aktie": False
                    }]

actions = \
    [[False, 3000, False, 0, -1, "car", None, False, False, False, 0, None, False]]  # + 3.000 und Autoversicherung   #0


class Action(ABC):

    @abstractmethod
    def act(self, player):
        pass


class MoneyAction(Action):
    def __init__(self, money):
        self.money = money

    def act(self, player):
        player.money += self.money


class InsuranceAction(Action):
    def __init__(self, insurance):
        self.insurance = insurance

    def act(self, player):
        player. += self.insurance

class PauseAction(Action):
    def act(self, player):
        player.pause = not player.pause


def create_action(self, add_money=0, pause=False, set_income=0, more_steps=-1, add_insurance=None, lose_insurance=None,
                  payday=False, marriage=False, buy_statussymbol=False, income_if_0=0, job=None, aktie=False):
    actions = []
    if add_money is not 0:
        actions.append(MoneyAction(money=add_money))

    if pause:
        actions.append(PauseAction())

    if add_insurance is not None:
        actions.append()

    self.set_income = set_income
    self.more_steps = more_steps
    self.add_insurance = add_insurance
    self.lose_insurance = lose_insurance
    self.payday = payday
    self.marriage = marriage
    self.buy_statussymbol = buy_statussymbol
    self.income_if_0 = income_if_0
    self.job = job
    self.aktie = aktie
    return actions


