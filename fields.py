

class Field:
    def __init__(self, following_fields, x, y, rotation, action, title="", text="") -> None:
        self.title = title
        self.text = text
        self.following_fields = following_fields

        self.x = x
        self.y = y
        self.rotation = rotation

        self.action = action

    def act(self, left_moves):
        return left_moves - 1

    def get_following_field(self):
        if len(self.following_fields) > 1:
            return self.following_fields[0]  # TODO choice implementieren
        else:
            return self.following_fields[0]

    def __str__(self):
        return f"{self.title}, {self.text}, {self.following_fields}, {self.x}, {self.y}, {self.rotation}, {self.action}"


class YellowField(Field):
    def __init__(self, following_fields, x, y, rotation, action, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, action, title, text)

    def act(self, left_moves):
        left_moves = super().act(left_moves)
        if left_moves > 0:
            return left_moves
        else:
            # TODO do something
            pass


class OrangeField(Field):
    def __init__(self, following_fields, x, y, rotation, action, amount_of_money=0, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, action, title, text)
        # self.amount_of_money = amount_of_money
        # self.text = "Klage auf Schadenersatz. Dir werden " + self.amount_of_money + " zugesprochen."
        # TODO decide if useful

    def act(self, left_moves):
        left_moves = super().act(left_moves)
        if left_moves > 0:
            return left_moves
        else:
            pass
            # TODO wähle einen anderen spieler
            # TODO ziehe diesem Spieler self.amount_of_money ab und addiere es bei dir


class WhiteField(Field):
    def __init__(self, following_fields, x, y, rotation, action, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, action, title, text)

    def act(self, left_moves):
        left_moves = super().act(left_moves)
        wants_to_act = True  # TODO Does he want???
        if wants_to_act:
            # TODO do what to do
            pass
        else:
            return left_moves


class RedField(Field):
    def __init__(self, following_fields, x, y, rotation, action, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, action, title, text)

    def act(self, left_moves):
        left_moves = super().act(left_moves)
        # TODO do what has to be done
        return left_moves
