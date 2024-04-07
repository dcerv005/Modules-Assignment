def mood_response(mood):
    list_of_moods = ['happy', 'sad', 'excited']
    if mood.lower() not in list_of_moods:
        return "Do not recognize the mood."
    else:
        if mood.lower() == 'happy':
            return "Glad to hear that you're feeling happy!"
        elif mood.lower() == 'sad':
            return "The day will get better!"
        elif mood.lower() == 'excited':
            return "Nice!"