from helpers.create_joke import create_joke


def test_create_joke():
    assert create_joke("jd", "CEO") == "Chief Happiness Officer" + " " + "jd"


def test_create_joke1():
    assert create_joke("jd", "Software") == "Rockstar" + " " + "jd"


# def test_create_joke2():
#     assert create_joke("jd", "ceo") == "Chief Happiness Officer" + " " + "jd"
