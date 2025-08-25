import time


# TO INVOKE DO AS FOLLOWS;
# nohup python enduro.py &
def long_running_task():
    print("処理を開始します (約5分かかります)...", flush=True)
    for i in range(1, 6):
        time.sleep(60)  # 1分待機
        print(f"{i}分経過...", flush=True)
    print("処理が完了しました！", flush=True)


if __name__ == "__main__":
    long_running_task()
