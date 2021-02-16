from house_downloader import HouseDownloader


def main():
    results = HouseDownloader.build().download_houses()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
