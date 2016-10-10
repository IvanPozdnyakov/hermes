import unittest

import os
import sys
import time
import os.path as op
from functools import partial
from kivy.clock import Clock

main_path = op.dirname(op.dirname(op.abspath(__file__)))
sys.path.append(main_path)

from messanger import Messanger

class Test(unittest.TestCase):
    # sleep function that catches `dt` from Clock
    def pause(*args):
        time.sleep(0.000001)

    # main test function
    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Execute
        app.main_window.finish_init(None)
        app.main_window.add_conversation_to_UI()
        
        sc = app.main_window.ids['screen_controls']

        self.assertIn({'text':'conversation_0'},app.main_window.ids['conversation_list'].data)
        self.assertEqual(app.main_window.current_screen_index,2)
        self.assertEqual(app.main_window.latest_screen_id,1)
        self.assertEqual(sc.current, 'conversation_0')

        # Comment out if you are editing the test, it'll leave the
        # Window opened.
        app.stop()

    # same named function as the filename(!)
    def test_add_conversation_to_UI(self):
        app = Messanger()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()

if __name__ == '__main__':
    unittest.main()
