def solution(season, dayCount, initialPhase):
    # Apply shift to days so that initialPhase is first
    days = ["NewMoon", "Crescent", "Quarter", "Gibbous", "Full", 
            "Waning", "Eclipse", "Twilight"]

    ordered_days = days[days.index(initialPhase):] + days[:days.index(initialPhase)]
    print(ordered_days)
    
    seasons = {"January": 31, "February": 28, "March": 31, "April": 30, 
               "May": 31, "June": 30, "July": 31, "August": 31, 
               "September": 30, "October": 31, "November": 30, "December": 31}
    
    tDays = 0
    for k, v in seasons.items():
        if k == season:
            break
        tDays += v
        print(f"tDays: {tDays}")
    tDays += dayCount
    
    # Since each phase is 8 days and there are 8 phases that will be 64 days in total. 8 rows x 8 cols
    # Using modulo 8 will cycle through the array 8 times no matter which day its on so,
    # If we know the week we can use the modulus operator to tell which phase we are in.

    # week = (total days // # of days in a week)
    # phase index = week % # of len(phase array)
    phase = ordered_days[((tDays//8)%8)]

    print(f"total days: {tDays}, days modded by 8: {tDays%8}, weeks modded by 8: {(tDays//8)%8}")

    # for i in range(0, tDays, 8):
        # phase = ordered_days[i%8]
        # print(f"phase: {phase}, index: {i}, modulo: {i%8}")
    return phase

def main():
    """Description:
        Given the season, dayCount, and initialPhase return the correct phase.
        
        Provided:
            phases = ["NewMoon", "Crescent", "Quarter", "Gibbous", "Full", 
            "Waning", "Eclipse", "Twilight"]
    
            seasons = {"January": 31, "February": 28, "March": 31, "April": 30, 
                    "May": 31, "June": 30, "July": 31, "August": 31, 
                    "September": 30, "October": 31, "November": 30, "December": 31}
    
    """
    results = []
    
    """Test Case 1:
        args:
            solution("January", 1, "NewMoon")
        result:
            January 1st is the 1st day of the season which falls in the 
            "NewMoon" phase since the intialPhase is NewMoon.
        explanation:
            1 - 8 = "NewMoon"
    """
    case_one_output = solution("January", 1, "NewMoon")
    case_one_expected = "NewMoon"
    case_one_result = case_one_output == case_one_expected
    results.append(case_one_result)
    
    """Test Case 2:
        args:
            solution("February", 4, "Gibbous")
        result:
            February 4th is the 35th day which falls in the 
            "Twilight" phase since the intialPhase is Gibbous. 
        explanation:
            1 - 8 = "Gibbous" days
            9 - 16 = "Full"
            17 - 24 = "Waning"
            25 - 32 = "Eclipse"
            33 - 40 = "Twilight"
            41 - 48 = "NewMoon"
            49 - 56 = "Crescent"
            57 - 64 = "Quarter"
    """

    case_two_output = solution("February", 4, "Gibbous") #35th day = "Twilight"
    case_two_expected = "Twilight"
    case_two_result = case_two_output == case_two_expected
    results.append(case_two_result)
    
    """Test Case 3:
        args:
            solution("September", 14, "Gibbous")
        result:
            September 14th is the 257th day of year which falls in the 
            "Gibbous" phase since the intialPhase is Gibbous.
            Beginning of a phase, in days, + 64 will start you at the next iteration of the same phase.
        explanation:
            1 - 8, 65 - 72, 129 - 136, 193 - 200, 257 - 264, 321 - 328 = "Gibbous" days
            9 - 16 = "Full"
            17 - 24 = "Waning"
            25 - 32 = "Eclipse"
            33 - 40 = "Twilight"
    """

    case_three_output = solution("September", 14, "Gibbous") #257th day = "Gibbous"
    case_three_expected = "Gibbous"
    case_three_result = case_three_output == case_three_expected
    results.append(case_three_result)
    
    for i in range(len(results)):
        print(f"Test Case: {i+1} {'pass' if results[i] else 'false'}")
    
if __name__ == "__main__":
    main()
    