import board
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.handlers.sequences import send_string
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D26,board.D27,board.D28,board.D8,)
keyboard.row_pins = (board.D29,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# LAYERS
layers = Layers()

# ENCODER
encoder_handler = EncoderHandler()

# HOLDTAP
holdtap = HoldTap()

# TAPDANCE
tapdance = TapDance()
tapdance.tap_time = 550

# MODULES
keyboard.modules.append(layers)
keyboard.modules.append(encoder_handler)
keyboard.modules.append(MediaKeys())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(holdtap)
keyboard.modules.append(tapdance)

encoder_handler.pins = ((board.D21,board.D23,None,True),)

rgb = RGB(
    pixel_pin=board.D4,
    num_pixels=3,
    rgb_order=(1,0,2),
    hue_default=170, #blue
    sat_default=255,
    val_default=255,
    animation_mode=AnimationModes.RAINBOW,
    refresh_rate=60,
)
keyboard.extensions.append(rgb)

# LAYER DEFINITIONS
LYR_BASE = 0
LYR_MACRO = 1
LYR_RGB = 2
LYR_MOUSE = 3

# LAYER SWITCH KEYS
TO_BASE = KC.DF(LYR_BASE)
TO_MACRO = KC.DF(LYR_MACRO)
TO_RGB = KC.DF(LYR_RGB)
TO_MOUSE = KC.DF(LYR_MOUSE)

# HELPER KEYS
TRANS = KC.TRNS
LGUI = KC.HT(KC.C, KC.LGUI) # holdtap

# MACROS
SAVE = simple_key_sequence(
    (
        KC.LCTL(KC.S), # ctrl+s
    )
)
zbroja = send_string("ale to to nie ja mam problem czy kompleksy tylko wy xd to wy sie przypierdalacie doslownie o kazda pierdole gwarantuje ci ze kolejne spierdolone miejsce to pisania w internecie nie jest mi potrzebne do zycia a przychodzenie tutaj to tylko rozrywka zeby posmiac siie z paru kretynow, ktorzy mysla ze kogokolwiek obchodzi co pisza przez pol dnia naprawde sa ludzie na ktorych bardziej mi zalezy od was i totalnie mam w chuju co myslicie o mnie i na jakikolwiek inny temat")
kekw = send_string(":kekw:")
swieta = send_string("Wesolych Swiat!")


# RGB mode toggle (tap dance)
RGB_TD = KC.TD(
    KC.RGB_MODE_PLAIN, # 1tap
    KC.RGB_MODE_BREATHE, # 2tap
    KC.RGB_MODE_RAINBOW, # 3taps
    KC.RGB_MODE_BREATHE_RAINBOW, # 4taps
    KC.RGB_MODE_KNIGHT, # 5taps
    KC.RGB_MODE_SWIRL, # 6taps
)
RGB_COL_CH = KC.HT(KC.RGB_SAI, KC.RGB_SAD, repeat=HoldTapRepeat.HOLD)


# KEYMAP
keyboard.keymap = [
    # LAYER 0: BASE-media
    [
    KC.MNXT, KC.MPLY, KC.MPRV, KC.TD(KC.MUTE, TO_MACRO, TO_RGB), # last one is encoder
    ],
    # LAYER 1: MACRO
    [
    swieta, kekw, zbroja, KC.TD(KC.MUTE, TO_RGB, TO_RGB), # last one is encoder
    ],
    # LAYER 2: RGB 
    [
    KC.RGB_TOG, RGB_TD, RGB_COL_CH, KC.TD(KC.MUTE, TO_MOUSE, TO_RGB), # last one is encoder
    ],
    # LAYER 3: MOUSE
    [
    KC.C, KC.H, KC.U, KC.TD(KC.MUTE, TO_BASE, TO_RGB), # last one is encoder
    ],
]
encoder_handler.map = [
            ((KC.VOLD, KC.VOLU),),       
            ((KC.MW_UP, KC.MW_DN),),      
            ((KC.RGB_HUI, KC.RGB_HUD),),       
            ((KC.MW_LEFT, KC.MW_RIGHT),),      
            ]

if __name__ == '__main__':
    keyboard.go()
