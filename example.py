from pydfs_lineup_optimizer import Site, Sport, get_optimizer


optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)
optimizer.load_players_from_csv("https://www.draftkings.com/lineup/getavailableplayerscsv?contestTypeId=70&draftGroupId=30978")
lineup_generator = optimizer.optimize(10)
for lineup in lineup_generator:
    print(lineup)
