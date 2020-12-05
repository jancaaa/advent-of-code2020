import re


def read_file() -> list:
    with open("input.txt") as fp:
        passports = []
        for passport in fp.read()[:-1].split("\n\n"):
            record = {}
            passport = passport.replace("\n", " ")
            parts = passport.split(" ")
            for p in parts:
                p = p.split(":")
                record[p[0]] = p[1]
            passports.append(record)
    return passports


def tests():
    assert valid_byr("1919") == False
    assert valid_byr("1920")
    assert valid_byr("1921")
    assert valid_byr("2001")
    assert valid_byr("2002")
    assert valid_byr("2003") == False
    assert valid_iyr("abc") == False

    assert valid_hgt("149cm") == False
    assert valid_hgt("150cm")
    assert valid_hgt("151cm")
    assert valid_hgt("192cm")
    assert valid_hgt("193cm")
    assert valid_hgt("194cm") == False

    assert valid_hgt("58in") == False
    assert valid_hgt("59in")
    assert valid_hgt("60in")
    assert valid_hgt("75in")
    assert valid_hgt("76in")
    assert valid_hgt("77in") == False

    assert valid_hgt("77aa") == False
    assert valid_hgt("aaaa") == False
    assert valid_hgt("77") == False

    assert valid_hcl("#123abc")
    assert valid_hcl("#123abC") == False
    assert valid_hcl("#123abz") == False
    assert valid_hcl("123abc") == False

    assert valid_pid("000000001")
    assert valid_pid("123456789")
    assert valid_pid("0123456789") == False
    assert valid_pid("abc9") == False


def valid_byr(year) -> bool:
    try:
        year = int(year)
    except ValueError:
        return False
    return 1920 <= year <= 2002


def valid_iyr(year) -> bool:
    try:
        year = int(year)
    except ValueError:
        return False
    return 2010 <= year <= 2020


def valid_eyr(year) -> bool:
    try:
        year = int(year)
    except ValueError:
        return False
    return 2020 <= year <= 2030


def valid_hgt(height) -> bool:
    if height[-2:] == "in":
        try:
            height = int(height[:-2])
        except ValueError:
            return False
        return 59 <= height <= 76
    elif height[-2:] == "cm":
        try:
            height = int(height[:-2])
        except ValueError:
            return False
        return 150 <= height <= 193
    else:
        return False


def valid_hcl(color) -> bool:
    regex = r"^#[a-f0-9]{6}$"
    return bool(re.search(regex, color))


def valid_ecl(value) -> bool:
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_pid(pid) -> bool:
    if not len(pid) == 9:
        return False
    try:
        pid = int(pid)
    except ValueError:
        return False
    return True


def part1(passports: list):
    valid_count = 0
    for x in passports:
        required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        if all(elem in x.keys() for elem in required_fields):
            valid_count += 1
    return valid_count


def part2(passports: list):
    valid_count = 0
    for x in passports:
        required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        if (all(elem in x.keys() for elem in required_fields)
                and valid_byr(x["byr"])
                and valid_iyr(x["iyr"])
                and valid_eyr(x["eyr"])
                and valid_hgt(x["hgt"])
                and valid_hcl(x["hcl"])
                and valid_ecl(x["ecl"])
                and valid_pid(x["pid"])
        ):
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    passports = read_file()
    tests()
    print(f"Part 1: {part1(passports)}")
    print(f"Part 2: {part2(passports)}")
