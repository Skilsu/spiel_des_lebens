from abc import ABC, abstractmethod

"""
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
"""


class Player:

    def __init__(self, name="", number=-1, active=False):
        self.name = name
        self.active = active
        self.steps_to_go = 0
        self.player_number = number

        self.moving = False

        self.current_field = 0

        # game logic
        self.money = 0
        self.children = []
        self.status_symbols = []
        self.action_cards = []
        self.car = False
        self.life = False
        self.fire = False
        self.debt = 0
        self.income = 0
        self.pause = False
        self.job = None
        self.aktie = False

    def __str__(self):
        print(f"{self.name=} \n"
              f"{self.active=} \n"
              f"{self.steps_to_go=} \n"
              f"{self.player_number=} \n\n"
              f"{self.moving=} \n\n"
              f"{self.current_field=} \n\n"
              f"game logic"
              f"{self.money=} \n"
              f"{self.children=} \n"
              f"{self.status_symbols=} \n"
              f"{self.action_cards=} \n"
              f"{self.car=} \n"
              f"{self.life=} \n"
              f"{self.fire=} \n"
              f"{self.debt=} \n"
              f"{self.income=} \n"
              f"{self.pause=} \n"
              f"{self.job=} \n"
              f"{self.aktie=} \n")


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
            pass  # TODO add statussymbol


class Income0Action(Action):
    def __init__(self, income):
        self.income = income

    def act(self, player):
        if player.income == 0:
            player.income = self.income


class JobAction(Action):
    def __init__(self, job):
        self.job = job

    def act(self, player):
        player.job = self.job


class AktieAction(Action):
    def act(self, player):
        player.aktie = True  # TODO right implemented???


def create_action(action_dict):
    actions = []
    add_money = action_dict.get("add_money", 0)
    pause = action_dict.get("pause", False)
    set_income = action_dict.get("set_income", 0)
    more_steps = action_dict.get("more_steps", -1)
    add_insurance = action_dict.get("add_insurance", None)
    lose_insurance = action_dict.get("lose_insurance", None)
    payday = action_dict.get("payday", False)
    marriage = action_dict.get("marriage", False)
    buy_statussymbol = action_dict.get("buy_statussymbol", False)
    income_if_0 = action_dict.get("income_if_0", 0)
    job = action_dict.get("job", None)
    aktie = action_dict.get("aktie", False)

    if add_money != 0:
        actions.append(MoneyAction(add_money))
    if pause:
        actions.append(PauseAction())
    if set_income != 0:
        actions.append(IncomeAction(set_income))
    if more_steps != -1:
        actions.append(MoreStepsAction(more_steps))
    if add_insurance is not None:
        actions.append(AddInsuranceAction(add_insurance))
    if lose_insurance is not None:
        actions.append(LoseInsuranceAction(lose_insurance))
    if payday:
        actions.append(PaydayAction())
    if marriage:
        pass  # TODO implement logic
    if buy_statussymbol:
        pass  # TODO implement logic
    if income_if_0 != 0:
        actions.append(Income0Action(income_if_0))
    if job is not None:
        actions.append(JobAction(job))
    if aktie:
        actions.append(AktieAction())
    return actions


player1 = Player("Player 1")
player2 = Player("Player 2")

action_dict1 = {"add_money": 3000,
               "pause": False,
               "set_income": 0,
               "more_steps": -1,
               "add_insurance": "car",
               "lose_insurance": None,
               "payday": False,
               "marriage": False,
               "buy_statussymbol": False,
               "income_if_0": 0,
               "job": None,
               "aktie": False}

action_dict2 = {"add_money": 3000,
                "add_insurance": "car"}

actions1 = create_action(action_dict1)
actions2 = create_action(action_dict2)

for action in actions1:
    action.act(player1)

for action in actions2:
    action.act(player2)

player1.__str__()
player2.__str__()

