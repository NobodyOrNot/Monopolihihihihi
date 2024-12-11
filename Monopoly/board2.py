class Property:
    def __init__(self, name, color, color_set_size=None, price=None, owner="bank", rent=None, all_color_set=False, house=None, house_count=0, mortgage=None, stop=0):
        self.name = name
        self.color = color
        self.color_set_size = color_set_size
        self.price = price
        self.owner = owner
        self.rent = rent
        self.all_color_set = all_color_set
        self.house = house
        self.house_count = house_count
        self.mortgage = mortgage
        self.stop = stop

plateau = {
    0: Property(name="depart", color="lightgrey"),
    1: Property(name="belleville", color="brown", color_set_size=2, price=60, rent=[2, 10, 30, 90, 160, 250], house=50, mortgage=30),
    2: Property(name="communaute", color="lightcoral"),
    3: Property(name="lecourbe", color="brown", color_set_size=2, price=60, rent=[4, 20, 60, 180, 320, 450], house=50, mortgage=30),
    4: Property(name="impots", color="darkgrey"),
    5: Property(name="montparnasse", color="black", color_set_size=4, price=200, rent=[25, 50, 100, 200]),
    6: Property(name="vaugirard", color="cyan", color_set_size=3, price=100, rent=[5, 30, 90, 270, 400, 550], house=50, mortgage=50),
    7: Property(name="chance", color="lightcoral"),
    8: Property(name="courcelles", color="cyan", color_set_size=3, price=100, rent=[5, 30, 90, 270, 400, 550], house=50, mortgage=50),
    9: Property(name="republique", color="cyan", color_set_size=3, price=120, rent=[8, 40, 100, 300, 450, 600], house=50, mortgage=60),
    10: Property(name="en-prison", color="lightgrey"),
    11: Property(name="villette", color="violet", color_set_size=3, price=140, rent=[10, 50, 150, 450, 625, 750], house=100, mortgage=70),
    12: Property(name="electricite", color="grey", color_set_size=2, price=150),
    13: Property(name="neuilly", color="violet", color_set_size=3, price=140, rent=[10, 50, 150, 450, 625, 750], house=100, mortgage=70),
    14: Property(name="paradis", color="violet", color_set_size=3, price=160, rent=[12, 60, 180, 500, 700, 900], house=100, mortgage=80),
    15: Property(name="lyon", color="black", color_set_size=4, price=200, rent=[25, 50, 100, 200]),
    16: Property(name="mozard", color="orange", color_set_size=3, price=180, rent=[14, 70, 200, 550, 700, 900], house=100, mortgage=90),
    17: Property(name="communaute", color="lightcoral"),
    18: Property(name="saint-michel", color="orange", color_set_size=3, price=180, rent=[14, 70, 200, 550, 700, 950], house=100, mortgage=90),
    19: Property(name="pigalle", color="orange", color_set_size=3, price=200, rent=[16, 80, 220, 600, 800, 1000], house=100, mortgage=100),
    20: Property(name="parc-gratuit", color="lightgrey"),
    21: Property(name="matignon", color="red", color_set_size=3, price=220, rent=[18, 90, 250, 700, 875, 1050], house=150, mortgage=110),
    22: Property(name="chance", color="lightcoral"),
    23: Property(name="malesherbes", color="red", color_set_size=3, price=220, rent=[18, 90, 250, 700, 875, 1050], house=150, mortgage=110),
    24: Property(name="henri-martin", color="red", color_set_size=3, price=240, rent=[20, 100, 300, 750, 925, 1100], house=150, mortgage=120),
    25: Property(name="nord", color="black", color_set_size=4, price=200, rent=[25, 50, 100, 200]),
    26: Property(name="saint-honore", color="yellow", color_set_size=3, price=260, rent=[22, 110, 330, 800, 975, 1150], house=150, mortgage=130),
    27: Property(name="henri-martin", color="yellow", color_set_size=3, price=260, rent=[22, 110, 330, 800, 975, 1150], house=150, mortgage=130),
    28: Property(name="eau", color="grey", color_set_size=2, price=150),
    29: Property(name="henri-martin", color="yellow", color_set_size=3, price=280, rent=[24, 120, 350, 850, 1025, 1200], house=150, mortgage=140),
    30: Property(name="allez-en-prison", color="lightgrey"),
    31: Property(name="breteuil", color="green", color_set_size=3, price=300, rent=[26, 130, 390, 900, 1100, 1275], house=200, mortgage=150),
    32: Property(name="foch", color="green", color_set_size=3, price=300, rent=[26, 130, 390, 900, 1100, 1275], house=200, mortgage=150),
    33: Property(name="communaute", color="lightcoral"),
    34: Property(name="capucines", color="green", color_set_size=3, price=320, rent=[28, 150, 450, 1000, 1200, 1400], house=200, mortgage=160),
    35: Property(name="saint-lazard", color="black", color_set_size=4, price=200, rent=[25, 50, 100, 200]),
    36: Property(name="chance", color="lightcoral"),
    37: Property(name="champs-elysees", color="blue", color_set_size=2, price=350, rent=[35, 175, 500, 1100, 1300, 1500], house=200, mortgage=175),
    38: Property(name="taxe-de-luxe", color="darkgrey"),
    39: Property(name="paix", color="blue", color_set_size=2, price=400, rent=[50, 200, 600, 1400, 1700, 2000], house=200, mortgage=200),
}