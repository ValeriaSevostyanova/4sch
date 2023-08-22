import sys
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor


class Demo(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.set_background_color(0.0, 0.5, 0.75, 1)
        self.accept('escape', sys.exit)
        self._panda = Actor('models/panda-model.egg', {
            'walk': 'models/panda-walk4.egg',
        })
        self._panda.set_h(60)
        self._panda.set_scale(0.005)
        self._panda.reparent_to(self.render)
        self._panda.loop('walk')
        self.cam.set_pos(0, -20, 2)


demo = Demo()
demo.run()
