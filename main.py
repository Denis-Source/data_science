from matplotlib import pyplot as plt


def from_csv(filename):
    rows = []
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        data = f.readlines()
        header = data.pop(0)
        for row in data:
            rows.append(row.split(","))
    return rows


print(from_csv("gdp.csv"))