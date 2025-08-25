from typing import NamedTuple, TypedDict, Final

class StudentInfoTuple(NamedTuple):
    name: str
    age: int

class StudentInfoDict(TypedDict):
    name: str
    age: int

# namedtupleの場合、内部情報を書き換えることができない
TARO: Final[StudentInfoTuple] = StudentInfoTuple('taro', 12)
# 下記行はエラーになる
#TARO.name = 'taro2'

# dictの場合内部情報を書き換えることができる
JIRO: Final[StudentInfoDict] = {'name': 'jiro', 'age': 9}
JIRO['name'] = 'jiro2'

