import utility
import CreateImageFeatures
import csv

def format_sql_request(headerFileName, imageDataFileName):
  with open(headerFileName, 'r') as headerFile:
    headerReader = csv.reader(headerFile)
    with open(imageDataFileName, 'r') as imageDataFile:
      imageDataReader = csv.reader(imageDataFile)
      for j in headerReader:
        header = j
      imageData = []
      
      imageDataHeader = imageDataReader.__next__()
      imageData.append(header)
      for row in imageDataReader:
        imageInfo = [0] * len(header)
        for i in range(len(row)):
          if imageDataHeader[i] in header:
            imageInfo[header.index(imageDataHeader[i])] = row[i]
        imageData.append(imageInfo)
      print(imageData)
      with open("sqlPair.csv", 'w', newline='') as pairoutput:
        writer = csv.writer(pairoutput)
        for row in imageData:
          writer.writerow(row)


utility.makeTestCSV('imgs')
CreateImageFeatures.write_test_to_csv('test_preprocess_output.csv', 'test_features.csv')
format_sql_request("header.csv", "test_features.csv")