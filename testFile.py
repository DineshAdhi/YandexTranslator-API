import YandexTranslator

key = "trnsl.1.1.20170508T175121Z.c2202e77aa3bb4a7.7d73016a5863e323330bc11d1ba6a32f73dda0a2"

translator = YandexTranslator.translator(key);

translator.translate(text, "ta")
