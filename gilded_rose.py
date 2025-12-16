class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


class GildedRose:
    def __init__(self, items):
        self.items = items   

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            item.sell_in -= 1

            if item.name == "Aged Brie":
                item.quality += 1
                if item.sell_in < 0:
                    item.quality += 1

            elif item.name.startswith("Backstage passes"):
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in < 5:
                    item.quality += 3
                elif item.sell_in < 10:
                    item.quality += 2
                else:
                    item.quality += 1

            else:
                degradation = 2 if item.name.startswith("Conjured") else 1
                if item.sell_in < 0:
                    degradation *= 2
                item.quality -= degradation

            if item.quality < 0:
                item.quality = 0
            if item.quality > 50:
                item.quality = 50
