def find_common_participants(group_one, group_two, delimiter=","):
    first_group = group_one.split(delimiter)
    second_group = group_two.split(delimiter)
    common_participants = sorted(set(first_group) & set(second_group))
    return common_participants

participants_first_group_1 = "Иванов|Петров|Сидоров"
participants_second_group_1 = "Петров|Сидоров|Смирнов"

common_participants_1 = find_common_participants(
    participants_first_group_1,
    participants_second_group_1,
    delimiter="|"
)
print(f"Общие участники: {common_participants_1}")

participants_first_group_2 = "Иванов,Петров,Сидоров"
participants_second_group_2 = "Петров,Сидоров,Смирнов"

common_participants_2 = find_common_participants(
    participants_first_group_2,
    participants_second_group_2
)
print(f"Общие участники: {common_participants_2}")

