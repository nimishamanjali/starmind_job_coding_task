import pandas as pd


def levenshtein(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)
    return min(levenshtein(a[1:], b[1:]) + (a[0] != b[0]),
               levenshtein(a[1:], b) + 1,
               levenshtein(a, b[1:]) + 1

               )


def get_all_names_with_distance_one(a, b):
    if levenshtein(a, b) == 1:
        return b


def filter_null_and_duplicates(lst):
    return list(set([i for i in lst if i]))


if __name__ == '__main__':
    df = pd.read_csv("20210103_hundenamen.csv")
    names_to_check = df['HUNDENAME'].tolist()
    result = []
    for i in names_to_check:
        result.append(get_all_names_with_distance_one("Luca", i))

print(filter_null_and_duplicates(result))
