from project import CelestialObject

def test_url():
    object1 = CelestialObject("neptune")
    assert object1.url() == "https://theskylive.com/neptune-info"
    object2 = CelestialObject("uranus")
    assert object2.url() == "https://theskylive.com/uranus-info"
    object3 = CelestialObject("saturn")
    assert object3.url() == "https://theskylive.com/saturn-info"

def test_userchoice():
    object1 = CelestialObject("sun")
    assert object1.userchoice() == "sun"
    object2 = CelestialObject("mars")
    assert object2.userchoice() == "mars"
    object3 = CelestialObject("venus")
    assert object3.userchoice() == "venus"


def test_label():
    object1 = CelestialObject("sun")
    assert object1.label() == object1._maincontent.find_all("label")
    object2 = CelestialObject("mars")
    assert object2.label() == object2._maincontent.find_all("label")
    object3 = CelestialObject("venus")
    assert object3.label() == object3._maincontent.find_all("label")

