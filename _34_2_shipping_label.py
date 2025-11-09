def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('apt')}, {kwargs.get('street')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}, {kwargs.get('street')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('zip')}")
    print(f"{kwargs.get('region')}")
    print()


shipping_label(
    "Mr.",
    "Kyryll",
    "Chudomirovich",
    "Flins",
    street="Final Night Cemetery",
    city="Paha isle",
    region="Nod Krai",
    zip="12345",
    apt="Grave 1",
    pobox="PO Box 404",
)
