import streamlit as st

st.set_page_config(page_title="Morse Translator", page_icon="📡")
st.title("📡 Morse Code Translator")
st.write("Translate between English and Morse Code (Mobile Friendly)")

# ---------------- MORSE DICTIONARY ----------------
MORSE = {
    'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
    'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
    'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
    'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
    'Y':'-.--','Z':'--..',
    '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'
}

REVERSE_MORSE = {v: k for k, v in MORSE.items()}

# ---------------- MODE ----------------
mode = st.radio(
    "Select Translation Mode",
    ["English → Morse", "Morse → English"]
)

# ---------------- INPUT ----------------
text = st.text_area("Enter text (no Ctrl needed):", height=120)

# ---------------- BUTTON ----------------
if st.button("🔁 Translate"):
    if not text.strip():
        st.warning("Please enter some text")
    else:
        if mode == "English → Morse":
            result = " ".join(MORSE.get(c.upper(), "") for c in text if c != " ")
            st.subheader("📡 Morse Code")
            st.success(result)

        else:
            words = text.split(" ")
            result = "".join(REVERSE_MORSE.get(w, "?") for w in words)
            st.subheader("🔤 English Text")
            st.success(result)
