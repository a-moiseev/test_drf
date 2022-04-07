from pathlib import Path
from django.test import TestCase
from .models import Video
from django.core.files import File
from django.conf import settings


class VideoTest(TestCase):
    def setUp(self):
        path = Path(settings.BASE_DIR) / "videos/test_file/test.avi"
        f = open(path, 'rb')
        file = File(f, name=path.name)
        v = Video.objects.create(title="VideoTest", file=file)

    def test(self):
        video_test = Video.objects.get(title="VideoTest")
        self.assertEqual(video_test.md5, "26f4620de01969656a5dd2906937eb7e")
