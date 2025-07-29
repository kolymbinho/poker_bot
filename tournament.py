class Tournament:
    def __init__(self):
        self.buy_in = 0
        self.rebuy = 0
        self.addon = 0
        self.players = {}

    def set_prices(self, buy_in, rebuy, addon):
        self.buy_in = buy_in
        self.rebuy = rebuy
        self.addon = addon

    def add_player(self, name):
        self.players[name] = {"rebuy": 0, "addon": 0}

    def add_rebuy(self, name):
        self.players[name]["rebuy"] += 1

    def add_addon(self, name):
        self.players[name]["addon"] += 1

    def get_results(self):
        total_buyin = len(self.players) * self.buy_in
        total_rebuy = sum(p["rebuy"] for p in self.players.values()) * self.rebuy
        total_addon = sum(p["addon"] for p in self.players.values()) * self.addon
        total_prize = total_buyin + total_rebuy + total_addon

        msg = f"💰 Общий призовой фонд: {total_prize}\n\n👥 Участники:\n"
        for name, data in self.players.items():
            rb = data["rebuy"]
            ad = data["addon"]
            msg += f"– {name}: ребаев {rb}, аддонов {ad}\n"

        # Авто-распределение по 50/30/20
        first = int(total_prize * 0.5)
        second = int(total_prize * 0.3)
        third = total_prize - first - second
        msg += f"\n🏆 Призы:\n🥇 {first}\n🥈 {second}\n🥉 {third}"

        return msg
