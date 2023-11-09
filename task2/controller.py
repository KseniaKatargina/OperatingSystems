import os
import signal
import subprocess
import select

produced = 0


def signal_handler(signum, frame):
    global produced
    if signum == signal.SIGUSR1:
        print(f"Produced: {produced}")


def main():
    global produced
    signal.signal(signal.SIGUSR1, signal_handler)

    pipe0 = os.pipe()
    pipe1 = os.pipe()
    pipe2 = os.pipe()

    pid_1 = os.fork()

    if pid_1 == 0:  
        os.close(pipe1[0])
        os.dup2(pipe1[1], 1)
        subprocess.Popen(["python3", "producer.py"])
        exit(0)
    else:
        os.close(pipe1[1])
        pid_2 = os.fork()

        if pid_2 == 0:
            os.close(pipe0[1])
            os.close(pipe2[0])
            os.dup2(pipe0[0], 0)
            os.dup2(pipe2[1], 1)
            os.execl("/usr/bin/bc", "bc")
            exit(0)
        else:
            os.close(pipe0[0])
            os.close(pipe2[1])

            results = []
            while True:
                rlist, _, _ = select.select([pipe1[0]], [], [], 1)
                if rlist:
                    expression = os.read(pipe1[0], 100).decode("utf-8").strip()
                    if not expression:
                        break

                    os.write(pipe0[1], expression.encode("utf-8") + b"\n")
                    produced += 1
                    res = os.read(pipe2[0], 100).decode("utf-8").strip()
                    results.append((expression, res))

                # Выводите результаты каждую секунду
                for expression, res in results:
                    print(f"{expression} = {res}")
                results = []


if __name__ == "__main__":
    main()
