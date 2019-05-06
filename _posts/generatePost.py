from datetime import date
from datetime import datetime

series = "Bungo Stray Dogs"
episode = "28"
magnet = ""

series_lower = series.lower().replace(" ", "-")
date = date.today()
time = datetime.now().strftime("%H:%M:%S")
filename = "{date}-{series}-{episode}.md".format(date = date, series = series_lower, episode = episode)

with open(filename, "w+") as post:
	post.write("---\n")
	post.write("layout: post\n")
	post.write("title: '{series} - {episode}'\n".format(series = series, episode = episode))
	post.write("image: '/assets/img/{series}-{episode}.jpg'\n".format(series = series_lower, episode = episode))
	post.write("date: {date} {time}\n".format(date = date, time = time))
	post.write("categories:\n")
	post.write("- {series}\n".format(series = series))
	post.write("---\n")
	post.write("\n")
	post.write("<img src='{{ page.image }}' alt='' width='640' height='360'>\n")
	post.write("\n")
	post.write("<a href='{magnet}'>Magnet</a>".format(magnet = magnet))
