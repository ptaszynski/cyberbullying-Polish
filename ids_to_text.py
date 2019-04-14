import sys
import json
import re
import math
import twitter



###### 1 - file with twitter tokens 
####   2 - file with tweet IDs
###    3 - output file

def make_list(in_file):
        IDlist=[]
        with open(in_file, 'r') as f:
                for line in f.readlines():
                        try:
                                IDlist.append(int(line.strip()))
                        except:
                                print("Problem with file with tweet IDs")
                                
        return IDlist



def load_tokens(path):
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            parts = [x.strip() for x in line.split(",")]
            (consumer_key, consumer_secret, auth_key, auth_secret) = parts
            tokens = dict()
            tokens["CLIENT_KEY"] = consumer_key
            tokens["CLIENT_SECRET"] = consumer_secret
            tokens["ATOKEN_KEY"] = auth_key
            tokens["ATOKEN_SECRET"] = auth_secret
            break  # assume first token line needed

        return tokens


def make_text(doc):
        text ="#NAME?"
        id = doc.id
        if doc.retweeted_status is not None:
                text=doc.retweeted_status.text
        elif doc.text is not None:
                text=doc.text        
        return (text, id)                

def get_tweets(api, IDlist):
        tweetDict={}
        stopper = math.ceil(len(IDlist)/20)
        for i in range(0, stopper):
                beg=(i*20)
                fin=((i*20)+20)
                statuses = api.GetStatuses(IDlist[beg:fin])
                for s in statuses:
                        text, id = make_text(s)
                        tweetDict[id] = text               
        return tweetDict

def write_tweets(outfile, IDlist, tweetDict):
        with open(outfile, 'w') as f:
                for x in IDlist:
                        if x in tweetDict.keys():
                                f.write(tweetDict[x] +"\n")
                        else:
                                f.write("#NAME?" +"\n")




def main():

    if ((len(sys.argv) < 4)):
            print("Wrong number of parameters. First argument is file with twitter tokens (you should have your developer account). Second argument shoud be input file with tweet IDs (one per line). Third is output file name.")
            sys.exit(1)    
    tokens = load_tokens(sys.argv[1])

    
    api = twitter.Api(
        consumer_key=tokens["CLIENT_KEY"],
        consumer_secret=tokens["CLIENT_SECRET"],
        access_token_key=tokens["ATOKEN_KEY"],
        access_token_secret=tokens["ATOKEN_SECRET"],
        sleep_on_rate_limit=True
    )
    l = make_list(sys.argv[2])
    
    k = get_tweets(api , l)
    write_tweets(sys.argv[3], l, k)
    

main()




