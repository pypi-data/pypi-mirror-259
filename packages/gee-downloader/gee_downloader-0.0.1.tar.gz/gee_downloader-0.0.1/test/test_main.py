import pytest
import os
from gee_downloader import read_polygon

def test_read_polygon():
    polygon = read_polygon(os.path.join('test', 'munich.json'))
    assert(polygon ==
        {
            "coordinates": [
                [
                    [
                        10.998896421666416,
                        48.34257717723628
                    ],
                    [
                        10.998896421666416,
                        47.80206314145221
                    ],
                    [
                        12.093460214218908,
                        47.80206314145221
                    ],
                    [
                        12.093460214218908,
                        48.34257717723628
                    ],
                    [
                        10.998896421666416,
                        48.34257717723628
                    ]
                ]
            ],
            "type": "Polygon"
        })
