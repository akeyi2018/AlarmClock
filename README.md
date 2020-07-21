### AlarmClock
<h5>目覚まし時計

<h5>指定した時間でセットできる。  
アラーム文字列をDisplayに表示するのみ  

Mp3/Mp4再生の設定は[ここ](https://akeyi2020.blogspot.com/2020/07/raspberry-pi.html)参照
AlarmPlayer.pyダウンロードし、以下のコマンドを入力、playlist.txtの曲がシャッフルに再生が可能

```YAML
python AlarmPlayer.py playlist.txt
```

* * * 
<h5>今後実装予定の機能


* * * 

Latest Update:2020/03/19


下記機能のクラス名とメソッド名のみ実装
| No | Class Name | 機能 | 使用ライブラリ | 備考 |  
|---:|:---|:---|:---|:---|
| 1 | AlarmTimer.py | アラーム生成、トリガー | datetime, time | 動作OK |
| 2 | AlarmPlayer.py | アラームを鳴らす | mplayer | ローカル再生可能 |
| 3 | SleepChecker.py | 睡眠チェック |  |  |
| 4 | SleepRecoder.py | 睡眠記録 |  |  |
| 5 | SleepSchedule.py | 睡眠スケジュール | jpholiday | 動作OK |
| 6 | Sleeperson.py | 使用者の情報 |  |  |


* 音楽をならす
* ストップボタン
* 自動セット機能


<h5>参考文献<br>



* Lチカ

https://www.raspberrypirulo.net/entry/gpio


* Callback

https://www.raspberrypirulo.net/entry/python-callback


* Wait for edge


https://www.raspberrypirulo.net/entry/python-waitforedge


※Raspberry PiのGPIOは、ノイズが大きいため使い方によっては稀に予期せぬ動作をしますので、ご注意ください。
