def tracklist(**tracks):
    for artist in tracks:
        print(artist)
        for album in tracks[artist]:
            print("ALBUM:", album, "TRACK:", tracks[artist][album])
