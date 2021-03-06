# Body characteristics
#
# Ladybug: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# 
# This file is part of Ladybug.
# 
# Copyright (c) 2013-2015, Djordje Spasic <djordjedspasic@gmail.com> 
# Ladybug is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published 
# by the Free Software Foundation; either version 3 of the License, 
# or (at your option) any later version. 
# 
# Ladybug is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Use this component to calculate the Basal Metabolic Rate, Body Mass Index indices and to create the "bodyCharacterstics_" input for the "Thermal comfort indices" component.
-
Basal Metabolic Rate formula by Mifflin-St. Jeor. Body Mass Index formula by Adolphe Quetelet.
-
Formulas from: "Comparison of predictive equations for resting Metabolic rate in healthy nonobese and obese adults: a systematic review",
Frankenfield, Roth-Yousey, Compher, American Dietetic Association, 2005.:
https://www.andeal.org/files/Docs/Frankenfield_et_al_2005%5B1%5D.pdf
-
Provided by Ladybug 0.0.61
    
    input:
        age_: An age of the person in years.
              -
              If not supplied, default value of 35 will be used.
        gender_: Person's gender.
                 -
                 1 or "male"
                 2 or "female".
                 -
                 If not supplied, "male" will be used as a default value.
        height_: Person's height in centimetres.
                 -
                 If not supplied default value of 175 cm will be used.
        weight_: Person's weight in kilograms.
                 -
                 If not supplied default value of 75 kg will be used.
        bodyPosition_: Position of person's body.
                      -
                      1 or "sitting" for sitting position.
                      2 or "standing" for standing position.
                      3 or "crouching" for crouching position.
                      -
                      If not supplied, 2 (standing) will be used as a default value.
        clothingInsulation_: Clothing insulation of a person in "clo" units.
                   It ranges from 0 (nude person) to 4 (polar outfit).
                   Overall clo value can be determined by adding individual clo values for each type of cloths, based on a clo values table ( http://www.engineeringtoolbox.com/clo-clothing-thermal-insulation-d_732.html )
                   A more simplified approch would be:
                   -
                   0.20 - Very light summer cloths (shorts/skirt, t-shirt, slippers, no socks)
                   0.55 - Summer cloths (light trousers, short sleeves or blouse)
                   1 - Street-business suit or Typical indoor winter clothing
                   1.5 - Suit and cotton coat
                   2 - Winter suit and coat
                   4 - Heavy polar outfit (fur pants, coat, hood, gloves...)
                   -
                   If not supplied it will be caclulated for each hour based on air temperature, with minimal 0.6 and maximal 4 clo values.
        acclimated_: Determine whether the test person had previously experienced heat/cold stress.
                     -
                     "acclimated" or True if person in subject is acclimatized,
                     "unacclimated" or False if it's not.
                     -
                     If no value is supplied, False (unacclimated) will be used by default.
        metabolicRate_: Activity's metabolic rate in mets. If not supplied 2.32 will be used as default value
                        Here are some of the examples of metabolic rates mets based on activity:
                        Activity - met
                        -------------------
                        Reclining  - 0.8
                        Seating - 1.0
                        Car driving - 1.2
                        Sedentary activity (office, dwelling, school, laboratory) - 1.2
                        Standing - 1.2
                        Standing (light activity: shopping, laboratory, light industry) - 1.6
                        Standing (medium activity: shop assistant, domestic work) - 2.0
                        Walking (4 km/h) - 2.32
                        Walking (5 km/h) - 3.4
                        ...
                        Washing dishes standing - 2.5
                        Domestic work (raking leaves on the lawn) - 2.9
                        Domestic work (washing by hand and ironing) - 2.9
                        Iron and steel (ramming the mould with a pneumatic hammer) - 3.0
                        Building industry (brick laying) - 2.2
                        Building industry (forming the mould) - 3.1
                        Building industry (loading a wheelbarrow with stones and mortar) - 4.7
                        Forestry (cutting with chainsaw) - 3.5
                        Forestry (working with an axe) - 8.5
                        Agriculture (digging with a spade) - 6.5
                        ...
                        Volleyball - 4.0
                        Golf - 5.0
                        Softball - 5.0
                        Gymnastics - 5.5
                        Aerobic Dancing - 6.0
                        Swimming - 6.0
                        Ice skating - 6.2
                        Bicycling (15 km/h) - 4.0
                        Bicycling (20km/h) - 6.2
                        Skiing (9 km/h) - 7.0
                        Backpacking - 7.0
                        Basketball - 7.0
                        Handball - 8.0
                        Hockey - 8.0
                        Racquetball - 8.0
                        Soccer - 8.0
                        Running (8 km/h) - 8.5
                        Running (15km/h) - 9.5
                        -
                        If not supplied default value of 2.32 (walking 4 km/h or 1.1m/s) mets will be used.
        activityDuration_: Duration of the activity sequence in minutes.
                           -
                           If not supplied, default value of 480 minutes (8 hours) will be used.
    output:
        readMe!: ...
        BMI: Body Mass Index - is the ratio of the persons weight to square of height. It is generally used as a method of screening for weight category.
             In kg/m2.
        BMILevel: Level of BMI for adult (18 years and older) males and females:
                     ----------------
                     - for males:
                     BMI < 17.5 - Anorexia
                     17.5 < BMI < 20.7 - Underweight
                     20.7 < BMI < 26.4 - Normal weight
                     26.4 < BMI < 27.8 - Marginally overweight
                     27.8 < BMI < 31.1 - Overweight
                     31.1 < BMI < 40 - Obese
                     BMI > 40 - Extreme obesity
                     -
                     - for females:
                     BMI < 17.5 - Anorexia
                     17.5 < BMI < 19.1 - Underweight
                     19.1 < BMI < 25.8 - Normal weight
                     25.8 < BMI < 27.3 - Marginally overweight
                     27.3 < BMI < 32.3 - Overweight
                     32.3< BMI < 40 - Obese
                     BMI > 40 - Extreme obesity
                     -
                     In calories/day.
        BMR: Basal Metabolic Rate - represents the minimum daily amount of energy needed to keep your body functioning, including breathing and keeping your heart beating, without lossing weight. It does not include the the calories you burn from normal daily activities or exercise.
             To account for daily activities and exercises, this BMR value needs to be multiplied with:
             -
             1.2 - Light or no exercise and desk job
             1.375 - Light exercise or sports 1-3 days a week
             1.55 - Moderate exercise or sports 3-5 days a week
             1.725 - Hard exercise or sports 6-7 days a week
             1.9 - Hard daily exercise or sports and physical job
             -
             Once the person knows the number of daily calories needed to maintain its weight, it can easily calculate the number of calories it needs to eat in order to gain or lose weight.
             In calories/day.
        bodyCharacteristics: A list of inputted values (age, gender, height, weight, bodyPosition, clothingInsulation, acclimated, metabolicRate, activityDuration).
                             -
                             Use it for the "Thermal comfort indices" component's "bodyCharacteristics_" input.
"""

ghenv.Component.Name = "Ladybug_Body Characteristics"
ghenv.Component.NickName = "BodyCharacteristics"
ghenv.Component.Message = 'VER 0.0.61\nNOV_05_2015'
ghenv.Component.Category = "Ladybug"
ghenv.Component.SubCategory = "6 | WIP"
#compatibleLBVersion = VER 0.0.59\nNOV_05_2015
try: ghenv.Component.AdditionalHelpFromDocStrings = "1"
except: pass

import Grasshopper.Kernel as gh
import scriptcontext as sc


def main(age, gender, height, weight, bodyPosition, clothingInsulation, acclimated, metabolicRate, activityDuration):
    try:
        if (age == None) or (age <= 0):
            age = 35  # in years
        
        if (gender == None):
            gender = "male"  # default
        else:
            try:
                if (gender.lower() == "male"):
                    gender = "male"
                elif (gender.lower() == "female"):
                    gender = "female"
                else:
                    raise
            except Exception,e:
                try:
                    if (int(gender) == 1):
                        gender = "male"
                    elif (int(gender) == 2):
                        gender = "female"
                    else:
                        raise
                except Exception,e:
                    bodyCharacteristics = []
                    BMR = BMI = BMILevel = None
                    validInputData = False
                    printMsg = "Something is wrong with your \"gender_\" input data. Please hover over this input to check the types of the data it supports."
                    
                    return BMR, BMI, BMILevel, bodyCharacteristics, validInputData, printMsg
        
        if (height == None) or (height <= 0):
            heightCM = 175  # in centimeters
            heightM = 1.75  # in meters
        else:
            heightCM = height  # in centimeters
            heightM = heightCM/100  # in meters
        
        if (weight == None) or (weight <= 0):
            weight = 75  # in kilograms
        
        if (bodyPosition == None):
            bodyPosition = "standing"  # default
        else:
            try:
                if (bodyPosition.lower() == "sitting"):
                    bodyPosition = "sitting"
                elif (bodyPosition.lower() == "standing"):
                    bodyPosition = "standing"
                elif (bodyPosition.lower() == "crouching"):
                    bodyPosition = "crouching"
                else:
                    raise
            except Exception,e:
                try:
                    if (int(bodyPosition) == 1):
                        bodyPosition = "sitting"
                    elif (int(bodyPosition) == 2):
                        bodyPosition = "standing"
                    elif (int(bodyPosition) == 3):
                        bodyPosition = "crouching"
                    else:
                        raise
                except Exception,e:
                    bodyCharacteristics = []
                    BMR = BMI = BMILevel = None
                    validInputData = False
                    printMsg = "Something is wrong with your \"bodyPosition_\" input data. Please hover over this input to check the types of the data it supports."
                    
                    return BMR, BMI, BMILevel, bodyCharacteristics, validInputData, printMsg
        
        if (clothingInsulation == None):# or (clothingInsulation <= 0):
            clothingInsulation = None
        
        if (acclimated == None):
            acclimated = "unacclimated"  # default
        else:
            try:
                if (acclimated.lower() == "unacclimated"):
                    acclimated = "unacclimated"
                elif (acclimated.lower() == "acclimated"):
                    acclimated = "acclimated"
                else:
                    raise
            except Exception,e:
                try:
                    if (int(acclimated) == 0):
                        acclimated = "unacclimated"
                    elif (int(acclimated) == 1):
                        acclimated = "acclimated"
                    else:
                        raise
                except Exception,e:
                    bodyCharacteristics = []
                    BMR = BMI = BMILevel = None
                    validInputData = False
                    printMsg = "Something is wrong with your \"acclimated_\" input data. Please hover over this input to check the types of the data it supports."
                    
                    return BMR, BMI, BMILevel, bodyCharacteristics, validInputData, printMsg
        
        if (metabolicRate == None) and (metabolicRate <= 0):
            metabolicRate = 2.32  # default value 2.32 mets = 135 W/m2
        
        if (activityDuration == None) and (activityDuration <= 0):
            activityDuration = 480  # default, in minutes
    
    except Exception, e:
        bodyCharacteristics = []
        BMR = BMI = BMILevel = None
        validInputData = False
        printMsg = "Something is wrong with your input data. Please hover over the inputs to check the type of the data that each one of them requires."
        
        return BMR, BMI, BMILevel, bodyCharacteristics, validInputData, printMsg
    
    
    # BMR
    if (gender == "male"):
        BMR = 9.99 * weight + 6.25 * heightCM - 4.92 * age + 5  # in calories/day (formula by Mifflin-St. Jeor)
        #BMR = 66.47 + (13.75*weight) + (5*heightCM) - (6.75*age)  # in calories/day  (formula by Harris Benedict)
        #BMR = 879 + 10.2*weight  # in calories/day  (formula by Owen)
    elif (gender == "female"):
        BMR = 9.99 * weight + 6.25 * heightCM - 5 * age - 161  # in calories/day (formula by Mifflin-St. Jeor)
        #BMR = 655.09 + (9.56*weight) + (1.84*heightCM) - (4.67*age)  # in calories/day  (formula by Harris Benedict)
        #BMR = 795 + 7.18*weight  # in calories/day  (formula by Owen)
    
    
    # BMI formula by Adolphe Quetelet:
    BMI = weight/((heightM)**2)  # kg/m2
    
    # BMI categories by NHANES II survey
    if (gender == "male"):
        if (BMI < 17.5):
            BMILevel = "Anorexia"
        elif (BMI >= 17.5) and (BMI < 20.7):
            BMILevel = "Underweight"
        elif (BMI >= 20.7) and (BMI < 26.4):
            BMILevel = "Normal weight"
        elif (BMI >= 26.4) and (BMI < 27.8):
            BMILevel = "Marginally overweight"
        elif (BMI >= 27.8) and (BMI < 31.1):
            BMILevel = "Overweight"
        elif (BMI >= 31.1) and (BMI < 40):
            BMILevel = "Obese"
        elif (BMI >= 40):
            BMILevel = "Extreme obesity"
    elif (gender == "female"):
        if (BMI < 17.5):
            BMILevel = "Anorexia"
        elif (BMI >= 17.5) and (BMI < 19.1):
            BMILevel = "Underweight"
        elif (BMI >= 19.1) and (BMI < 25.8):
            BMILevel = "Normal weight"
        elif (BMI >= 25.8) and (BMI < 27.3):
            BMILevel = "Marginally overweight"
        elif (BMI >= 27.3) and (BMI < 32.3):
            BMILevel = "Overweight"
        elif (BMI >= 32.3) and (BMI < 40):
            BMILevel = "Obese"
        elif (BMI >= 40):
            BMILevel = "Extreme obesity"
    
    # printing
    print "Input data:\n\nAge: %0.2f\nGender: %s\nHeight: %0.2f\nWeight: %0.2f\nBody position: %s\nClothing: %s\nAcclimated: %s\nMetabolic rate: %0.2f\nActivity duration: %0.2f" % (age, gender, heightCM, weight, bodyPosition, clothingInsulation, acclimated, metabolicRate, activityDuration)
    
    bodyCharacteristics = [age, gender, heightCM, weight, bodyPosition, clothingInsulation, acclimated, metabolicRate, activityDuration]
    validInputData = True
    printMsg = "ok"
    
    return BMR, BMI, BMILevel, bodyCharacteristics, validInputData, printMsg


level = gh.GH_RuntimeMessageLevel.Warning
if sc.sticky.has_key("ladybug_release"):
    if sc.sticky["ladybug_release"].isCompatible(ghenv.Component):
        
        BMR, BMI, BMILevel, bodyCharacteristics, validInputData, printMsg = main(age_, gender_, height_, weight_, bodyPosition_, clothingInsulation_, acclimated_, metabolicRate_, activityDuration_)
        if not validInputData:
            print printMsg
            ghenv.Component.AddRuntimeMessage(level, printMsg)
    else:
        printMsg = "You need a newer version of Ladybug to use this component." + \
            "Use updateLadybug component to update userObjects.\n" + \
            "If you have already updated userObjects drag the Ladybug_Ladybug component " + \
            "into the canvas and try again."
        print printMsg
else:
    printMsg = "First please let the Ladybug fly..."
    print printMsg
    ghenv.Component.AddRuntimeMessage(level, printMsg)