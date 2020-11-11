import re

if __name__ == '__main__':
    target = "Hello 1234567 World_This is a Regex Demo"
    target1 = "Hello 123 4567 World_This is a Regex Demo"

    print(len(target))
    # result = re.match('^Hello\s(\d+)\sWorld', target)
    result1 = re.match('^Hello.*Demo$', target)

    print(result1)
    print(result1.group())
    print(result1.span())
