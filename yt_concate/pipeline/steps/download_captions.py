from pytube import YouTube
from .step import Step
from .step import StepException
import time
import os

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        # download the package by:  pip install pytube
        start = time.time()
        for url in data:
            __ = utils.get_caption_filepath(url)
            if os.path.exists(__) and os.path.getsize(__) > 0:
                print('found existing caption file for', url)
                continue
            print(url)
            try:
                source = YouTube(url)
                # try 'en' first then 'a.en' for auto-generated captions
                en_caption = source.captions.get_by_language_code('en')
                if en_caption is None:
                    en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error when downloading caption for', url, "this video may not have captions")
                continue

            # print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

            end = time.time()
            print('took', end - start, 'seconds')
            # break
