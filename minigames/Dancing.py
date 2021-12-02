from pynput import keyboard
from random import *


secret_len = randint(10,25)

secret_num = randrange(4**secret_len)


d = secret_num
n = 4
mission_num = ''
while d:
    mission_num += str(d%n)
    d = d // n

print(mission_num)
table = str.maketrans('0123', '→←↑↓')
arrow_mission = mission_num.translate(table)
print (arrow_mission)
  # 정확한 버튼을 누르면 앞에서부터 한개씩 글자가 없어지면 좋겠음


def key_press(key):
    #print(f'{key} pressed')

    if key == key.up:
        pass
    if key == key.down:
        pass
    if key == key.left:
        pass
    if key == key.right:
        pass
def key_release(key):
    # print(f'{key} release')
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()





#
#
# def on_press(key):
#     try:
#         print('Alphanumeric key pressed: {0} '.format(
#             key.char))
#     except AttributeError:
#         print('special key pressed: {0}'.format(
#             key))
#
# def on_release(key):
#     print('Key released: {0}'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False
#
# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()