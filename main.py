from samples.mapapi_PG import show_map


def main():
    latitude, lontitude = input(), input()
    spn = input()
    show_map(f"ll={latitude},{lontitude}&spn={spn}", "map")


if __name__ == '__main__':
    main()
