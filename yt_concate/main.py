from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCJsN2KCAD7qkA6-fOeB2fOw'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
