from collections import deque

# 👉 Lista ejemplo (deberías tener mas de 200 personajes)
personajes = [
    {
        "name": "Kang",
        "alias": "Kang the Conqueror",
        "real_name": "Nathaniel Richards",
        "short_bio": "Kang the Conqueror is a time-traveling warlord who has battled many heroes, especially the Avengers. He is known for his mastery of advanced technology and his ability to manipulate time.",
        "first_appearance": 1964,
        "is_villain": True
    },
    {
        "name": "Hulk",
        "alias": "The Hulk",
        "real_name": "Bruce Banner",
        "short_bio": "Hulk is a gamma-powered superhero with incredible strength and durability. He transforms into a green giant when angered or stressed.",
        "first_appearance": 1962,
        "is_villain": False
    },
    {
        "name": "Black Widow",
        "alias": "Natasha Romanoff",
        "real_name": "Natasha Romanoff",
        "short_bio": "Black Widow is a highly trained spy and former assassin with exceptional skills in hand-to-hand combat and espionage.",
        "first_appearance": 1964,
        "is_villain": False
    },
    {
        "name": "Black Cat",
        "alias": "Felicia Hardy",
        "real_name": "Felicia Hardy",
        "short_bio": "Black Cat is a skilled burglar with a unique power that brings bad luck to her enemies. She often operates in the gray area between hero and villain.",
        "first_appearance": 1979,
        "is_villain": True
    },
    {
        "name": "Iron Man",
        "alias": "Iron Man",
        "real_name": "Tony Stark",
        "short_bio": "A billionaire inventor who built a powered suit of armor to save his life and became a founding Avenger.",
        "first_appearance": 1963,
        "is_villain": False
    },
    {
        "name": "Magneto",
        "alias": "Master of Magnetism",
        "real_name": "Max Eisenhardt",
        "short_bio": "A powerful mutant with control over magnetic fields, often portrayed as an adversary to the X-Men, though with complex motivations.",
        "first_appearance": 1963,
        "is_villain": True
    },
    {
        "name": "Storm",
        "alias": "Storm",
        "real_name": "Ororo Munroe",
        "short_bio": "A mutant with the ability to manipulate weather, known for her leadership in the X-Men and her strong moral compass.",
        "first_appearance": 1975,
        "is_villain": False
    },
    {
        "name": "Venom",
        "alias": "Venom",
        "real_name": "Eddie Brock",
        "short_bio": "A journalist who bonds with an alien symbiote to become the anti-hero Venom, often torn between vengeance and justice.",
        "first_appearance": 1988,
        "is_villain": True
    },
    {
        "name": "Scarlet Witch",
        "alias": "Scarlet Witch",
        "real_name": "Wanda Maximoff",
        "short_bio": "A mutant with chaos magic and reality-warping powers, known for her complex role as both hero and threat.",
        "first_appearance": 1964,
        "is_villain": False
    },
    {
        "name": "Abomination",
        "alias": "Abomination",
        "real_name": "Emil Blonsky",
        "short_bio": "A former KGB agent who transforms into a gamma-powered monster and becomes one of Hulk's main enemies.",
        "first_appearance": 1967,
        "is_villain": True
    },
    {
        "name": "Adam Warlock",
        "alias": "Adam Warlock",
        "real_name": "Adam Warlock",
        "short_bio": "An artificially created perfect human who becomes a cosmic protector and wielder of the Soul Gem.",
        "first_appearance": 1967,
        "is_villain": False
    },
    {
        "name": "Angel",
        "alias": "Angel",
        "real_name": "Warren Worthington III",
        "short_bio": "A founding member of the X-Men with large feathered wings that allow him to fly.",
        "first_appearance": 1963,
        "is_villain": False
    },
    {
        "name": "Annihilus",
        "alias": "Annihilus",
        "real_name": "Annihilus",
        "short_bio": "A powerful insectoid ruler from the Negative Zone, obsessed with extending his lifespan.",
        "first_appearance": 1968,
        "is_villain": True
    },
    {
        "name": "Ant Man",
        "alias": "Ant Man",
        "real_name": "Hank Pym",
        "short_bio": "A brilliant scientist who discovered Pym Particles and became a size-changing superhero.",
        "first_appearance": 1962,
        "is_villain": False
    },
    {
    "name": "Apocalypse",
    "alias": "Apocalypse",
    "real_name": "En Sabah Nur",
    "short_bio": "One of the first mutants, Apocalypse believes in survival of the fittest and has enhanced his body over millennia with alien technology.",
    "first_appearance": 1986,
    "is_villain": True
    },
    {
        "name": "Baron Zemo",
        "alias": "Baron Zemo",
        "real_name": "Helmut Zemo",
        "short_bio": "A brilliant and ruthless strategist, Baron Zemo is a longtime foe of Captain America and leader of various villainous groups.",
        "first_appearance": 1973,
        "is_villain": True
    },
    {
        "name": "Beast",
        "alias": "Beast",
        "real_name": "Henry 'Hank' McCoy",
        "short_bio": "A founding member of the X-Men, Beast possesses superhuman strength and agility along with a brilliant scientific mind.",
        "first_appearance": 1963,
        "is_villain": False
    },
    {
        "name": "Beta Ray Bill",
        "alias": "Beta Ray Bill",
        "real_name": "Beta Ray Bill",
        "short_bio": "A noble alien warrior deemed worthy of wielding Mjolnir, he was granted his own hammer, Stormbreaker, by Odin.",
        "first_appearance": 1983,
        "is_villain": False
    },
    {
        "name": "Black Bolt",
        "alias": "Black Bolt",
        "real_name": "Blackagar Boltagon",
        "short_bio": "King of the Inhumans, Black Bolt possesses a voice so powerful that even a whisper can cause massive destruction.",
        "first_appearance": 1965,
        "is_villain": False
    },
    {
        "name": "Black Panther",
        "alias": "Black Panther",
        "real_name": "T'Challa",
        "short_bio": "King of Wakanda and protector of its people, Black Panther is a skilled fighter, strategist, and bearer of the Heart-Shaped Herb.",
        "first_appearance": 1966,
        "is_villain": False
    },
    {
        "name": "Blizzard",
        "alias": "Blizzard",
        "real_name": "Donnie Gill",
        "short_bio": "A villain who uses a suit capable of generating intense cold and ice-based attacks, often clashing with Iron Man.",
        "first_appearance": 1987,
        "is_villain": True
    },
    {
        "name": "Bullseye",
        "alias": "Bullseye",
        "real_name": "Lester",
        "short_bio": "An assassin with deadly accuracy, Bullseye never misses and is a persistent nemesis of Daredevil.",
        "first_appearance": 1976,
        "is_villain": True
    },
    {
        "name": "Cable",
        "alias": "Cable",
        "real_name": "Nathan Summers",
        "short_bio": "A time-traveling mutant soldier with telekinetic powers and a techno-organic virus, he is the son of Cyclops and Madelyne Pryor.",
        "first_appearance": 1990,
        "is_villain": False
    },
    {
    "name": "Captain America",
    "alias": "Captain America",
    "real_name": "Steve Rogers",
    "short_bio": "A super-soldier from World War II, Captain America is a symbol of heroism, justice, and patriotism in the Marvel Universe.",
    "first_appearance": 1941,
    "is_villain": False
    },
    {
        "name": "Captain Britain",
        "alias": "Captain Britain",
        "real_name": "Brian Braddock",
        "short_bio": "Chosen by Merlyn and Roma to protect the multiverse, Captain Britain draws his powers from a mystical amulet and his own will.",
        "first_appearance": 1976,
        "is_villain": False
    },
    {
        "name": "Charlie-27",
        "alias": "Charlie-27",
        "real_name": "Charlie-27",
        "short_bio": "A genetically engineered soldier from Jupiter and member of the original Guardians of the Galaxy team from the 31st century.",
        "first_appearance": 1969,
        "is_villain": False
    },
    {
        "name": "Cloak",
        "alias": "Cloak",
        "real_name": "Tyrone Johnson",
        "short_bio": "Cloak can manipulate darkforce energy and teleport through the Dark Dimension. He is one half of the duo Cloak and Dagger.",
        "first_appearance": 1982,
        "is_villain": False
    },
    {
        "name": "Colossus",
        "alias": "Colossus",
        "real_name": "Piotr Rasputin",
        "short_bio": "A Russian mutant who can transform his body into organic steel, Colossus is a powerful member of the X-Men.",
        "first_appearance": 1975,
        "is_villain": False
    },
    {
        "name": "Cyclops",
        "alias": "Cyclops",
        "real_name": "Scott Summers",
        "short_bio": "A founding member and leader of the X-Men, Cyclops emits powerful optic blasts and is known for his strategic mind.",
        "first_appearance": 1963,
        "is_villain": False
    },
    {
        "name": "Cyclops-X-Men97",
        "alias": "Cyclops-X-Men97",
        "real_name": "Scott Summers",
        "short_bio": "An alternate version of Cyclops as seen in the animated series X-Men '97, continuing to lead the X-Men after Xavier’s absence.",
        "first_appearance": 2023,
        "is_villain": False
    },
    {
        "name": "Dagger",
        "alias": "Dagger",
        "real_name": "Tandy Bowen",
        "short_bio": "Dagger generates light daggers that heal and purify. She forms a powerful partnership with Cloak.",
        "first_appearance": 1982,
        "is_villain": False
    }],
    
# 1️) Ordenado por nombre ascendente

ordenado_por_name = sorted(personajes, key=lambda x: x["name"])
print("\n✅ Ordenados por name:")
for p in ordenado_por_name:
    print(p["name"])

# 2️) Posición de "Rocket Raccoon"
names = [p["name"] for p in personajes]
if "Rocket Raccoon" in names:
    pos = names.index("Rocket Raccoon")
    print(f"\n✅ Rocket Raccoon está en la posición {pos}")
else:
    print("\n❌ Rocket Raccoon no está en la lista")

# 3) Listar villanos
is_villian = [p for p in personajes if p["es_villano"]]
print("\n✅ Villanos:")
for v in villanos:
    print(v["name"])

# 4️) Villanos en una cola, mostrar los anteriores a 1980
cola_villanos = deque(is_villian)
villanos_antes_1980 = [v for v in cola_villanos if v["first_appearance"] < 1980]
print("\n✅ Villanos antes de 1980:")
for v in villanos_antes_1980:
    print(v["name"], "-", v["first_appearance"])

# 5️) Superhéroes que empiezan con BI, G, MY, W 
prefijos = ("BI", "G", "MY", "W")
superheroes_filtrados = [
    p for p in personajes
    if not p["es_villano"] and p["name"].upper().startswith(prefijos)
]
print("\n✅ Superhéroes que comienzan con BI, G, MY o W:")
for s in superheroes_filtrados:
    print(s["name"])

# 6️) Ordenados por nombre real
ordenado_nombre_real = sorted(personajes, key=lambda x: x["real_name"])
print("\n✅ Ordenados por nombre real:")
for p in ordenado_nombre_real:
    print(p["name"], "-", p["real_name"])

# 7️) Ordenados por fecha de aparición
ordenado_fecha = sorted(personajes, key=lambda x: x["first_appearance"])
print("\n✅ Superhéroes ordenados por aparición:")
for p in ordenado_fecha:
    print(p["name"], "-", p["first_appearance"])

# 8️) Modificar nombre real de Ant Man
for p in personajes:
    if p["name"] == "Ant Man":
        p["real_name"] = "Scott Lang"
        print("\n✅ Nombre real de Ant Man modificado a Scott Lang.")

# 9️) Biografía contiene 'Time-Traveling' o 'Suit'
palabras_clave = ["time-traveling", "suit"]
coincidentes = [
    p for p in personajes
    if any(palabra in p["short_bio"].lower() for palabra in palabras_clave)
]
print("\n✅ Personajes con 'Time-Traveling' o 'Suit' en la short_bio:")
for p in coincidentes:
    print(p["name"], "-", p["short_bio"])

# ) Eliminar Electro y Barón Zemo
nombres_a_eliminar = ["Electro", "Barón Zemo"]
eliminados = []

for name in nombres_a_eliminar:
    for i, p in enumerate(personajes):
        if p["name"] == name:
            eliminados.append(personajes.pop(i))
            break

print("\n✅ Personajes eliminados:")
for p in eliminados:
    print(p)
