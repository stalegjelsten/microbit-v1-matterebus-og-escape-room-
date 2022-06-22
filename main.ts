input.onButtonPressed(Button.A, function () {
    if (aktivt_tall == alfabet.length) {
        aktivt_tall = -1
    }
    aktivt_tall += 1
    basic.showString(alfabet.charAt(aktivt_tall),5)
})
function checkAnswer () {
    if (gjetning == svar) {
        basic.showIcon(IconNames.Yes)
        basic.clearScreen()
        basic.pause(100)
        for (let index = 0; index < 3; index++) {
            basic.showString(premie)
            basic.pause(500)
        }
        if (riktigGjettingsMelding.length > 0) {
            basic.showString(riktigGjettingsMelding)
        }
    } else {
        basic.showIcon(IconNames.No)
        gjetning = ""
        if (feilGjettingsMelding.length > 0) {
            basic.showString(feilGjettingsMelding)
        }
    }
}
input.onGesture(Gesture.Shake, function () {
    gjetning = "" + gjetning + alfabet.charAt(aktivt_tall)
    aktivt_tall = -1
    if (gjetning.length == svar.length) {
        checkAnswer()
    }
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    gjetning = "" + gjetning + alfabet.charAt(aktivt_tall)
    aktivt_tall = -1
    if (gjetning.length == svar.length) {
        checkAnswer()
    }
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function () {
    if (aktivt_tall <= 0) {
        aktivt_tall = alfabet.length
    }
    aktivt_tall += -1
    basic.showString(alfabet.charAt(aktivt_tall),5)
})
function startupDisplay () {
    basic.showString("#")
    basic.showNumber(oppgavenummer)
    basic.clearScreen()
    basic.showString("#Tegn:")
    basic.showNumber(svar.length)
    if (velkomstMelding.length > 0) {
        basic.showString(velkomstMelding)
    }
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
}
let aktivt_tall = 0
let gjetning = ""
let alfabet = ""
let riktigGjettingsMelding = ""
let feilGjettingsMelding = ""
let velkomstMelding = ""
let premie = ""
let svar = ""
let oppgavenummer = 0
// Denne variabelen er et heltall (integer). Dette er oppgavenummeret eller postnummeret. Det kan hjelpe deg å sortere microbitene og det kan hjelpe elevene til å finne ut rekkefølgen på oppgavene.
oppgavenummer = 1
// Denne variabelen er en tekststreng (string). Strengen kan enten inneholde 3 ulike typer tegn:
// 1. STORE BOKSTAVER
// 2. små bokstaver
// 3. tallene 0 til 9, samt kommategn og brøkstrek (0123456789,/)
svar = "1/3"
// Denne variabelen er en tekststreng (string). Dette er premien eller hintet som elevene får med seg videre til neste oppgave
premie = "K"
// Denne meldingen vises til elevene før oppgaven. Kan f.eks. inneholde hint.
velkomstMelding = ""
// Denne teksten vises til elevene dersom de gjetter feil. Kan f.eks. inneholde hint.
feilGjettingsMelding = ""
// Denne teksten vises til elevene hvis de gjetter riktig. Kan f.eks. inneholde instruksjoner om hvor de finner neste oppgave.
riktigGjettingsMelding = ""
startupDisplay()
if ("abcdefghijklmnopqrstuvwxyz".includes(svar.charAt(0))) {
    alfabet = "abcdefghijklmnopqrstuvwxyz"
} else if ("ABCDEFGHIJKLMNOPQRSTUVWXYZ".includes(svar.charAt(0))) {
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
} else {
    alfabet = "0123456789,/"
}
gjetning = ""
aktivt_tall = -1
