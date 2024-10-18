from tkinter import *
from hitbox import Hitbox  # Импортируем класс Hitbox

class Tank:
    def init(self, canvas, x, y, color):
        self.canvas = canvas
        self.size = 50  # Размер танка (квадрата)
        self.hitbox = Hitbox(x, y, self.size, self.size)
        self.color = color
        self.rect = self.canvas.create_rectangle(x, y, x + self.size, y + self.size, fill=color, outline='black')

    def moveto(self, x, y):
        self.hitbox.moveto(x, y)
        self.canvas.coords(self.rect, x, y, x + self.size, y + self.size)

    def forward(self):
        self.moveto(self.hitbox.x, self.hitbox.y - 5)

    def backward(self):
        self.moveto(self.hitbox.x, self.hitbox.y + 5)

    def left(self):
        self.moveto(self.hitbox.x - 5, self.hitbox.y)

    def right(self):
        self.moveto(self.hitbox.x + 5, self.hitbox.y)

def check_collision():
    if player.hitbox.intersects(enemy.hitbox):
        print('Танки столкнулись')

def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()
    check_collision()

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

w = Tk()
w.title('Танки на минималках 2.0')
canvas = Canvas(w, width=800, height=600, bg='alice blue')
canvas.pack()

# Создаем танки как квадраты
player = Tank(canvas, x=100, y=100, color='red')   # Красный танк
enemy = Tank(canvas, x=200, y=100, color='blue')    # Синий танк
green_tank = Tank(canvas, x=300, y=100, color='green')  # Зеленый танк

w.bind('<KeyPress>', key_press)

w.mainloop()