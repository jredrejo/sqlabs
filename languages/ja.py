# coding: utf8
{
"\n%s arranges its radio buttons vertically, which occupies a relatively large area. \nHere we implemented a horizontal radio widget, and further made it clickable for it's labels. \n": '%sはラジオボタンを垂直に配置するため、少し広めの領域を占めてしまいます。そこで水平のラジオウィジェットを実装し、さらにラベルをクリック可能にしました。',
'\n%s is made by a single select tag,\nwhich would be difficult to handle when it had many options.\nWe built more user-friendly multiple select widget with two select tags.\nYou can choice between horizontal or vertical layout.\n': '%s は単一のセレクトタグからなり、多数のオプションを持つ場合に扱うのが困難になります。そこで、より使い勝手のよい、２つのセレクトタグからなる複数選択ウィジェットを作成しました。水平まはた垂直のレイアウトを選ぶことができます。\r\n',
'\nA WYSIWYG editor widget using %s. You can specify your language by a contructor argument, and include your image chooser.\n': '%sを使用したWYSIWYGエディターウィジェットです。コンストラクタの引数で使用言語を指定することができ、さらに独自の画像選択機能を組み込むことができます。\r\n',
'\nA custom %s for denser layout using multi-line columns. \nYou can specify structured fields corresponding to the layout.\nOther functionarities are same as SQLFORM, including facotry and readonly forms.\n': 'より密なレイアウトのための複合カラムを用いたカスタム%sです。レイアウトに対応する構造化したフィールドを指定することができます。他の機能はSQLFORMと同じで、factoryやreadonlyフォームも利用可能です。',
'\nA custom %s for denser layout using multi-line rows. \nYou can specify structured fields corresponding to the layout.\nThe interface of the class keeps backward-compatible to the SQLTABLE,\nand enables more flexible customization.\n': 'より密なレイアウトのための複合行を用いたカスタム%sです。レイアウトに対応する構造化したフィールドを指定することができます。クラスのインタフェースはSQLTABLEと後方互換を保ちつつ、より柔軟なカスタマイズが可能です。\r\n',
'\nA file upload widget using %s.\nThe uploadify turns a file input tag into a flash-based file uploader,\nwhich displays a progress bar and enables ajax upload. \n': '%sを用いたファイルアップロードウィジェットです。uploadifyはファイルのインプタグをflashベースのファイルアップローダーに変換します。これにより、プログレスバーが表示され、ajaxアップロードが可能になります。\r\n',
'\nA standard paginator which can be used with SQLTABLE. The basic design is inspired by %s.\n': 'SQLTABLEとともに用いることができる標準的なページネーターです。基本的な設計は%sを参考にしています。\r\n',
'\nAn input widget whose size is automatically adjusted to maximum length of its field value\n defined by validators such as IS_LENGTH and IS_INT_IN_RANGE.\nThe widget works with string, integer, double, and, decimal fields.\n': '自動的にサイズが調整される入力ウィジェットです。IS_LENGTH や IS_INT_IN_RANGE のようなバリデータによって決まるフィールドの値の最大長に応じて変化します。string、integer、double、decimal フィールドに対応しています。',
'\nThe lazy options widget receives js events and sends ajax requests to populate its select options as in %s.\n': '遅延オプションウィジェットはjsのイベントを受け取ってajaxリクエストを送り、%sのように選択オプションを追加します。\r\n',
'\nThe plugin provides a form object which is an extra table column composed of checkboxes to select multiple records,\nand submits selected record ids.\n': 'このプラグインは複数のレコードを選択するためのチェックボックスからなる追加のテーブルカラムとしてフォームオブジェクトを提供します。このフォームはレコードのIDを送信します。\r\n',
'\nThe suggest widget is an alternative for %s.\nIt uses %s with some modifications to handle non-us charcters. \nFurther, it visualize a selecting status at each typing step.\n': 'サジェストウィジェットは%sの代替です。修正した%sを用いて非US文字を扱うことができます。さらに、各タイピングのステップにおける選択状態を可視化します。',
'\nThis plugin a form object which makes table rows permutable using %s, and submits permuted row indices.\n': 'このプラグインは%sを用いてテーブルの行を入れ替え可能にするフォームオブジェクトを提供します。このフォームは入れ替えた行のインデックスを送信します。\r\n',
'\nThis plugin automatically attaches not-empty markers to labels of "not-empty" fields of a form, \nbased on field validators.\n': 'このプラグインは、フィールドのバリデータに基づいて、自動的に必須マークを"必須"フィールドのラベルに付与します。\r\n',
'\nThis plugin provides a color picker widget, using %s. Picked color is displayed in forms. \n': 'このプラグインは、%sを用いて色選択ウィジェットを提供します。選択した色はフォームに表示されます。\r\n',
'\nThis plugin provides buttons to select table records by a value of a field,\nshowing the record count for each value of the field.\n': 'このプラグインは、フィールドの値によってテーブルレコードを選択するボタンを提供します。さらに、フィールドの各値に対してレコードの総数を表示します。',
'\nThis plugin provides time, date and datetime picker widgets using %s.\n': 'このプラグインは%sを使用して、時刻、日付、日時の選択ウィジェットを提供します。',
'%Y-%m-%d': '%Y-%m-%d',
'%Y-%m-%d %H:%M:%S': '%Y-%m-%d %H:%M:%S',
'%s mutual friends': '共通の友達%s人',
'A WYSIWYG editor widget using elRTE.js': 'elRTE.jsを用いたA WYSIWYGエディターウィジェット',
'A built-in multiple options widget': '組み込みの複数オプションウィジェット',
'A built-in radio widget': '組み込みのラジオウィジェット',
'A collection of plugins of %s, an opensource Python web framework.\nHere we love to share useful code parts produced by our development with the framework.\nThe code parts are organized in %s, and easily available.': 'オープンソースのPythonウェブ・フレームワーク %s のプラグイン集です。ここでは、このフレームワークによる開発で生み出された有用なコード部品を共有したいと思います。コード部品は %s に基づいて整理されいて、簡単に利用可能です。',
'A color picker widget using colorpicker.js': 'colorpicker.jsを用いた色選択ウィジェット',
'A custom SQLFORM for denser layout': 'より密なレイアウトのためのカスタムSQLFORM',
'A custom SQLTABLE for denser layout': 'より密なレイアウトのためのカスタムSQLTABLE',
'A date-time picker widget using anytime.js': 'anytime.jsを用いた日時選択ウィジェット',
'A direct messaging manager': 'ダイレクト・メッセージ用の管理プログラム',
'A file upload widget using uploadify.js': 'uploadify.jsを用いたファイルアップロードウィジェット ',
'A friendship manager': 'フレンドシップ用の管理プログラム',
'A lazy loading options widget triggered by a js event': 'jsのイベントで起動する遅延ロードオプションウィジェット',
'A manager for direct messaging between users as in Facebook.': 'Facebookにあるようなユーザー間のダイレクト・メッセージングのための管理プログラムです。',
'A manager to make ajax-intensive comment boxes for a sort of news feed as in Facebook.': 'Facebookにあるようなニュースフィードに対するAjaxを駆使したコメントボックスを作成するための管理プログラムです。',
'A manager to make friendship relations among users as in Facebook.': 'Facebookにあるようなユーザー間のフレンドシップ関係を構築するための管理プログラムです。',
'A radio widget arranging its buttons horizontally': '水平にボタン配置したラジオウィジェット',
'A refined autocomplete widget': '洗練された自動コンプリートウィジェット',
'A scope selector for table records': 'テーブルレコードに対するスコープのセレクター',
'A size-adjusted input widget': 'サイズ調整した入力ウィジェット',
'A standard paginator': '標準的なページネーター',
'A table column composed of checkboxes': 'チェックボックスからなるテーブルカラム',
'A user-friendly multiple options widget': '使い勝手のよい複数オプションウィジェット',
'Add friend': '友だちになる',
'Add not-empty markers to field labels': 'フィールドラベルに必須マークを付与します',
'All': 'すべて',
'Apr': '4月',
'Are you sure you want to delete this object?': 'このオブジェクトを削除してもよろしいですか?',
'Aug': '8月',
'Back': '戻る',
'Back to the web2py-plugin list': 'web2pyプラグイン一覧に戻る',
'CMS based on Web2py.': 'Web2pyベースのCMSです。',
'Calendar': 'カレンダー',
'Cannot be empty': '空にすることはできません',
'Choose date': '日付を選択',
'Choose date time': '日時を選択',
'Choose time': '時刻を選択',
'Client IP': 'Client IP',
'Cloudmap is a visual search engine for any contents with user evaluations.': 'Cloudmap は任意のユーザー評価コンテンツに対する視覚検索エンジンです。',
'Confirm': '許可する',
'Contact': 'お問い合わせ',
'Contact us': 'お問い合わせ',
'Day': '日',
'Dec': '12月',
'Demo': 'デモ',
'Description': '説明',
'Display: <b>%(start)s - %(end)s</b> of <b>%(total)s</b>': '全<b>%(total)s</b>件 (<b>%(start)s ～ %(end)s</b>件目)',
'Download Plugin': 'プラグインをダウンロード',
'E-mail': 'E-mail',
'Email': 'メールアドレス',
'Feb': '2月',
'First name': '名前',
'Fri': '金',
'Group ID': 'Group ID',
'Hour': '時',
'Introducing new products or services being developed by %s': '%s で開発している新商品やサービスを紹介します',
'Invalid email': '不正なemailです',
'Jan': '1月',
'Jul': '7月',
'Jun': '6月',
'Last name': '名字',
'Make facebook-like comment boxes': 'Facebookライクなコメントボックスを作成します',
'Make table rows permutable': 'テーブルの行を入れ替え可能にします',
'Mar': '3月',
'May': '5月',
'Message': '本文',
'Minute': '分',
'Mon': '月',
'Month': '月',
'Name': 'お名前',
'Next': '>',
'NoSQL package based on Cassandra.': 'CassandraベースのNoSQLパッケージです。',
'Not now': '無視する',
'Nov': '11月',
'OK': 'OK',
'Object or table name': 'Object or table name',
'Oct': '10月',
'Origin': 'Origin',
'Paginate: ': '1ページに:',
'Password': 'パスワード',
'Prev': '<',
'Record Created': 'レコードを作成しました',
'Record Deleted': 'レコードを削除しました',
'Record ID': 'Record ID',
'Registration key': '登録キー',
'Remove friend': '友達から削除',
'Reset Password key': 'パスワードキーをリセット',
'Role': 'ロール',
'Sat': '土',
'Second': '秒',
'See Demo': 'デモを見る',
'Select a file': 'ファイルを選択してください',
'Select an image': '画像を選択してください',
'Send': '送信する',
'Sep': '7月',
'Source code': 'ソースコード',
'Static files': '静的ファイル',
'Subject': '題名',
'Submit': '送信する',
'Sun': '日',
'Table name': 'Table name',
'Thank you for your inquiry.': 'お問い合わせありがとうございます。',
'There are no static files': '静的ファイルはありません',
'Thu': '木',
'Timestamp': 'タイムスタンプ',
'Tue': '火',
'Usage': '使用例',
'User ID': 'User ID',
'View all %s comments': 'コメント%s件をすべて見る',
'Website': 'ウェブサイト',
'Wed': '水',
'Write a comment..': 'コメントする',
'Year': '年',
'Your message has been sent.': 'メッセージが送信されました。',
'a built-in autocomplete widget': '組み込みの自動コンプリートウィジェット',
'a built-in options widget': '組み込みのオプションウィジェット',
"a web2py's plugin system": 'web2pyのプラグインシステム',
'close': '閉じる',
'delete': '削除',
'enter a file from %(min)g to %(max)g KB': '%(min)g ～ %(max)g KBのファイルを入力してください',
'enter a number between %(min)g and %(max)g': '%(min)g ～ %(max)g の間の数字を入力してください',
'enter a valid URL': '正しいURLを入力してください',
'enter a valid email address': '正しいメールアドレスを入力してください',
'enter a value': '値を入力してください',
'enter an integer between %(min)g and %(max)g': '%(min)g ～ %(max)g の整数を入力してください',
'enter an integer greater than or equal to %(min)g': '%(min)g 以下の整数を入力してください',
'enter date as %(format)s': 'enter date as %(format)s',
'enter from %(min)g to %(max)g characters': '%(min)g ～ %(max)g 文字を入力してください',
'invalid image': '不正な画像です',
'language': '言語',
'register': '登録',
'requesting': '申請しています',
'this discussion': 'この議論',
'under construction': '準備中',
'value not allowed': '許可された値ではありませｎ',
}
