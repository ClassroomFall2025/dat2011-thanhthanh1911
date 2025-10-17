with open("Resource.txt", "r", encoding="utf-8") as file:
    dong = file.readlines()
    print(dong)
    for d in dong:
        print(d)