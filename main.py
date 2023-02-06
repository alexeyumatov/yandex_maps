from pg_showmap import show_map


def main():
    latitude, longitude = input(), input()
    spn = input()
    show_map(latitude, longitude, spn)


if __name__ == '__main__':
    main()
