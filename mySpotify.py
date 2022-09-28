import os, os.path
import pandas as pd
path = r'/Users/martinweiss/Documents/Python/Random Python Scripts/Spotify/Streaming History'
outputPath = r'/Users/martinweiss/Documents/Python/Random Python Scripts/Spotify/Streaming History'
fileCount = (len([entry for entry in os.listdir(path) if os.path.isfile(os.path.join(path, entry))]))
data = []
countList = []
files = os.listdir(path)
files.sort()
for file in files:
	if file.endswith('json'):
		count = file
		count = file.replace('StreamingHistory', '')
		count2 = count.replace('.json', '')
		count2 = int(count2)
		countList.append(count2)
		
sortedList = countList.sort()
list_2022 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
		
for json in countList:
	df = pd.read_json(r'/Users/martinweiss/Documents/Python/Random Python Scripts/Spotify/Streaming History/StreamingHistory' + str(json) + '.json')
	data.append(df)

data = pd.concat(data)
data.reset_index(drop=True, inplace=True)
data = data[data.msPlayed >= 30000]
artistList = (data['artistName']).tolist()
trackList = (data['trackName']).tolist()
msPlayedList = (data['msPlayed']).tolist()
#data.to_excel(f'{outputPath}/all_streaming_data.xlsx', index = False)
trackList = [i for i in trackList if i != 'Unknown Track']
artistList = [i for i in artistList if i != 'Unknown Artist']
print('Minutes Played:', round(sum(msPlayedList)/60000))
print('Top Spotify Data 9/17/2021 - 9/18/2022. Streams greater than 30 seconds.')
print('Top Artists 9/17/2021 - 9/18/2022')
print('Artist   Streams')

topArtists = []
for i in range (10):
	def most_frequent(artistList):
		return max(set(artistList), key = artistList.count)
	print(most_frequent(artistList), artistList.count(most_frequent(artistList)))
	topArtists.append(most_frequent(artistList))
	topArtist = topArtists[i]
	artistList = [i for i in artistList if i != topArtist]

print('Top Tracks 9/17/2021 - 9/18/2022')
print('Track   Streams')
topTracks = []
for i in range (10):
	def most_frequent(trackList):
		return max(set(trackList), key = trackList.count)
	print(most_frequent(trackList), trackList.count(most_frequent(trackList)))
	topTracks.append(most_frequent(trackList))
	topTrack = topTracks[i]
	trackList = [i for i in trackList if i != topTrack]