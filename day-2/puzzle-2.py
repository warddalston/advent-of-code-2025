demo = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
puzzle_input = "92916254-92945956,5454498003-5454580069,28-45,4615-7998,4747396917-4747534264,272993-389376,36290651-36423050,177-310,3246326-3418616,48-93,894714-949755,952007-1003147,3-16,632-1029,420-581,585519115-585673174,1041-1698,27443-39304,71589003-71823870,97-142,2790995-2837912,579556301-579617006,653443-674678,1515120817-1515176202,13504-20701,1896-3566,8359-13220,51924-98061,505196-638209,67070129-67263432,694648-751703,8892865662-8892912125"
parsed_ranges = [id_range.split("-") for id_range in puzzle_input.split(",")]


def validate_id(id: str, splits: int) -> bool:
    if len(id) % splits:
        return False

    split_length = len(id) // splits
    target = id[:split_length]
    comparison_index = split_length

    while comparison_index < len(id):
        if id[comparison_index: (comparison_index + split_length)] != target:
            return False
        comparison_index += split_length
    return True

def validate_range(start_id: str, stop_id: str) -> int:
    out = 0
    for id in range(int(start_id), int(stop_id) + 1):
        string_id, split = str(id), 2
        while len(string_id) >= split:
            if validate_id(string_id, split):
                out += id
                break
            split += 1
    return out

sum([validate_range(x[0], x[1]) for x in parsed_ranges])
