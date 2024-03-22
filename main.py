from Config import Config
from audio.generate_audio import generate_audio
from figures.Divided import Divided
from figures.Eight import Eight
from figures.Equals import Equals
from figures.Five import Five
from figures.Four import Four
from figures.Fraction import Fraction
from figures.Minus import Minus
from figures.Nine import Nine
from figures.One import One
from figures.Plus import Plus
from figures.Sequence import Sequence
from figures.Seven import Seven
from figures.Six import Six
from figures.Three import Three
from figures.Times import Times
from figures.Two import Two
from figures.Zero import Zero
from recording.concat2video import concat2video
from recording.concat_videos import concat_videos

if __name__ == '__main__':
    start_x, y_coor = Config.start_x, Config.start_y
    action_spaces = [
        [
            [Equals(), Seven(), Divided(), Times(),
             Sequence(One(), Plus(), Fraction(Two(), Three()), Four(), width=300, height=100)],
            [Fraction(One(), Seven()), One()],
            [Plus(), Minus(), ],
            [Zero(), One(), Two(), Three(), Four(), Five(), Six(), Seven(), Eight(), Nine(), ],
            [Zero(), Eight(), ],
        ],
    ]
    for action_space in action_spaces:
        for row in action_space:
            x_coor = start_x
            for figure in row:
                figure.x_coor = x_coor
                figure.y_coor = y_coor
                x_coor += figure.width
            y_coor -= max(figure.height for figure in row)
        for figure in (figure for row in action_space for figure in row):
            figure.draw()
            # figure.undo()
        concat2video()
    for text_translate in Config.texts_to_translate:
        generate_audio(text_translate)
    concat_videos()

