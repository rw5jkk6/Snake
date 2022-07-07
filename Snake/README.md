## 初めに
- 完成をコピーして動きを確認する


## Githubでsnakeゲームを作る(左の数字はファイル番号で対応してる)

1. ゲームができる画面表示と終了をつける
    - 全てのゲームの共通になるので、ユーザスニペットを使う。上を参照
    - コメントをつけてcommitする
2. 画面に縦線と横線をつける
    - コードを書く
    - コメントをつけてcommitする
    - 前のcommitとコードを比較する。git graphを押して、○masterの右クリックしてmain.pyを押す
3. snakeが動く
    - ここから複雑になるのでbranchで作業する
    - コードを書く
    - さっきと同じで、前のcommitとコードを比較する
    - コメントをつけてcommitする
    - masterとmergeする。まずvscodeの左下をクリックしてmasterにcheck　outする。branchのところで右クリックしてmergeを押す
4. 自分自身と壁に当たるとゲームーオーバーにする
    - branchでコードを書く
    - コメントをつけてcommitする
    - masterとmergeする。
    - 自分自身に当たってもゲームオーバーしないのでmasterをrevert(○masterの右で右クリックしてrevertを選ぶ)して、先ほどのbranchにcheckoutして修正してmergeする
5. ゲームオーバーしてるか分からないので\[ゲームオーバー]の文字を表示させる
    - branchでコードを書く
    - コメントをつけてcommitする
    - masterとmergeする。
6. エサをゲーム開始時に置くが、エサを取ることはできない
    - branchでコードを書く
    - コメントをつけてcommitする
    - masterとmergeする。
7. エサを食べると大きくなって、ランダムに餌が出現する
    - branchでコードを書く
    - コメントをつけてcommitする
    - masterとmergeする。

## 応用
- snakeの色を赤と青にしてコンフリクトさせてみる
- forkしてcloneする
- エサの数を30にするプルリクエストを送る
