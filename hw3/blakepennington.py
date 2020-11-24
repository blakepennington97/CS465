def check_pair(result, hand):
    temp_list = []
    index_to_keep = 0
    j = 0
    found = False

    # grab only card numbers, not suites
    for i in hand:
        temp_list.append(i[0]) 
    
    # now check for pairs, if found update that index to True (keep it!)
    for i in temp_list:
        if temp_list.count(i) == 2:
            #print "pair exists!"
            found = True
            index_to_keep = j
            result[index_to_keep] = False
        j+=1

    return result, found


def check_trips(result, hand):
    temp_list = []
    index_to_keep = 0
    j = 0
    found = False

    # grab only card numbers, not suites
    for i in hand:
        temp_list.append(i[0]) 
    
    # now check for trips, if found update that index to True (keep it!)
    for i in temp_list:
        if temp_list.count(i) == 3:
            #print "trip exists!"
            found = True
            index_to_keep = j
            result[index_to_keep] = False
        j+=1

    return result, found


def check_two_pairs(result, hand):
    temp_list = []
    index_to_keep = 0
    j = 0
    count = 0
    found = False

    # grab only card numbers, not suites
    for i in hand:
        temp_list.append(i[0]) 
    
    # now check for pairs, if found update that index to True (keep it!)
    for i in temp_list:
        if temp_list.count(i) == 2:
            index_to_keep = j
            result[index_to_keep] = False
            count+=1
        j+=1
    
    if (count == 4):
        found = True
        #print "two pairs exists"

    return result, found


def check_flush_draw(result, hand):
    temp_list = []
    index_to_keep = 0
    j = 0
    found = False

    # grab only suites, not card numbers
    for i in hand:
        temp_list.append(i[1]) 
    
    # now check for flush, if found update that index to True (keep it!)
    for i in temp_list:
        if temp_list.count(i) == 4:
            #print "flush draw exists!"
            found = True
            index_to_keep = j
            ##print(index_to_keep)
            result[index_to_keep] = False
        j+=1

    return result, found


def check_straight_draw(result, hand):
    temp_list = []
    index_to_keep = 0
    j = 0
    found = False

    # init temp_list
    for i in range(15):
        temp_list.append((-1, -2))

    # grab rank values and place in temp list accordingly with associated original index values
    for i in hand:
        if i[0] == 'A':
            temp_list[1] = (i[0], j)
            temp_list[14] = (i[0], j)
        elif i[0] == 'T':
            temp_list[10] = (i[0], j)
        elif i[0] == 'J':
            temp_list[11] = (i[0], j)
        elif i[0] == 'Q':
            temp_list[12] = (i[0], j)
        elif i[0] == 'K':
            temp_list[13] = (i[0], j)
        else:
            temp_list[int(i[0])] = (i[0], j)
        j+=1
    
    count = 0
    is_straight_draw = False

    # determine if hand is straight draw
    for i in range(len(temp_list)):
        if temp_list[i][0] == -1:
            if count == 3:
                if (i+1 < len(temp_list) - 1) and temp_list[i+1][0] != -1:
                    is_straight_draw = True
                    break
                else:
                    count = 0
            elif count == 2:
                if (i+2 <= len(temp_list)) and (i+3 <= len(temp_list)) and temp_list[i+1][0] != -1 and temp_list[i+2][0] != -1:
                    is_straight_draw = True
                    break
                else:
                    temp_list[i-1] = (-1, -1)
                    count = 0
            else:
                count = 0
                if (i > 0):
                    temp_list[i-1] = (-1, -1)
        elif temp_list[i][0] != -1:
            count+=1

        if count == 4:
            is_straight_draw = True
            break
    
    # set list of cards to keep in straight draw
    if (is_straight_draw):
        #print "straight draw exists!"
        found = True
        for i in temp_list:
            if i[1] != -1:
                result[i[1]] = False

    return result, found


def keep_high_rank_cards(result, hand):
    index_to_keep = 0
    match = True
    #print "garbage hand"
    temp = False

    for i in hand:
        if i[0] == 'J' or 'Q' or 'K' or 'A' and temp == False:
            result[index_to_keep] = True
            temp = True
        index_to_keep+=1

    return result, match


def check_flush(result, hand):
    match = False
    suits = [i[1] for i in hand]

    if len(set(suits)) == 1:
        match = True
        #print "flush exists!"
        result = [False, False, False, False, False]
    
    return result, match


def check_straight(result, hand):
    temp_list = []
    index_to_keep = 0
    j = 0
    found = False

    # init temp_list
    for i in range(15):
        temp_list.append((-1, -2))
    
    # grab rank values and place in temp list accordingly with associated original index values
    for i in hand:
        if i[0] == 'A':
            temp_list[1] = (i[0], j)
            temp_list[14] = (i[0], j)
        elif i[0] == 'T':
            temp_list[10] = (i[0], j)
        elif i[0] == 'J':
            temp_list[11] = (i[0], j)
        elif i[0] == 'Q':
            temp_list[12] = (i[0], j)
        elif i[0] == 'K':
            temp_list[13] = (i[0], j)
        else:
            temp_list[int(i[0])] = (i[0], j)
        j+=1
    
    count = 0
    is_straight = False

    # determine if hand is straight
    for i in range(len(temp_list)):
        if temp_list[i][0] == -1:
            count = 0
            if (i > 0):
                temp_list[i-1] = (-1, -1)
        elif temp_list[i][0] != -1:
            count+=1

        if count == 5:
            is_straight = True
            break
    
    # set list of cards to keep in straight draw
    if (is_straight):
        #print "straight exists!"
        found = True
        for i in temp_list:
            if i[1] != -1:
                result[i[1]] = False

    return result, found


def check_straight_flush(result, hand):
    found = False
    result, found1 = check_flush(result, hand)
    result, found2 = check_straight(result, hand)

    if (found1 and found2):
        #print "straight flush exists!"
        found = True
    
    return result, found


def check_royal_flush(result, hand):
    found = False
    ranks = sorted(hand)
    result, found = check_straight_flush(result, hand)

    if (found and ranks[0][0] == 'A' and ranks[4][0] == 'T'):
        found = True
        #print 'royal flush exists!'


    return result, found


def check_four_of_a_kind(result, hand):
    found = False
    temp_list = []
    index_to_keep = 0
    j = 0

    # grab only card numbers, not suites
    for i in hand:
        temp_list.append(i[0]) 
    
    # now check for four of a kind, if found update that index to True (keep it!)
    for i in temp_list:
        if temp_list.count(i) == 4:
            #print "four of a kind exists!"
            found = True
            index_to_keep = j
            result[index_to_keep] = False
        j+=1

    return result, found


def check_full_house(result, hand):
    found = False
    result, found1 = check_pair(result, hand)
    result, found2 = check_trips(result, hand)

    if (found1 and found2):
        #print "full house exists!"
        found = True
    
    return result, found


class blakepennington:
    student_Name = ""
    student_Hand = []
    # Student function uses student Hand and return a boolean list to exchange cards
    # The Draw
    #     Our draw decision is really based around the following. We'd rather make an above average strength hand frequently than a super-strong hand rarely.
    #         If we have a pair we draw 3 and try and make trips.
    #         If we have trips, we draw two and try to make Quads or a full house. 
    #         If we have a flush-draw or straight-draw we draw one and try to hit.
    #         If we have total garbage (usually in a free play situation) we can hold on to cards above a Queen or Jack and replace the others.
    def student_function(self):
        result = [True, True, True, True, True]
        hand= self.student_Hand
        match = False

        # check hand to determine which cards to discard
        if (not match):
            result, match = check_royal_flush(result, hand)
        if (not match):
            result, match = check_straight_flush(result, hand)
        if (not match):
            result, match = check_four_of_a_kind(result, hand)
        if (not match):
            result, match = check_full_house(result, hand)
        if (not match):
            result, match = check_flush(result, hand)
        if (not match):
            result, match = check_straight(result, hand)
        if (not match):
            result, match = check_flush_draw(result, hand)
        if (not match):
            result, match = check_straight_draw(result, hand)
        if (not match):
            result, match = check_trips(result, hand)
        if (not match):
            result, match = check_pair(result, hand)
        if (not match):
            result, match = keep_high_rank_cards(result, hand)

        return result