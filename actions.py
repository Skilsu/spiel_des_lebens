from abc import ABC, abstractmethod


class Action(ABC):

    @abstractmethod
    def act(self, player):
        pass


class MoneyAction(Action):
    def __init__(self, money):
        self.money = money

    def act(self, player):
        player.add_money(self.money)


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
        player.steps_to_go += self.steps


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
        player.add_money(player.income)


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

class ChoiceInFieldAction(Action):
    def act(self, player):
        player.choosing_in_field = True

def create_action(action_dict):
    actions = []

    if "choice_in_field" in action_dict:
        actions.append(ChoiceInFieldAction())
    if "add_money" in action_dict:
        actions.append(MoneyAction(action_dict["add_money"]))
    if "pause" in action_dict:
        actions.append(PauseAction())
    if "set_income" in action_dict:
        actions.append(IncomeAction(action_dict["set_income"]))
    if "more_steps" in action_dict:
        actions.append(MoreStepsAction(action_dict["more_steps"]))
    if "add_insurance" in action_dict:
        actions.append(AddInsuranceAction(action_dict["add_insurance"]))
    if "lose_insurance" in action_dict:
        actions.append(LoseInsuranceAction(action_dict["lose_insurance"]))
    if "payday" in action_dict:
        actions.append(PaydayAction())
    if "buy_statussymbol" in action_dict:
        pass  # TODO implement logic
    if "income_if_0" in action_dict:
        actions.append(Income0Action(action_dict["income_if_0"]))
    if "job" in action_dict:
        actions.append(JobAction(action_dict["job"]))
    if "aktie" in action_dict:
        actions.append(AktieAction())

    return actions

