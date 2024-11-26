# Aplicacion del servidor
from microdot import Microdot, send_file
from microdot import do_connect
from boot import led_1, led_2, led_3
import neopixel
import time
import onewire
import ds18x20

buzzer = Pin(14, Pin.OUT)
ds = Pin(19)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
temp_celsius = 24

do_connect()

app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')


@app.route("/<dir>/<file>")
async def static(request, dir, file):
    return send_file("/" + dir + "/" + file)


@app.route('/sensors/ds18b20/read')
async def temperature_measuring(request):
    global ds_sensor
    ds_sensor.convert_temp()
    time.sleep_ms(1)
    roms = ds_sensor.scan()
    for rom in roms:
        temp_celsius = ds_sensor.read_temp(rom)
    
    json = {'temperature': temp_celsius};
    
    return json


@app.route('/setpoint/set/<int:value>')
async def setpoint_calculation(request, value):
    json = {}
    
    print("Calculate setpoint")
    
    if value >= temp_celsius:
        buzzer.on()
        json = {'buzzer': 'Encendido'}
        
    else:
        buzzer.off()
        json = {'buzzer': 'Apagado'}
    
    return json


app.run(port=80)