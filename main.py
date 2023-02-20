from googletrans import Translator


def text_translater(text='Hello friend' , src='en' , dest='fi'):
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)
        
        return translation.text
    except Exception as ex:
        return ex
    

