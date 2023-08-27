import json

from fields import WhiteField, OrangeField, YellowField, RedField

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)


def load_fields():
    with open("fields.json", "r") as infile:
        json_dict = json.load(infile)

    fields = []

    for info in json_dict["fields"]:
        if info["color"] == list(RED):
            fields.append(RedField(following_fields=info["following_fields"],
                                   x=info["x"],
                                   y=info["y"],
                                   rotation=info["rotation"],
                                   action=info["action"],
                                   title=info["title"],
                                   text=info["text"]
                                   ))

        elif info["color"] == list(YELLOW):
            fields.append(YellowField(following_fields=info["following_fields"],
                                      x=info["x"],
                                      y=info["y"],
                                      rotation=info["rotation"],
                                      action=info["action"],
                                      title=info["title"],
                                      text=info["text"]
                                      ))

        elif info["color"] == list(WHITE):
            fields.append(WhiteField(following_fields=info["following_fields"],
                                     x=info["x"],
                                     y=info["y"],
                                     rotation=info["rotation"],
                                     action=info["action"],
                                     title=info["title"],
                                     text=info["text"]
                                     ))

        elif info["color"] == list(ORANGE):
            fields.append(OrangeField(following_fields=info["following_fields"],
                                      x=info["x"],
                                      y=info["y"],
                                      rotation=info["rotation"],
                                      action=info["action"],
                                      title=info["title"],
                                      text=info["text"]
                                      ))
    return fields
