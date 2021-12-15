# A-SOUL-Danmu

## 关于搜索模块
  关键字：搜索内容1；；搜索内容2
### name：
  通过发送者的用户名检索内容，默认通过kmp搜索。使用nameF进行完全匹配检查
### id：
  通过发送者的uid检索内容，注意，id和idF相同
### danmu：
  通过弹幕内容检索， danmuF同上
### fans：
  注意，不支持仅搜索粉丝牌等级，例如fans：21
  可以仅搜索粉丝牌名称，例如fans：奶淇琳
  或者同时搜索等级和名称，等级和名称前使用-连接，例如fans：21-奶淇琳
  fansF同上

### 同时检索一个关键字下的多个内容：
  例如同时搜索奶淇琳和顶碗人：
  fans：奶淇琳；；顶碗人

## 关于自己打包软件
  Core.py对应LiveCore.exe
  SearchCore.py对应SearchCore.exe
  pyinstaller参数 -F就可以，-w的话没有控制台输出。
