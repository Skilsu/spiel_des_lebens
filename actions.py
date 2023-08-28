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


class PauseAction(Action):
    def act(self, player):
        player.pause = not player.pause


class IncomeAction(Action):
    def __init__(self, income):
        self.income = income

    def act(self, player):
        player.income = self.income


class MoreStepsAction(Action):
    def __init__(self, steps):
        self.steps = steps

    def act(self, player):
        player.steps_to_go = self.steps


class AddInsuranceAction(Action):
    def __init__(self, insurance):
        self.insurance = insurance

    def act(self, player):
        if self.insurance == "car":
            player.car = True
        elif self.insurance == "life":
            player.life = True
        elif self.insurance == "fire":
            player.fire = True


class LoseInsuranceAction(Action):
    def __init__(self, insurance):
        self.insurance = insurance

    def act(self, player):
        if self.insurance == "car":
            player.car = False
        elif self.insurance == "life":
            player.life = False
        elif self.insurance == "fire":
            player.fire = False


class PaydayAction(Action):
    def act(self, player):
        player.money += player.income


class MarriageAction(Action):
    def act(self, player):
        pass  # TODO implement logic???


class GetStatussymbolAction(Action):
    def __init__(self, statussymbol):
        self.statussymbol = statussymbol

    def act(self, player):
        if len(player.status_symbols) < 3:
            player.wefnjpi  # TODO add statussymbol


def create_action(self, add_money=0, pause=False, set_income=0, more_steps=-1, add_insurance=None, lose_insurance=None,
                  payday=False, marriage=False, buy_statussymbol=False, income_if_0=0, job=None, aktie=False):
    actions = []
    if add_money is not 0:
        actions.append(MoneyAction(money=add_money))
    if pause:
        actions.append(PauseAction())
    if set_income is not 0:
        actions.append(IncomeAction(set_income))
    if more_steps is not -1:
        actions.append(MoreStepsAction(more_steps))
    if add_insurance is not None:
        actions.append(AddInsuranceAction(add_insurance))
    if lose_insurance is not None:
        actions.append(LoseInsuranceAction(lose_insurance))
    if payday:
        actions.append(PaydayAction())

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
