class Field:
    def __init__(self, following_fields, x, y, rotation, actions, color, title="", text="", ) -> None:
        self.title = title
        self.text = text
        self.following_fields = following_fields

        self.x = x
        self.y = y
        self.rotation = rotation

        self.actions = actions  # [MoneyAction(3000), InsuranceAction("car")]

        self.color = color

    def __str__(self):
        return f"{self.title}, {self.text}, {self.following_fields}, {self.x}, {self.y}, {self.rotation}, {self.actions}"

    def get_following_field(self, following_field_number=0):
        return self.following_fields[following_field_number]

    def get_actions(self):
        return self.actions


class YellowField(Field):
    def __init__(self, following_fields, x, y, rotation, actions, color, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, actions, color, title, text)


class OrangeField(Field):
    def __init__(self, following_fields, x, y, rotation, actions, color, amount_of_money=0, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, actions, color, title, text)




class WhiteField(Field):
    def __init__(self, following_fields, x, y, rotation, actions, color, title="", text="", choice_text="") -> None:
        super().__init__(following_fields, x, y, rotation, actions, color, title, text)




class RedField(Field):
    def __init__(self, following_fields, x, y, rotation, actions, color, title="", text="") -> None:
        super().__init__(following_fields, x, y, rotation, actions, color, title, text)


