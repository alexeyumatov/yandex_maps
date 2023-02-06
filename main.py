from pg_showmap import show_map


def main():
    with open('request.txt', 'r', encoding='utf-8') as file:
        output = file.readlines()
        output = tuple([el.rstrip('\n') for el in output])
        latitude, longitude, scale = output
    show_map(latitude, longitude, scale)


if __name__ == '__main__':
    main()
