from helpers.joke_dict import joke_dict


def create_joke(name, title):
    if title in joke_dict:
        return joke_dict[title] + " " + name
    return joke_dict["Generic"] + " " + name
