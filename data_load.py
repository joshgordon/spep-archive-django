#!/usr/bin/env python3
import os
from mutagen.id3 import ID3
import datetime
from dateutil.parser import parse
import re

# django stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spepArchiveDjango.settings")
from django.conf import settings

from archive.models import Series, Pastor, Sermon, Type
from django.utils import dateparse


sermons_type = Type.objects.get(name="Sermon")

path = "/data/sermons"

regex = re.compile(r"[^ _.]+")

all_pastors = []
all_series = []
all_data = []

for subdir, dirs, files in os.walk(path):
    for file in files:
        if 'Music' in subdir.split('/') or 'Good News' in subdir.split('/'):
            continue
        filepath = os.path.join(subdir, file)
        info = { "title": file.split('.')[0], "series": subdir.split('/')[-1],
            "author": "", "date": datetime.date(1970, 1, 1),
            "filename": '/'.join(filepath.split('/')[3:]), "seq": 0, "verse": ""}
        taginfo = None
        try:
            taginfo = ID3(filepath)
        except:
            print("Taginfo fail " + filepath)
        try:
            info['title'] = taginfo.get('TIT2').text[0]
        except:
            print("Titleinfo fail " + filepath)
        try:
            info['series'] = taginfo.get('TALB').text[0]
        except:
            print("Series info fail " + filepath)
        try:
            info['author'] = taginfo.get('TPE1').text[0]
        except:
            print("author FAIL on " + filepath)
        try:
            info['seq'] = int(taginfo.get('TRCK').text[0])
        except:
            print("seq fail on " + filepath)
        try:
            info['verse'] = taginfo.get('COMM::\x00\x00\x00').text[0]
        except  :
            try:
                info['verse'] = taginfo.get('COMM::eng').text[0]
            except:
                print("Comment fail on " + filepath)
        try:
            info['date'] = parse(regex.findall(file)[0])
        except ValueError:
            print("Date fail on " + filepath)
            pass

        if info['series'] not in all_series:
            all_series.append(info['series'])
        if info['author'] not in all_pastors:
            all_pastors.append(info['author'])
        all_data.append(info)

pastor_map = {}
series_map = {}

for pastor in all_pastors:
    try:
        p = Pastor(name=pastor)
        p.save()
        pastor_map[pastor] = p
    except:
        print("psator %s is a duplicate" % pastor)
        if pastor not in pastor_map:
            pastor_map[pastor] = Pastor.objects.get(name=pastor)
        pass

for series in all_series:
    try:
        s = Series(name=series)
        s.save()
        series_map[series] = s
        print(s)
    except:
        print("Series %s is a duplicate" % series)
        if series not in series_map:
            series_map[series] = Series.objects.get(name=series)
        pass

print(series_map)
print(pastor_map)

sermon_type = Type.objects.get(name="Sermon")
for sermon in all_data:
    sermon_series = None
    sermon_author = None
    sermon_date = None
    if sermon['author'] != '':
        sermon_author = pastor_map[sermon['author']]
    if sermon['series'] != '':
        sermon_series = series_map[sermon['series']]
    kwargs = {
        'sermon_title': sermon['title'],
        'pastor': sermon_author,
        'verse': sermon['verse'],
        'type': sermon_type,
        'series': sermon_series,
        'pub_date': sermon['date'],
        'url': sermon['filename'],
        'sequence_num': sermon['seq']
    }
    s = Sermon(**kwargs)
    s.save()
