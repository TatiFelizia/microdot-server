# Aplicacion del servidor
from microdot import Microdot, send_file
from microdot import do_connect
from boot import led_1, led_2, led_3
import neopixel

neo = neopixel.NeoPixel(Pin(27), 4)

for i in range(4):
    neo[i] = (0, 0, 0)

neo.write()

do_connect()

app = Microdot()

@app.route('/')
async def index(request):
    return send_file("index.html")

@app.route("/<dir>/<file>")
async def static(request, dir, file):
    return send_file("/" + dir + "/" + file)

@app.route('/led/toggle/<led>')
async def led_toggle(request, led):
    if led == "led1":
        led_1.value(not led_1.value())

    elif led == "led2":
        led_2.value(not led_2.value())

    elif led == "led3":
        led_3.value(not led_3.value())

@app.route('/rgbled/change/red/<int:red>')
async def rgb_led(request, red):
    global neo
    green = neo[0][1]
    blue = neo[0][2]
    
    for pixel in range(4):
        neo[pixel] = (red, green, blue)
        
    neo.write()
    
@app.route('/rgbled/change/blue/<int:blue>')
async def rgb_led(request, blue):
    global neo
    
    red = neo[0][0]
    green = neo[0][1]
    
    for pixel in range(4):
        neo[pixel] = (red, green, blue)
        
    neo.write()
    
@app.route('/rgbled/change/green/<int:green>')
async def rgb_led(request, green):
    global neo
    
    red = neo[0][0]
    blue = neo[0][2]
    
    for pixel in range(4):
        neo[pixel] = (red, green, blue)
        
    neo.write()

app.run(port = 80)
