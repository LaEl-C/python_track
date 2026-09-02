def man_pal(text):
    cleaned_text = text.replace(" ", "").lower()

    textb = ""
    for ch in reversed(cleaned_text):
        textb += ch
    # print(textb)
    print(True) if cleaned_text == textb else print(False)

man_pal("madam")
man_pal("Davidevi")