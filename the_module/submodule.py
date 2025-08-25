# import enduro
import sys, os
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))
from another_module.another_sub import another_sub
from enduro import long_running_task

print(f"from submodule sys.path:{sys.path}")


def submodule_function():
    print("サブモジュールの関数が呼び出されました。")
    another_sub()
    if False:
        long_running_task()
    print("サブモジュールの処理が完了しました。")


if __name__ == "__main__":
    submodule_function()
