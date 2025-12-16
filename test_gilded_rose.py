from gilded_rose import Item, GildedRose


def test_normal_item_degrades():
    item = Item("Elixir of the Mongoose", 5, 7)
    GildedRose([item]).update_quality()
    assert item.sell_in == 4
    assert item.quality == 6


def test_quality_never_negative():
    item = Item("Elixir of the Mongoose", 0, 0)
    GildedRose([item]).update_quality()
    assert item.quality == 0


def test_aged_brie_increases():
    item = Item("Aged Brie", 2, 0)
    GildedRose([item]).update_quality()
    assert item.quality == 1


def test_backstage_passes_drop_to_zero():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    GildedRose([item]).update_quality()
    assert item.quality == 0


def test_conjured_degrades_twice_as_fast():
    item = Item("Conjured Mana Cake", 3, 6)
    GildedRose([item]).update_quality()
    assert item.quality == 4


def test_sulfuras_never_changes():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
    GildedRose([item]).update_quality()
    assert item.sell_in == 0
    assert item.quality == 80
