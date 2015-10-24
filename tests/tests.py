import movement_analyzer
from structures import Cactus
import unittest


class TestMovementAnalyzer(unittest.TestCase):

    def setUp(self):
        self.obstacles = [Cactus(0, 20, 10), Cactus(21, 20, 10), Cactus(42, 20, 10)]

    def test_merge_obstacles(self):
        merged = movement_analyzer.merge_obstacles(self.obstacles, 2)
        self.assertEqual(len(merged), 1)

        merged_cactus = merged[0]
        x = merged_cactus.x
        width = merged_cactus.width
        self.assertEqual(x, 0)
        self.assertEqual(width, 62)

