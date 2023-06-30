'''


PYTHON WEB BASICS
EXAM

'''

from PIL import ImageGrab
ss_region = (50, 110, 800, 670)
ss_img = ImageGrab.grab(ss_region)
ss_img.save("py_web_exam.jpg")
