from pathlib import Path

def get_cats_info(path):
    if not path.exists():
        return []   # порожній список, якщо файлу немає

    cat_list = []
    keys = ["id", "name", "age"]
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            values = line.strip().split(",")
            part_dict = dict(zip(keys, values))
            cat_list.append(part_dict)

    return cat_list
cats_list = []
p_file = Path("cat.txt")
print(get_cats_info(p_file))