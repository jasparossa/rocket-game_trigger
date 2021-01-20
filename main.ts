input.onButtonPressed(Button.A, function () {
    score += 1
})
input.onPinPressed(TouchPin.P2, function () {
    music.playTone(262, music.beat(BeatFraction.Whole))
    score += 1
})
let score = 0
basic.showIcon(IconNames.Yes)
basic.pause(100)
while (score < 5) {
    basic.showString("" + (score))
}
for (let index = 0; index < 4; index++) {
    basic.showString("5")
    basic.showIcon(IconNames.Happy)
    music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
    basic.pause(5000)
}
basic.forever(function () {
	
})
