"""MainMatrix - \u043D\u0435\u0431\u043E\u043B\u044C\u0448\u0430\u044F \u0431\u0438\u0431\u043B\u0438\u043E\u0442\u0435\u043A\u0430 \u0434\u043B\u044F \u0443\u043F\u0440\u043E\u0449\u0435\u043D\u0438\u044F \u0440\u0430\u0431\u043E\u0442\u044B \u0441 \u043C\u0430\u0442\u0440\u0438\u0446\u0430\u043C\u0438
\u0420\u0430\u0437\u0440\u0430\u0431\u043E\u0442\u0447\u0438\u043A: MainPlay TG
https://t.me/MainPlay_InfoCh"""

__version_tuple__=(0,0,1)
__import_data__={
  "{name}=main.{name}":[
    "DictWithStr",
    "DictWithTuple",
    "DontFill",
    "ListsInList",
    "matrix",
    "PillowImage",
    "WrongCoordinates",
    ]
  }
__depends__={
  "required":[],
  "optional":[
    "PIL",
    ]
  }
__scripts__=[]
__all__=[]
__import_errors__={}
import MainMatrix.main as main
for code,names in __import_data__.items():
  for name in names:
    try:
      exec(code.format(name=name))
      __all__.append(name)
    except Exception as e:
      __import_errors__[name]=e
__all__.sort()
__version__="{}.{}.{}".format(*__version_tuple__)
del code,names,name