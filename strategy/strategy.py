from abc import ABCMeta, abstractmethod
import random
from strategy.hand import Hand
from another_module.another_sub import another_sub

# from .hand import Hand


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def nextHand(self):
        pass

    @abstractmethod
    def study(self, win):
        pass


class PreventLoseStrategy(Strategy):
    def __init__(self):
        self.__opponentLastHand = None
        self.__myPrevHand = Hand.getHand(random.randint(0, 2))  # 初回はランダム
        self.__lastResult = None  # 前回の勝敗結果
        self.__gameCount = 0
        another_sub()
        print("PreventLoseStrategy initialized.")

    def nextHand(self):
        self.__gameCount += 1

        if self.__opponentLastHand is None:
            # 初回はランダムな手を出す
            self.__myPrevHand = Hand.getHand(random.randint(0, 2))
        else:
            # CircularStrategyに特化した戦略：
            # CircularStrategyは グー(0) → チョキ(1) → パー(2) → グー(0) の順番
            # 相手の次の手を予測して、それに勝つ手を出す

            opponent_hand_value = self.__opponentLastHand._Hand__handvalue

            # 相手の次の手を予測（CircularStrategyの場合）
            predicted_next_hand = (opponent_hand_value + 1) % 3

            # 予測した手に勝つ手を出す
            winning_hand_value = (predicted_next_hand + 2) % 3
            self.__myPrevHand = Hand.getHand(winning_hand_value)

        return self.__myPrevHand

    def study(self, win):
        # 勝敗結果を記録
        if win:
            self.__lastResult = "win"
        elif win is False:  # 明示的にFalseをチェック
            self.__lastResult = "lose"
        else:
            self.__lastResult = "draw"

    def setOpponentHand(self, opponentHand):
        """相手の手を記録するメソッド"""
        self.__opponentLastHand = opponentHand
