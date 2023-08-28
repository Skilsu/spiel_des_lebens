

statussymbols = [["Rolls Royce", "Millionärs-Einkommen aus Vermietung", 1000],
                 ["Villa in Südfrankreich", "Millionärs-Einkommen aus Vermietung", 2000],
                 ["Kunstsammlung", "Millionärs-Einkommen aus Ausstellungen", 3000],
                 ["Rennpferde", "Millionärs-Einkommen aus Geldpreisen", 3000],
                 ["Luxus-Yacht", "Millionärs-Einkommen aus Charteraufträgen", 4000],
                 ["Privat-Jet", "Millionärs-Einkommen aus Charterflügen", 4000]]


class Statussymbol:
    def __init__(self, title, description, value):
        self.title = title
        self.description = description
        self.value = value

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description + " " + self.value

