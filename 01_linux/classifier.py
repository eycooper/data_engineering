import naive_bayes as nb
import sys
import os

model = nb.NaiveBayesClassifier(k=0.5)
model.load_from_file()


def process_stdin(stream):
    
    # read from stdin 
    # expect filepath location
    #isFile = True
    files_to_score = [] 

    for line in stream:
        # check if its a fil
        # print(line)
        # print(os.path.isfile(line.rstrip()))
       # if os.path.isfile(line.rstrip()):
       files_to_score.append(line.rstrip())
       # else:
            # assuming it could be a directory
           # directory  = line.rstrip()
           # isFile = False

    # get files from location
   # files_to_score = []
    #if isFile:
    #files_to_score.append(file)
    #else:
        #for directory in directories: 
        #      files = []
       # for f in os.listdir(directory):
           # files_to_score.append(os.path.join(directory + f))
            #files.append(os.path.join(directory +  f))
            #files_to_score += files

    return files_to_score

def score_one_file(fname, model):
    try:
        sys.stderr.write(fname)
        subject = ""
        with open(fname, errors='ignore') as source:
            for line in source:
                if line.startswith("Subject:"):
                    subject = line.lstrip("Subject: ")
        
        score = model.predict(subject)
        formatted_return = "{}\t{}".format(str(score), fname)
        print(formatted_return)
    except Exception as e:
        sys.stderr.write("{}\tUncaught Exception:\t{}".format(fname, e))


files_to_score = process_stdin(sys.stdin)

for fname in files_to_score:
    score_one_file(fname, model)
