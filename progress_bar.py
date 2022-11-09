from time import sleep


def progress(percent=0, width=1):
	left = width * percent
	right = width - left
	print('\r[','=' * left, ' ' * right, ']',
		f'{percent:.0f}%',
		sep='', end='', flush=True)


for i in range(100):
	progress(i)
	sleep(0.2)
print("\n")
