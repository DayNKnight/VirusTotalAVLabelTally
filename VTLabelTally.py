from tqdm import tqdm 
import json
import requests

def main(inputFile,fromSave):
    # Read all the hashes from the input file if we are not loading from the save file
    if not fromSave:
        with open(inputFile,'r') as file:
            hashes = file.readlines()
        
        # Strip the newline characters from the string
        for _hash in range(len(hashes)):
            hashes[_hash] = hashes[_hash].strip()

        # Deduplicate the hash list
        hashes = list(set(hashes))
        
        hashDictionary = {}
        for _hash in tqdm(range(len(hashes))):
            _hash = hashes[_hash]
            resp = requests.get(url.format(id=_hash), headers=params)
            respJson = resp.json()
            try:
                hashDictionary[_hash] = respJson["data"]
            except:
                print("Caught exception while trying to download the hash data")
                print(f"Stopped on hash {_hash}")
                print(f"Data in the response is \n{respJson}")
                print("*********************\n\nIf the hash is not in VT, I am reccomending that you delete the hash from the list.")
                print("Continuing with the requests")
                continue
        
        fp = open("Outfile.json",'w')
        json.dump(hashDictionary,fp,indent=4)
        fp.close() 
    else:
        fp = open("Outfile.json",'r')
        hashDictionary = json.load(fp)
        fp.close() 

    # Create the dictionary that is going to hold the tally for each company
    nameTally = {}

    keys = list(hashDictionary.keys())
    for key in tqdm(range(len(keys))):
        key = keys[key]
        sampleResults = hashDictionary[key]
        analysisResults = sampleResults["attributes"]["last_analysis_results"]

        for company in list(analysisResults.keys()):
            # Create the company listing in the name tally list if it is not there
            if company not in nameTally:
                nameTally[company] = {}

            # Check to see if the company in name tally has an undetected section
            if analysisResults[company]["category"] == "undetected":
                # If it doesnt, create one with a starting value of 1, else increment the value by 1
                if "undetected" not in nameTally[company]:
                    nameTally[company]["undetected"] = 1
                else:
                    nameTally[company]["undetected"] += 1
            else:
                # Same thing for if it is not undetected
                result = analysisResults[company]["result"]
                if result not in nameTally[company]:
                    nameTally[company][result] = 1
                else:
                    nameTally[company][result] += 1
            
    # This is going to output the results of the program to an output file in the format specified
    # fp = open("Results.txt",'w')
    # json.dump(nameTally,fp,indent=4)
    # fp.close()

    with open("Results.txt",'w') as file:
        keys = list(nameTally.keys())
        for company in keys:
            file.write(f"{company}\n")
            for detectionName in list(nameTally[company].keys()):
                file.write(f"\t{detectionName} : {nameTally[company][detectionName]}\n")
            file.write("\n")
if __name__ == "__main__":
    fp = open("key.txt",'r')
    API_KEY = fp.readline().strip()
    fp.close()

    url = 'https://www.virustotal.com/api/v3/files/{id}'
    params = {'x-Apikey': API_KEY}
    main("inFile.txt",False)