import pandas as pd
import random
import pickle
import numpy as np

doctor_name_list = '''Dr. Samantha Taylor
Dr. Adam Patel
Dr. Jessica Nguyen
Dr. Brian Lee
Dr. Allison Rodriguez
Dr. Daniel Smith
Dr. Sarah Thompson
Dr. Anthony Davis
Dr. Emily Kim
Dr. Michael Wilson
Dr. Julia Chang
Dr. Andrew Jackson
Dr. Christine Chen
Dr. Benjamin King   
Dr. Rachel Lee
Dr. Christopher Miller
Dr. Lisa Kim
Dr. Jonathan Jones
Dr. Laura Martinez
Dr. Matthew Johnson
Dr. Rebecca Davis
Dr. David Brown
Dr. Vanessa Hernandez
Dr. Joshua Garcia
Dr. Elizabeth Taylor
Dr. Kevin Kim
Dr. Ashley Lee
Dr. Nicholas Wilson
Dr. Jasmine Nguyen
Dr. Steven Smith
Dr. Michelle Lee
Dr. Jeremy Patel
Dr. Lauren Brown
Dr. Justin Miller
Dr. Samantha Johnson
Dr. Christopher Davis
Dr. Alexandra Kim
Dr. Eric Wilson
Dr. Sophia Chen
Dr. Alexander Lee
Dr. Gabriella Rodriguez
Dr. Caleb Jones
Dr. Sarah Thompson
Dr. Ryan Davis
Dr. Grace Lee
Dr. Christopher Kim
Dr. Victoria Smith
Dr. Samuel Patel
Dr. Isabella Davis
Dr. Andrew Johnson
Dr. Lauren Brown
Dr. Michael Wilson
Dr. Katherine Kim
Dr. Matthew Lee
Dr. Maria Hernandez
Dr. Ethan Nguyen
Dr. Samantha Taylor
Dr. William Brown
Dr. Nicole Kim
Dr. James Davis
Dr. Rachel Lee
Dr. Daniel Smith
Dr. Ava Garcia
Dr. Anthony Davis
Dr. Sophia Chen
Dr. Benjamin King
Dr. Alexandra Kim
Dr. Alexander Lee
Dr. Christopher Davis
Dr. Emily Kim
Dr. John Wilson
Dr. Vanessa Hernandez
Dr. Daniel Johnson
Dr. Elizabeth Taylor
Dr. Brian Lee
Dr. Julia Chang
Dr. Ryan Davis
Dr. Jennifer Kim
Dr. Kevin Smith
Dr. Gabriella Rodriguez
Dr. Samuel Patel
Dr. Christina Nguyen
Dr. Lauren Brown
Dr. Andrew Jackson
Dr. Maria Hernandez
Dr. Jonathan Jones
Dr. Ava Garcia
Dr. Sophia Chen
Dr. James Davis
Dr. Rachel Lee
Dr. Alexander Lee
Dr. Isabella Davis
Dr. Matthew Johnson
Dr. Sarah Thompson
Dr. Caleb Jones
Dr. Katherine Kim
Dr. Christopher Kim
Dr. Victoria Smith
Dr. Eric Wilson
Dr. Vanessa Hernandez'''.split('\n')

doctor_df = pd.DataFrame(columns=['name', 'int', 'area'])
doctor_df['name'] = doctor_name_list

area = ['piplod', 'vesu', 'pal', 'adajan', 'bhatar', 'ghod dod road', 'katargam', 'udhna', 'khajod', 'kamrej']

int_choice = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J']

for i in range(len(doctor_df)):
    doctor_df['area'][i] = random.choice(area)
    doctor_df['int'][i] = random.choice(int_choice)

new_pt = pickle.load(open(r"D:\VIT\Hackathons\SVNIT - DotSlash 6.0\Doctor recommendation system\new_pt.pkl", 'rb'))
new_pt.index = doctor_df['name'][:50]
new_similarity_scores = pickle.load(open(r"D:\VIT\Hackathons\SVNIT - DotSlash 6.0\Doctor recommendation system\new_similarity_scores", 'rb'))


def recommend(int, area):
    doctor_df[['int', 'area']] == (int, area)
    groups = doctor_df.groupby(['int'])
    result = groups.get_group(int)
    result.reset_index()
    return result

# x = recommend('D', 'piplod')
# # print(' '.join([str(elem) for elem in x[2:3]]))
# print(x['name'][1:2])

if __name__ == "__main__":
    recommend()
        