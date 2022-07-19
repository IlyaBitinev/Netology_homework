import requests


def top_intelligence(url, *name_hero):
    response = requests.get(url)
    iq = 0
    name = " "
    for item in response.json():
        if item["name"] in name_hero and item["powerstats"]["intelligence"] > iq:
            iq = item["powerstats"]["intelligence"]
            name = item["name"]
    return name


if __name__ == "__main__":
    print(top_intelligence("https://akabab.github.io/superhero-api/api/all.json", "Hulk", "Thanos", "Capitan America"))
