#商品名と値段の設定
items = {'りんご': 100, 'バナナ': 200, 'オレンジ': 300, 'キウイ': 400}

#自動販売機の処理
while True:
# 商品の表示
print('==================================================')
print('商品一覧')
for item_name, item_price in items.items(): # 商品名と値段を同時に取得
print(f"{item_name}: {item_price}円")
print('==================================================')
# 商品の選択
while True:
    choice = input('購入する商品を入力してください（終了する場合は q を入力）：')
    if choice == 'q':
        print('自動販売機を終了します')
        break
    elif choice not in items:
        print('その商品はありません')
    else:
        break

if choice == 'q':  # q を入力した場合はループを抜ける
    break

# 購入する数量の選択
while True:
    count = input('購入する個数を入力してください：')
    if not count.isdigit() or int(count) <= 0:
        print('個数は正の整数で入力してください')
    else:
        count = int(count)
        break

# 支払い金額の計算
total_price = items[choice] * count

# 支払い方法の選択
while True:
    payment_method = input('支払い方法を選択してください（1: 現金、2: カード）：')
    if payment_method == '1':
        # 現金支払いの場合
        while True:
            amount = input(f'投入する金額を入力してください（{total_price}円以上）：')
            if not amount.isdigit():
                print('金額は正の整数で入力してください')
            elif int(amount) < total_price:
                print(f'投入する金額は{total_price}円以上にしてください')
            else:
                amount = int(amount)
                change = amount - total_price
                break
        break
    elif payment_method == '2':
        # カード支払いの場合
        print(f'カードで{total_price}円支払います')
        change = 0
        break
    else:
        print('1か2で入力してください')

# 購入した商品と数量、支払い金額とお釣りを表示する
print('--------------------------------------------------')
print(f'{choice}を{count}個購入しました')
print(f'支払い金額は{total_price}円です')
if change > 0:
    print(f'お釣りは{change}円です')
print('ありがとうございました！') 



#このコードでは、以下のような処理が実現されています。

#商品名と価格を設定する変数 items を定義する。
#while ループを用いて、自動販売機の処理を繰り返す。
#商品の一覧を表示し、購入する商品をユーザーに選択してもらう。
#q を入力することで自動販売機を終了する。
#購入する数量をユーザーに選択してもらう。
#購入する数量が正しい形式で入力されるまで、エラーメッセージを表示しつつ再度入力を促す。
#支払い金額を計算する。
#購入した商品と数量、支払い金額を表示する。
