import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Morse Code Translator", page_icon="📡")
st.title("📡 Morse Code Translator")
st.write("Translate between **English** and **Morse Code**")

# ---------------- MORSE DICTIONARY ----------------
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}

# ---------------- FUNCTIONS ----------------
def english_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE.get(char, '') for char in text)

def morse_to_english(code):
    words = code.split(' / ')
    decoded = []

    for word in words:
        letters = word.split()
        decoded_word = ''.join(REVERSE_MORSE.get(letter, '') for letter in letters)
        decoded.append(decoded_word)

    return ' '.join(decoded)

# ---------------- UI ----------------
mode = st.radio("Select Translation Mode", ["English → Morse", "Morse → English"])

user_input = st.text_area("Enter text", height=120)

if user_input:
    if mode == "English → Morse":
        output = english_to_morse(user_input)
        st.subheader("📡 Morse Code")
        st.code(output)

    else:
        output = morse_to_english(user_input)
        st.subheader("🔤 English Text")
        st.success(output)
        
