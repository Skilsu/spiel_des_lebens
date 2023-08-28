class Field:
    def __init__(self, following_fields, x, y, rotation, action, title="", text="") -> None:
        self.title = title
        self.text = text
        self.following_fields = following_fields

        self.x = x
        self.y = y
        self.rotation = rotation

        self.action = action  # [MoneyAction(3000), InsuranceAction("car")]

    def __str__(self):
        return f"{self.title}, {self.text}, {self.following_fields}, {self.x}, {self.y}, {self.rotation}, {self.action}"

    def get_following_field(self):
        if len(self.following_fields) > 1:
            return self.following_fields[0]  # TODO choice implementieren???
        else:
            return self.following_fields[0]

    def choice_options(self):
        return None

    def return_choice(self, choice):
        pass

    def get_actions(self, player):
        if player.steps_to_go == 0:
            return self.action
        else:
            return []


class YellowField(Field):
    def __init__(self, following_fields, x, y, rotation, action, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, action, title, text)


class OrangeField(Field):
    def __init__(self, following_fields, x, y, rotation, action, amount_of_money=0, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, action, title, text)
        self.chosen_player = -1

    def act(self, left_moves):
        left_moves = super().act(left_moves)
        if left_moves > 0:
            return left_moves
        else:
            pass
            # TODO wähle einen anderen spieler
            # TODO ziehe diesem Spieler self.amount_of_money ab und addiere es bei dir

    def choice_options(self):
        return ["player"]

    def return_choice(self, choice):
        self.chosen_player = choice

    def get_actions(self, player):
        actions = super().get_actions(player)


class WhiteField(Field):
    def __init__(self, following_fields, x, y, rotation, action, title="", text="", choice_text="") -> None:
        super().__init__(following_fields, x, y, rotation, action, title, text)
        self.wants_to_act = True
        self.choice_text = choice_text

    def choice_options(self):
        return {"type": "bool",
                "choice_text": self.choice_text}

    def return_choice(self, choice):
        if choice:
            self.wants_to_act = True
        else:
            self.wants_to_act = False

    def get_actions(self, player):
        if self.wants_to_act:
            return self.action
        else:
            return []


class RedField(Field):
    def __init__(self, following_fields, x, y, rotation, action, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, action, title, text)

    def act(self, left_moves):
        left_moves = super().act(left_moves)
        # TODO do what has to be done
        return left_moves

    def get_actions(self):
        return self.action
