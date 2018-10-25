# Tuples containing elements for naming items, rooms, entities etc

Affinities = ('Chaos', 'Abyss', 'Void', 'Eldritch')
Elements = ('Water', 'Air', 'Earth', 'Fire')
Modifiers_Elemental_T1 = ('Dew', 'Whistles', 'Pebbles', 'Ashes')
Modifiers_Elemental_T2 = ('Splashes', 'Breezes', 'Rocks', 'Smoulders')
Modifiers_Elemental_T3 = ('Waves', 'Typhoons', 'Boulders', 'Flames')
Modifiers_Bonus = ('Cursed', 'Blessed')
Quality = ('Broken', 'Chipped', 'Mundane', 'Tempered', 'Pristine')
Weapons = ('Nodachi', 'Katana', 'Tekkan', 'Hachiwari')
Upgrades = ('+0', '+1', '+2', '+3', '+4', '+5')


# Saving weapon image file paths into separate variables:

handle_path = './Resources/Visual/Textures/Items/Handle.png'
blade_path = './Resources/Visual/Textures/Items/Blade.png'
bonus_path = './Resources/Visual/Textures/Items/Bonus.png'

# Defining colors for the 4 elements

Modifiers_Elemental_Colours = ((28, 58, 89),
                               (244, 213, 141),
                               (28, 89, 29),
                               (206, 78, 55))

# Usage: Select element from tuples and parse it to generator

# Order: Quality + WEAPON_NAME + 'OF' +  Modifiers_Elemental
# + Upgrade + (Modifier_Bonus)
# Example: Chipped Nodachi of Smoulders +2 (Cursed)




































