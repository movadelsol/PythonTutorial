from strategy.strategy import PreventLoseStrategy
from strategy.player import Player

# import strategy as stg


def startMain():
    player1 = Player("Taro", PreventLoseStrategy())
    player2 = Player("Hana", PreventLoseStrategy())


def testPreventLoseStrategy():
    """PreventLoseStrategyのテスト関数"""
    print("=== PreventLoseStrategy vs CircularStrategy Test ===")

    prevent_strategy = PreventLoseStrategy()
    player1 = Player("PreventLose", prevent_strategy)
    player2 = Player("Circular", prevent_strategy)


if __name__ == "__main__":
    # 元のテスト
    startMain()

    print("\n" + "=" * 50 + "\n")

    # PreventLoseStrategyのテスト
    testPreventLoseStrategy()
