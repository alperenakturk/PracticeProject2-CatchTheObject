import time
import turtle
from random import randint

# Ekranı ayarlama
catch_board = turtle.Screen()
catch_board.tracer(0, delay=0)  # Animasyonların kontrolü ve hızı için kullanılır
catch_board.bgcolor("light blue")
catch_board.title("Catch The Object")

# Oyuncu kurulum
player = turtle.Turtle()
player.shape("turtle")  # Kaplumbağa şeklini ayarladık
player.penup()  # Çizgi çizmeyi önlemek için kalemi kaldırdık
player.goto(0, 0)  # Kaplumbağayı başlangıç pozisyonuna getirdik

# Puan tablosu
points = turtle.Turtle()
points.penup()  # Kalemi kaldır
points.goto(-65, 270)
points.color("black")
style_score = ('Courier', 25)
points.hideturtle()
score_point = 0
points.write(f"Puan: {score_point}", font=style_score)

# Zamanlayıcı
timer_text = turtle.Turtle()
timer_text.penup()  # Kalemi kaldır
timer_text.goto(-65, 300)
timer_text.color("black")
style_timer = ("Courier", 25)
timer_text.hideturtle()

countdown_time = 30  # Geri sayım süresi (saniye)
baslangic = time.time()


def get_point(x, y):
    if countdown_time > 0:
        global score_point
        score_point += 1
        points.clear()
        points.write(f"Puan: {score_point}", font=style_score)
    else:
        print("")



def kaybol():
    player.hideturtle()  # Kaplumbağayı kaybol
    catch_board.update()
    catch_board.ontimer(gorun, 750)  # 1 saniye sonra tekrar çağır

def gorun():
    player.goto(randint(-250, 250), randint(-250, 250))  # Yeni rastgele konuma git
    player.showturtle()  # Kaplumbağayı görünür yap
    catch_board.update()
    catch_board.ontimer(kaybol, 1000)  # 1 saniye sonra tekrar çağır

# Geri sayım ve oyun döngüsü
def countdown():
    global countdown_time
    kalan_sure = countdown_time - int(time.time() - baslangic)
    if kalan_sure >= 0:
        timer_text.clear()
        timer_text.write(f"Süre: {kalan_sure}", font=style_timer)
        catch_board.update()
        catch_board.ontimer(countdown, 1000)
    else:
        timer_text.clear()
        timer_text.write("Süre doldu!", font=style_timer)
        catch_board.update()

# İlk çağrılar
player.onclick(get_point)  # Olay işleyicisini burada bir kez ayarlıyoruz
kaybol()
countdown()

turtle.done()
