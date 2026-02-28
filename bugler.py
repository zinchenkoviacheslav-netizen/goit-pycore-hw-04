from pathlib import Path

def total_salary(path):
    if not path.exists():
        return 0,0
    else:
        common_salary = 0
        mean_salary = 0
        i = 0
        with path.open("r", encoding="utf-8") as file:
            for line in file:
                parts = line.split(",")
                try:
                    common_salary += int(parts[-1].strip())
                    i += 1
                except ValueError:
                    pass
        if i > 0:
            mean_salary = int(common_salary / i)


    return common_salary, mean_salary

p_file = Path("salary.txt")
common_sal, mean_sal = total_salary(p_file)
print(f"Загальна сума заробітної плати: {common_sal}, Середня заробітна плата: {mean_sal}")