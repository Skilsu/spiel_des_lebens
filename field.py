

class Field:
    def __init__(self, following_fields, x, y, title="", text="") -> None:
        if title == "":
            self.title = None
        else:
            self.title = title
        if text == "":
            self.text = None
        else:
            self.text = text
        # self.following_fields = following_fields  # TODO just a first idea

    def move(self, left_moves):
        return left_moves - 1


class YellowField(Field):
    def __init__(self, following_fields, x, y) -> None:
        super().__init__(following_fields, x, y)

    def move(self, left_moves):
        left_moves = super().move(left_moves)
        if left_moves > 0:
            return left_moves
        else:
            # TODO do something
            return 0
            pass


class OrangeField(Field):
    def __init__(self, following_fields, x, y, amount_of_money) -> None:
        super().__init__(following_fields, x, y)
        self.amount_of_money = amount_of_money

    def move(self, left_moves):
        left_moves = super().move(left_moves)
        if left_moves > 0:
            return
        else:
            self.text = "Klage auf Schadenersatz. Dir werden " + self.amount_of_money + " zugesprochen."
            # TODO wähle einen anderen spieler
            # TODO ziehe diesem Spieler self.amount_of_money ab und addiere es bei dir


class WhiteField(Field):
    def __init__(self, following_fields, x, y) -> None:
        super().__init__(following_fields, x, y)

    def move(self, left_moves, wants_to_act):
        left_moves = super().move(left_moves)
        if wants_to_act:
            # TODO do what to do
            pass
        else:
            return


class RedField(Field):
    def __init__(self, following_fields, x, y) -> None:
        super().__init__(following_fields, x, y)

    def move(self, left_moves):
        left_moves = super().move(left_moves)
        # TODO do what has to be done
        return left_moves


class StopField(Field):
    def __init__(self, following_fields, x, y) -> None:
        super().__init__(following_fields, x, y)

    def move(self, left_moves):
        left_moves = super().move(left_moves)
        # TODO do what has to be done
        return 0


class CustomsField(Field):
    def __init__(self, following_fields, x, y) -> None:
        super().__init__(following_fields, x, y)
        self.first_player = False

    def move(self, left_moves):
        left_moves = super().move(left_moves)
        if self.first_player:
            # TODO: Add code for the first player's move
            pass
        else:
            # TODO: Add code for the other players' move
            pass