import random
import turtle
import time
turtle.register_shape("head.gif") #Turtle için resim tanıtıldı.
turtle.register_shape("start.gif")
#Karakter, score, ve zaman sayacı için çizim araçları tanımlandı.
turtle_instance=turtle.Turtle()
score=turtle.Turtle()
Time=turtle.Turtle()
buton_basla=turtle.Turtle()

#Karakter resmi eklendi
turtle_instance.shapesize(2)
turtle_instance.shape("head.gif")

#Oyunun oynanılacağı ekran oluşturuldu , başlık ve arkaplan eklendi.
draw_board=turtle.Screen()
draw_board.bgpic("cs.gif")
draw_board.title("Aim Trainer")


turtle_instance.penup()
turtle_instance.speed(0)

#Zaman göstergesinin yeri ve görünürlüğü ayarlandı.
Time.hideturtle()
Time.penup()
Time.goto(0,250)
Time.speed(0)

#Score göstergesinin yeri ve görünürlüğü ayarlandı. Ekrana ilk score değeri yazıldı.
score.penup()
score.hideturtle()
score.speed(0)
score.goto(0, 275)
score.write("SCORE:0", align="center", font=("Arial", 20, "normal"))

buton_basla.penup()
buton_basla.speed(0)
buton_basla.shape("start.gif")
buton_basla.goto(0,0)


#Tıklamaları algılamak ve saymak için fonksiyon tanımlandı.#
sayac=0
def click(x, y):
    if not hasattr(click, 'sayac'):
        click.sayac = 0
    turtle_instance.hideturtle()
    click.sayac += 1
    score.clear()
    score.write("SCORE:%s"%click.sayac, align="center", font=("Arial", 15, "normal"))

    #Butona basıldığında algılaması için fonksiyon yazıldı
basla= None
def click_basla(x, y):
    global basla
    if hasattr(click_basla, 'sayac'):
        click_basla.sayac = True
        basla = click_basla.sayac
    else:
        click_basla.sayac = False
        basla = click_basla.sayac

#Zaman sayacı için değişken belirlendi.


while True:
    t = 1
    buton_basla.onclick(click_basla)
    if basla==True:
        buton_basla.hideturtle()
        time.sleep(1)
    #Oyun for döngüsüyle başlatıldı.
        for i in range(60):
            vakit=60-i
            Time.write("Time: %s"%vakit, align="center", font=("Arial", 15, "normal"))

            #Karakterin x,y konumu random komutuyla belirlendi
            x=random.randint(-250,250)
            y=random.randint(-235,235)
            turtle_instance.setposition(x,y)
            turtle_instance.showturtle()

            #Oyun ilerledikçe karakter yer değiştirmesini hızlandırmak için bekleme süresi her döngüde kısaltıldı.
            t-=0.01
            time.sleep(t)
            turtle_instance.onclick(click)
            turtle_instance.hideturtle()
            time.sleep(0.1)
            Time.clear()
    buton_basla.showturtle()
    #Süre bitiminde ekrana Game Over! yazdırıldı.
    Time.write("Game Over!", align="center", font=("Arial", 15, "normal"))
    basla=False

draw_board.mainloop()