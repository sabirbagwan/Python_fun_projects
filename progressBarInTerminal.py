import math
import colorama

# def progress_bar(progress, total, color = colorama.Fore.LIGHTYELLOW_EX):
def progress_bar(progress, total):
    percent = 100 * (progress/float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end = "\r")
    # print(color + f"\r|{bar}| {percent:.2f}%", end = "\r")
    # if progress == total:
        # print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end = "\r")
        # print(colorama.Fore.RESET)


numbers = [x * 5 for x in range(2000, 2300)]
results = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))
