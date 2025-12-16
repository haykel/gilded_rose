from gilded_rose import Item, GildedRose

items = [
    Item("Aged Brie", 2, 0),
    Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
    Item("Conjured Mana Cake", 3, 6),
    Item("Elixir of the Mongoose", 5, 7),
    Item("Sulfuras, Hand of Ragnaros", 0, 80),
]

gilded_rose = GildedRose(items)

days = 30

for day in range(days):
    print("\n" + "-" * 30)
    print(f"Jour {day}")
    print("-" * 30)

    for item in items:
        print(item)

    input("\nAppuie sur Entrée pour passer au jour suivant...")

    gilded_rose.update_quality()
