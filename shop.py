# 商品名と値段の設定
items = {'りんご': 100, 'バナナ': 200, 'オレンジ': 300,'キウイ':400}

# 自動販売機の処理
while True:
    # 商品の表示
    print('==================================================')
    print('商品一覧')
    for item_name in items:
        print(item_name + ': ' + str(items[item_name]) + '円')
    print('==================================================')

    # 商品の選択
    while True:
        choice = input('購入する商品を入力してください（終了する場合は q を入力）：')
        if choice in items or choice == 'q':
            break
        print('その商品はありません')

    # 終了処理
    if choice == 'q':
        print('自動販売機を終了します')
        break

    # 購入する数量の選択
    while True:
        count = input('購入する個数を入力してください：')
        if count.isdigit() and int(count) > 0:
            count = int(count)
            break
        print('個数は正の整数で入力してください')

    # 支払い金額の計算
    total_price = items[choice] * count

    # 支払い方法の選択
    while True:
        payment_method = input('支払い方法を選択してください（1: 現金、2: カード）：')
        if payment_method == '1':
            # 現金支払いの場合
            while True:
                amount = input('投入する金額を入力してください：')
                if amount.isdigit() and int(amount) >= total_price:
                    amount = int(amount)
                    break
                print('金額は正の整数で、購入金額以上の金額を入力してください')
            change = amount - total_price
            break
        elif payment_method == '2':
            # カード支払いの場合
            print('カードで ' + str(total_price) + '円 支払います')
            change = 0
            break
        else:
            print('1か2で入力してください')

    # 購入した商品と数量、支払い金額とお釣りを表示する
    print('--------------------------------------------------')
    print(choice + 'を ' + str(count) + '個 購入しました')
    print('支払い金額は ' + str(total_price) + '円 です')
    if change > 0:
        print('お釣りは ' + str(change) + '円 です')
    print('ありがとうございました！')


#このコードでは、以下のような処理が実現されています。

#商品名と価格を設定する辞書 items を定義する。
#while ループを用いて、自動販売機の処理を繰り返す。
#商品の一覧を表示し、購入する商品をユーザーに選択してもらう。
#q を入力することで自動販売機を終了する。
#購入する数量をユーザーに選択してもらう。
#購入する数量が正しい形式で入力されるまで、エラーメッセージを表示しつつ再度入力を促す。
#支払い金額を計算する。
#購入した商品と数量、支払い金額を表示する。