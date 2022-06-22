def on_logo_long_pressed():
    global gjetning, aktivt_tall
    gjetning = ""
    aktivt_tall = -1
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    global aktivt_tall
    if aktivt_tall == len(alfabet):
        aktivt_tall = -1
    aktivt_tall += 1
    basic.show_string(alfabet.char_at(aktivt_tall), 10)
input.on_button_pressed(Button.A, on_button_pressed_a)

def checkAnswer():
    global gjetning
    if gjetning == svar:
        basic.show_icon(IconNames.YES)
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.happy),
            SoundExpressionPlayMode.UNTIL_DONE)
        basic.clear_screen()
        basic.pause(100)
        for index in range(3):
            basic.show_string("" + (premie))
            basic.pause(500)
        if len(riktigGjettingsMelding) > 0:
            basic.show_string("" + (riktigGjettingsMelding))
    else:
        basic.show_icon(IconNames.NO)
        gjetning = ""
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.sad),
            SoundExpressionPlayMode.UNTIL_DONE)
        if len(feilGjettingsMelding) > 0:
            basic.show_string("" + (feilGjettingsMelding))

def on_button_pressed_ab():
    global gjetning, aktivt_tall
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            400,
            600,
            255,
            0,
            100,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
    gjetning = "" + gjetning + alfabet.char_at(aktivt_tall)
    aktivt_tall = -1
    if len(gjetning) == len(svar):
        checkAnswer()
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global aktivt_tall
    if aktivt_tall <= 0:
        aktivt_tall = len(alfabet)
    aktivt_tall += -1
    basic.show_string(alfabet.char_at(aktivt_tall), 10)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global gjetning, aktivt_tall
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            400,
            600,
            255,
            0,
            100,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
    gjetning = "" + gjetning + alfabet.char_at(aktivt_tall)
    aktivt_tall = -1
    if len(gjetning) == len(svar):
        checkAnswer()
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def startupDisplay():
    basic.show_string("#")
    basic.show_number(oppgavenummer)
    basic.clear_screen()
    basic.show_string("#Tegn:")
    basic.show_number(len(svar))
    if len(velkomstMelding) > 0:
        basic.show_string("" + (velkomstMelding))
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
aktivt_tall = 0
gjetning = ""
alfabet = ""
riktigGjettingsMelding = ""
feilGjettingsMelding = ""
velkomstMelding = ""
premie = ""
svar = ""
oppgavenummer = 0
# Denne variabelen er et heltall (integer). Dette er oppgavenummeret eller postnummeret. Det kan hjelpe deg å sortere microbitene og det kan hjelpe elevene til å finne ut rekkefølgen på oppgavene.
oppgavenummer = 1
# Denne variabelen er en tekststreng (string). Strengen kan enten inneholde 3 ulike typer tegn: 
# 1. STORE BOKSTAVER
# 2. små bokstaver
# 3. tallene 0 til 9, samt kommategn og brøkstrek (0123456789,/)
svar = "1/3"
# Denne variabelen er en tekststreng (string). Dette er premien eller hintet som elevene får med seg videre til neste oppgave
premie = "K"
# Denne meldingen vises til elevene før oppgaven. Kan f.eks. inneholde hint.
velkomstMelding = ""
# Denne teksten vises til elevene dersom de gjetter feil. Kan f.eks. inneholde hint.
feilGjettingsMelding = ""
# Denne teksten vises til elevene hvis de gjetter riktig. Kan f.eks. inneholde instruksjoner om hvor de finner neste oppgave.
riktigGjettingsMelding = ""
startupDisplay()
if "abcdefghijklmnopqrstuvwxyz".includes(svar.char_at(0)):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
elif "ABCDEFGHIJKLMNOPQRSTUVWXYZ".includes(svar.char_at(0)):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
else:
    alfabet = "0123456789,/"
gjetning = ""
aktivt_tall = -1