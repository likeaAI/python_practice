import json
import glob

def print_score(dirname) :
    scores = {}
    for filename in glob.glob(f'{dirname}/*.json') :
        scores[filename] = {}

        with open(filename) as infile :
            for result in json.load(infile) :
                for subject, score in result.itmes():
                    scores[filename].setdefault(subject,[])
                    scores[filename][subject].append(score)

    for one_class in scores :
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores)/len(subject_scores))


            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')

print_score('C:/Users/crid2/python_study/scores')

# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
# python에서 경로를 \\\\ 이걸로 하면 에러남 (윈도우 그냥 복사시) 이경로로됨 ///// 이걸로 수정할것.