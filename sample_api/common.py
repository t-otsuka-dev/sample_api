# --*-- coding: utf-8  --*--



def sort(dic, sort):

    if "Default" in sort or "Price" in sort:
        #sort = Price(Default)
        ##価格昇順
        items = sorted(dic.items(), key=lambda x: int(x[1]['Price']))
    elif "Point" in sort:
        #sort = Point
        ##ポイント降順
        items = sorted(dic.items(), key=lambda x: int(x[1]['Point']), reverse=True)
    elif "PricePoint" in sort:
        #sort = PricePoint
        ##価格降順＋ポイント降順
        items = sorted(dic.items(), key=lambda x: int(x[1]['PricePoint']), reverse=True)
    else:
        # sort = 設定値外
        ##価格昇順
        items = sorted(dic.items(), key=lambda x: int(x[1]['Price']))

    return items