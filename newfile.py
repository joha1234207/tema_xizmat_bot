import json

B

def add_themes(file_path, platform, category, new_links):
    # JSON faylni o‘qish
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Agar kategoriya yoki platform bo‘lmasa yaratib qo‘yadi
    if platform not in data:
        data[platform] = {}

    if category not in data[platform]:
        data[platform][category] = []

    # Yangi linklarni qo‘shish
    data[platform][category].extend(new_links)

    # Faylga qayta yozish
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✅ Linklar qo‘shildi!")
  

add_themes(
	"data.json",
	"ios",
	"BOSHQA❤",
	links
)