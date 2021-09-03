import datetime

from num.hello import contains_y,jeff,first_letter_in,first_vowel_in,digit_sum,check_karma,check_master_number,get_effective

import collections
from collections import OrderedDict

x = datetime.datetime.now()
year_now = x.year
month_now = x.strftime("%m")
day_now = x.strftime("%d")

data = {}

def numerology_2(FN,MN,LN,btd1,btm1,bty1):
    ####################
    btd = int(btd1)
    btm = int(btm1)
    bty = int(bty1)
    
    
    
    if MN == '':
        name2 = contains_y(FN[len(FN)-1]).upper()
        name1 = contains_y(FN[:len(FN)-1]).upper()
    else:
        name2 = contains_y(MN).upper()
        name1 = contains_y(FN).upper()
        
    name3 = contains_y(LN).upper()
    
    k1=jeff(name1)
    sE=k1[0]
    vo=k1[1]
    co=k1[2]
    
    k2=jeff(name2) # k2[3] = vowels   k1[3] + k1[4] + k2[3] + k2[4] + k3[3] + k3[4]
    sE1=k2[0]
    vo1=k2[1]
    co1=k2[2]
    
    k3=jeff(name3)
    sE2=k3[0]
    vo2=k3[1]
    co2=k3[2]
    
    #modifiers['first_letter'] = first_letter_in(name1)
    #modifiers['first_vowel'] = first_vowel_in(name1)
    
    individual_expression_in_names = (sE+sE1+sE2)
    
    k_exp = individual_expression_in_names
    
    # check for karmic debt and put it in modifiers
    #modifiers[check_karma(k_exp,'expression')[0]] = check_karma(k_exp,'expression')[1] #'karmicDebt[13].inTheLifePath'
    
    #expression
    exp = check_master_number(k_exp)
    #print(exp)
    #exp_ = [k_exp,digit_sum(check_master_number(k_exp))] #
    
    ##########going for soul urge or heart desire number
    individual_vowels_in_names = (vo+vo1+vo2)
    
    k_sU = individual_vowels_in_names
    
    # check for karmic debt and put it in modifiers
    #modifiers[check_karma(k_sU,'soul_urge')[0]] = check_karma(k_sU,'soul_urge')[1]
    
    sU = digit_sum(individual_vowels_in_names)
    
    #sU_ = [k_sU,digit_sum(check_master_number(k_sU))]
    
    #Secret Self
    individual_imagenumber_in_names = (co+co1+co2) #secret self the consulnants in names
    secret_self  = digit_sum(individual_imagenumber_in_names)
    k_s_self = individual_imagenumber_in_names
    #s_self = digit_sum(secret_self)
    
    #modifiers['secret_self'] = [k_s_self,check_master_number(k_s_self)]
    
    #############Everything Numbers###################
    bd = [int(x) for x in str(btd)]
    bm = [int(x) for x in str(btm)]
    by = [int(x) for x in str(bty)]
    
    #print(sum(bd) + sum(bm) + sum(by))
    
    s = digit_sum(sum(bd)) + digit_sum(sum(bm)) + digit_sum(sum(by)) #list all numbers and sum
    
    #birthday
    k_bd = btd
    
    # check for karmic debt and put it in modifiers
    #modifiers[check_karma(k_bd,'birthday')[0]] = check_karma(k_bd,'birthday')[1]
    
    bd_ = [k_bd,check_master_number(k_bd)] 
    
    b_day = digit_sum(sum(bd))
    
    #Life Path
    k_lp = sum(bd) + sum(bm) + sum(by) #karma in life path
    
    # check for karmic debt and put it in modifiers
    #modifiers[check_karma(k_lp,'life_path')[0]] = check_karma(k_lp,'life_path')[1]
    
    lp = digit_sum(s)
    
    lp_ = [k_lp,digit_sum(check_master_number(k_lp))]
    
    #check for sub elements in life path
    def sub_element(which,core): 
        if core in [digit_sum(sum(bm)),digit_sum(sum(bd)),digit_sum(sum(by))]:
            data[f'sub_element_{len(data)-1}'] = f'{core}.{core}' ##aspects[8].pt_8;
        #else:
            #data[f'{core}_{which}_sub_element'] = 'NaN'
    
    #things current
    sum_bd = sum(bd)
    sum_bm = sum(bm)
    sum_by = digit_sum(sum(by))
    for_py = digit_sum(sum_bd + sum_bm)
    
    cy1 = digit_sum(digit_sum(year_now)) #current year
    
    #personal year number bd + bm + cy1
    py_num = digit_sum(digit_sum((sum_bd + sum_bm + cy1)))# personal year
    
    #Your Life Path - Expression Bridge
    #LEB = abs(birth_force - exp)
    
    k_Mrity = exp + lp
    reality_number = digit_sum(exp + lp)
    #Mrity = reality_number
    
    #modifiers['maturity_number'] = [k_Mrity,digit_sum(k_Mrity)]
    
    #---------------------------------------------#
    #first_name = list(name1)
    
    #Growth number
    grow_n = [sum(digit_sum(ord(char.lower())-96) for char in name1 if char.lower() in name1.lower())][0]
    #modifiers['growth_number'] = [grow_n,check_master_number(k_lp)]
    
    list_name = list(name1 + name2 + name3)
    join_all_apha_in_name = ''.join(list_name)
    #print(join_all_apha_in_name)
    
    convert_alpha_in_name_to_number = [ord(char.lower())-96 for char in join_all_apha_in_name if char.lower()
                                   in join_all_apha_in_name.lower()]
    
    new_convert_alpha_in_name_to_number = [] #[5, 4, 5, 2, 1, 3, 3, 8, 3, 8, 3, 2, 5, 3, 6, 2, 5, 3]
    for i in convert_alpha_in_name_to_number:
        summed = digit_sum(i)
        new_convert_alpha_in_name_to_number.append(summed)
    
    freq = collections.Counter(new_convert_alpha_in_name_to_number)# Counter({3: 6, 5: 4, 2: 3, 8: 2, 4: 1, 1: 1, 6: 1})
    
    physical = []
    mental = []
    emotional = []
    intuitive = []
    
    for i in list_name:
        if i in ['D','E','M','W']:
            physical.append(i)
        elif i in ['A','G','H','J','L','N','P']:
            mental.append(i)
        elif i in ['B','I','O','R','S','T','X','Z']:
            emotional.append(i)
        elif i in ['C','F','K','Q','U','V','Y']:
            intuitive.append(i)
    
    def compare_temperament(tempt):
        if tempt in [3,4,5]:
            return 'Average'
        elif tempt >= 6:
            return 'Strong'
        elif tempt in [0,1,2]:
            return 'Weak'
        
    phy = compare_temperament(len(physical))
    men = compare_temperament(len(mental))
    emo = compare_temperament(len(emotional))
    intt = compare_temperament(len(intuitive))
    
    #point of security
    #point_of_security = digit_sum(digit_sum(physical + mental + emotional + intuitive))
    #ps = point_of_security
    
    #specialized trait and point of intensification
    how_many_one = freq[1] #1 [3]
    how_many_two = freq[2] #3 [1]
    how_many_three = freq[3] #6 [1 or 2]
    how_many_four = freq[4] #1 [1]
    how_many_five = freq[5] #5 [3 or 4 or 5]
    how_many_six = freq[6] #1 [1 or 2]
    how_many_seven = freq[7] # 0 [0 or 1]
    how_many_eight = freq[8] # 2 [1]
    how_many_nine = freq[9] #0 [3]
    
    one = how_many_one
    two = how_many_two
    thr = how_many_three 
    fou = how_many_four
    fiv = how_many_five
    six = how_many_six
    sev = how_many_seven
    eig = how_many_eight
    nin = how_many_nine
           
    #int_pts = {'n1':one,'n2':two,'n3':thr,'n4':fou,'n5':fiv,'n6':six,'n7':sev,'n8':eig,'n9':nin}
    #print('int_pts = ',int_pts)
    
    #which number is the max for intensity point
    def get_key(val):
        for key, value in freq.items():
            if val == value:
                return key
        return "key doesn't exist"
    int_pt = get_key(max(one,two,thr,fou,fiv,six,sev,eig,nin))
    
    #modifiers['intensity_point'] = int_pt
    #modifiers['prime_intensifier'] = int_pt
    
    
    #missing numbers in name
    exp_list = k1[3] + k1[4] + k2[3] + k2[4] + k3[3] + k3[4] #[5, 5, 1, 0, 4, 2, 3, 5, 3, 3, 0, 3, 8, 3, 8, 2, 5, 6, 3, 0, 2, 5]
    gen_list = [1,2,3,4,5,6,7,8,9]
    s1 = set(exp_list) #{0, 1, 2, 3, 4, 5, 6, 8}
    cha = [x for x in gen_list if x not in s1]
    #print('cha = ',cha)
    
    #
    data['lifePath'] = k_lp
    data['birthday'] = k_bd
    data[f'effectiveness_of_lifepath_expression_{len(data)-1}'] = get_effective(k_lp,k_exp) #eff = get_effectiveness(core1,core2)
    data['expression'] = k_exp
    data[f'effectiveness_of_lifepath_soulUrge_{len(data)-1}'] = get_effective(k_lp,k_sU)
    data['SoulUrge'] = k_sU #
    data[f'effectiveness_of_exp_soulUrge_{len(data)-1}'] = get_effective(k_exp,k_sU)
    
    if check_karma(k_exp,'expression')[1] != 'NaN':
        data[check_karma(k_exp,'expression')[0]] = check_karma(k_exp,'expression')[1] #'karmicDebt[13].inTheLifePath'
    
    if check_karma(k_sU,'soul_urge')[1] != 'NaN':
        data[check_karma(k_sU,'soul_urge')[0]] = check_karma(k_sU,'soul_urge')[1]
    
    if check_karma(k_bd,'birthday')[1] != 'NaN':
        data[check_karma(k_bd,'birthday')[0]] = check_karma(k_bd,'birthday')[1]
    
    if check_karma(k_lp,'life_path')[1] != 'NaN':
        data[check_karma(k_lp,'life_path')[0]] = check_karma(k_lp,'life_path')[1]    
        
    data['secret_self'] = k_s_self
    
    sub_element('lp',lp) #8
    sub_element('exp',exp) #6
    sub_element('b_day',b_day) #4
    sub_element('sU',sU) #1
    
    data['maturity_number'] = k_Mrity
    
    data['prime_intensifier'] = int_pt
    
    for number in cha:
        if number in [lp,sU,exp,b_day]:
            data[f'modified_karmic_lesson_{number}'] = number
        elif f'modified_karmic_lesson_{number}' not in data:
            data[f'karmic_lesson_{number}'] = number
    
    def count_number(number,number_value,number_list):
        if number > number_list[-1]: #2_lessthan_average": 0,
            data[f'morethan_average_{number}'] = number_value
        elif number < number_list[0] and number_list == 0 and f'karmic_lesson_{number_value}' and f'modified_karmic_lesson_{number_value}' not in data:
            data[f'lessthan_average_{number}'] = number_value #1
    
    one_ = [3]
    two_ = [1]
    thr_ = [1,2] 
    fou_ = [1]
    fiv_ = [3,4,5]
    six_ = [1,2]
    sev_ = [0,1]
    eig_ = [1]
    nin_ = [3]
    
    count_number(one,1,one_)
    count_number(two,2,two_)
    count_number(thr,3,thr_)
    count_number(fou,4,fou_)
    count_number(fiv,5,fiv_)
    count_number(six,6,six_)
    count_number(sev,7,sev_)
    count_number(eig,8,eig_)
    count_number(nin,9,nin_)
    
    #challenges
    first_challenge = abs((digit_sum(sum(bm))) - (digit_sum(sum(bd))))
    second_challenge = abs((digit_sum(sum(bd))) - (digit_sum(sum(by))))
    third_challenge = abs(first_challenge - second_challenge)
    fourth_challenge = abs((digit_sum(sum(bm))) - (digit_sum(sum(by))))
    cH = first_challenge
    cH1 = second_challenge
    cH2 = third_challenge
    cH3 = fourth_challenge
    
    #get the challenge
    data['challenge'] = cH3
    
    data['physical'] = phy
    data['mental'] = men
    data['emotional'] = emo
    data['intuitive'] = intt
    
    data['first_letter'] = first_letter_in(name1)
    data['first_vowel'] = first_vowel_in(name1)     
        
    
    return data


