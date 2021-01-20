def on_button_pressed_a():
    global score
    score += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pulsed_p1_high():
    global score
    score += 1
pins.on_pulsed(DigitalPin.P1, PulseValue.HIGH, on_pulsed_p1_high)

score = 0
basic.show_icon(IconNames.YES)
basic.pause(100)

def on_forever():
    pins.set_pull(DigitalPin.P1, PinPullMode.PULL_DOWN)
    while score != 5:
        basic.show_string("" + str(score))
    for index in range(4):
        basic.show_string("5")
        basic.show_icon(IconNames.HAPPY)
    music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
        MelodyOptions.ONCE)
    basic.pause(5000)
basic.forever(on_forever)
