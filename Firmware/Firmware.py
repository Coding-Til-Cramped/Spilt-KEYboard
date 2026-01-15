import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.split import Split

keyboard = KMKKeyboard()

# ==============================
# MATRIX CONFIG
# ==============================
keyboard.diode_orientation = DiodeOrientation.COLUMNS

# 🔴 REPLACE THESE WITH YOUR REAL MCU PINS
keyboard.col_pins = (
    board.P0_03,  # COL0
    board.P0_28,  # COL1
    board.P0_29,  # COL2
    board.P0_04,  # COL3
    board.P0_05,  # COL4
)

keyboard.row_pins = (
    board.P1_15,  # ROW0
    board.P1_14,  # ROW1
    board.P1_13,  # ROW2
    board.P0_11,  # ROW3
    board.P0_02,  # ROW4 (thumb row)
)

# ==============================
# SPLIT (WIRED)
# ==============================
keyboard.split = True

keyboard.extensions.append(
    Split(
        split_type=Split.SPLIT_UART,
        uart_tx=board.P0_20,  # 🔴 SET
        uart_rx=board.P0_19,  # 🔴 SET
        uart_flip=True,
    )
)

# ==============================
# KEYMAP (42 KEYS TOTAL)
# ==============================
keyboard.keymap = [
    # Layer 0
    [
        # ----- LEFT HALF -----
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,
        KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,
        KC.A,  KC.S,  KC.D,  KC.F,  KC.G,
        KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,
        KC.SPC, KC.NO, KC.NO, KC.NO, KC.NO,

        # ----- RIGHT HALF -----
        KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,
        KC.Y,  KC.U,  KC.I,  KC.O,  KC.P,
        KC.H,  KC.J,  KC.K,  KC.L,  KC.SCLN,
        KC.N,  KC.M,  KC.COMM, KC.DOT, KC.SLSH,
        KC.ENT, KC.NO, KC.NO, KC.NO, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()
