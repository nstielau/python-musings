#!/usr/bin/env python

import time
import unittest

class Logger():
    def __init__(self, time_window, max_messages):
        self.drop_count = 0
        self.msg_timstamps = []
        self.time_window = time_window
        self.max_messages = max_messages

    def log(self, msg):
        if len(self.msg_timstamps) < self.max_messages or \
           self.msg_timstamps[-self.max_messages] < time.time() - self.time_window:
            self.msg_timstamps.append(time.time())
            # We only need max_messages to tell if we are should drop,
            # truncate to save memory
            self.msg_timstamps[-self.max_messages:]
        else:
            self.drop_count = self.drop_count + 1


class LogRatelimitedTest(unittest.TestCase):
    def test_create_logger(self):
        logger = Logger(1, 5)
        self.assertNotEqual(logger, None)

    def test_rate_limit_should_drop_none_with_few_msgs(self):
        logger = Logger(1, 5)
        for i in range(4):
            logger.log(i)
        self.assertEqual(0, logger.drop_count)

    def test_should_rate_limit(self):
        logger = Logger(1, 5)
        for i in range(10):
            logger.log(i)
        self.assertEqual(5, logger.drop_count)

if __name__ == "__main__":
    unittest.main()
