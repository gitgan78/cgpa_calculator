name=input("Your name: ")





class subs():
    def __init__(self,cred,grade,gp=None):
        self.cred=cred
        self.grade=grade
        self.gp=gp
        
        if self.grade=='NA':
            self.gp=0.0
        elif self.grade=='A':
            self.gp=4.0
        elif self.grade=='A-':
            self.gp=3.67
        elif self.grade=='B+':
            self.gp=3.33
        elif self.grade=='B':
            self.gp=3.0
        elif self.grade=='B-':
            self.gp=2.67
        elif self.grade=='C+':
            self.gp=2.33
        elif self.grade=='C':
            self.gp=2.0
        elif self.grade=='D':
            self.gp=1.0
        elif self.grade=='F':
            self.gp=0.0
        else:
            print("Invalid input, run the cell again!")
            
ooo=[]

print("Sem 1")
print("------------------------")

mechanics_grade=input("Mechanics grade: ")
ooo.append(subs(4,mechanics_grade))

mechanics_lab_grade=input("Mechanics lab grade: ")
ooo.append(subs(2,mechanics_lab_grade))

basic_chemistry_grade=input("Basic Chemistry grade: ")
ooo.append(subs(4,basic_chemistry_grade))

chemistry_practicals_1_grade=input("Chemistry practicals 1 grade: ")
ooo.append(subs(2,chemistry_practicals_1_grade))

differential_calculus_grade=input("Differential Calculus grade: ")
ooo.append(subs(4,differential_calculus_grade))

differential_calculus_maxima_grade=input("Differential Calculus using Maxima grade: ")
ooo.append(subs(2,differential_calculus_maxima_grade))

english_grade1=input("English grade: ")
ooo.append(subs(3,english_grade1))

language_grade1=input("Kannada/Add Eng/Sanskrit/Hindi/Tamil/French grade: ")
ooo.append(subs(3,language_grade1))

elective_credit1=float(input("Elective cred: (No elective? type 0)"))
if float(elective_credit1==0):
    elective_grade1='NA'
else:
    elective_grade1=input("Elective grade: ")
ooo.append(subs(elective_credit1,elective_grade1))

print("------------------")

print("Sem 2")
print("--------------------")

electricity_n_magnetism_grade=input("Electricity and Magnetism grade: ")
ooo.append(subs(4,electricity_n_magnetism_grade))

electricity_n_magnetism_lab_grade=input(" Electricity and Magnetism lab: ")
ooo.append(subs(2,electricity_n_magnetism_lab_grade))

phy_n_org_chem_1_grade=input("Enter Physical and Organic Chemistry grade: ")
ooo.append(subs(4,phy_n_org_chem_1_grade))

chemistry_practicals_2_grade=input("Enter Chemistry Practicals 2 grade: ")
ooo.append(subs(2,chemistry_practicals_2_grade))

differential_eqns_grade=input("Enter Differential Equations grade: ")
ooo.append(subs(4,differential_eqns_grade))

diff_eqn_maxima_grade=input("Differential equations using Maxima grade: ")
ooo.append(subs(2,diff_eqn_maxima_grade))

english_grade2=input("English grade: ")
ooo.append(subs(3,english_grade2))

language_grade2=input("Kannada/Add Eng/Sanskrit/Hindi/Tamil/French grade: ")
ooo.append(subs(3,language_grade2))

envi_grade=input("Environmental Studies grade: ")
ooo.append(subs(2,envi_grade))

holistic_edu_grade2=input("Holistic Education grade: ")
ooo.append(subs(2,holistic_edu_grade2))

elective_credit2=float(input("Elective cred: (No elective? type 0)"))
if float(elective_credit2==0):
    elective_grade2='NA'
else:
    elective_grade2=input("Elective grade: ")
ooo.append(subs(elective_credit2,elective_grade2))


print("---------------------------")

print("Sem 3")
print("----------------------")

thermal_phy_grade=input("Thermal Physics and Statistical Mechanics grade: ")
ooo.append(subs(4,thermal_phy_grade))

phy_lab_3_grade=input("Physics Lab 3 grade: ")
ooo.append(subs(2,phy_lab_3_grade))

phy_n_org_chem_2_grade=input("Enter Physical and Organic Chemistry 2 grade: ")
ooo.append(subs(4,phy_n_org_chem_2_grade))

chem_practicals_3_grade=input("Chemistry Practicals 3 grade: ")
ooo.append(subs(2,chem_practicals_3_grade))

real_analysis=input("Real analysis grade: ")
ooo.append(subs(4,real_analysis))

intro_python=input("Introduction to Python programming for mathematics grade: ")
ooo.append(subs(2,intro_python))

english_grade3=input("English grade: ")
ooo.append(subs(3,english_grade3))

language_grade3=input("Kannada/Add Eng/Sanskrit/Hindi/Tamil/French grade: ")
ooo.append(subs(3,language_grade3))

elective_credit3=float(input("Elective cred: (No elective? type 0)"))
if float(elective_credit3==0):
    elective_grade3='NA'
else:
    elective_grade3=input("Elective grade: ")
ooo.append(subs(elective_credit3,elective_grade3))

print("-------------------------------")


print("Sem 4")
print("-------------------")

waves_n_opt_grade=input("Waves and optics grade: ")
ooo.append(subs(4,waves_n_opt_grade))

phy_lab_4_grade=input("Physics Lab 4 grade: ")
ooo.append(subs(2,phy_lab_4_grade))

inorg_n_phy_grade=input("Inorganic and Physical Chemistry grade: ")
ooo.append(subs(4,inorg_n_phy_grade))

chem_practicals_4_grade=input("Chemistry Practicals 4 grade: ")
ooo.append(subs(2,chem_practicals_4_grade))

algebra_grade=input("Algebra grade: ")
ooo.append(subs(4,algebra_grade))

intro_math_mod_grade=input("Introduction to Mathematical Modelling using Python grade: ")
ooo.append(subs(2,intro_math_mod_grade))

english_grade4=input("English grade: ")
ooo.append(subs(3,english_grade4))

language_grade4=input("Kannada/Add Eng/Sanskrit/Hindi/Tamil/French grade: ")
ooo.append(subs(3,language_grade4))

holistic_edu_grade4=input("Holistic Education grade: ")
ooo.append(subs(2,holistic_edu_grade4))

elective_credit4=float(input("Elective cred: (No elective? type 0)"))
if float(elective_credit4==0):
    elective_grade4='NA'
else:
    elective_grade4=input("Elective grade: ")
ooo.append(subs(elective_credit4,elective_grade4))

print("------------------------------------")


print("Sem 5")
print("--------------------")


modern_phy_1_grade=input("Modern Physics grade: ")
ooo.append(subs(3,modern_phy_1_grade))

modern_phy_1_lab_grade=input("Modern Physics Lab 1 grade: ")
ooo.append(subs(2,modern_phy_1_lab_grade))

spectro_grade=input("Spectroscopy grade: ")
ooo.append(subs(3,spectro_grade))

chem_practicals_5_grade=input("Chemistry Practicals 5 Spectroscopy grade: ")
ooo.append(subs(2,chem_practicals_5_grade))

lin_algebra_grade=input("Linear Algebra grade: ")
ooo.append(subs(3,lin_algebra_grade))

lin_alg_python_grade=input("Linear Algebra using Python grade: ")
ooo.append(subs(2,lin_alg_python_grade))

phy_elect_grade=input("Astro/Electronics/Renewable grade: ")
ooo.append(subs(3,phy_elect_grade))

phy_elect_lab_grade=input("Astro/Electronics/Renewable Lab grade: ")
ooo.append(subs(2,phy_elect_lab_grade))

chem_elect_grade=input("Inorgnic materials of Industrial importance/Organic Chemistry grade: ")
ooo.append(subs(3,chem_elect_grade))


chem_elect_lab_grade=input("Inorganic Chemistry/Organic Chemistry Practicals lab grade: ")
ooo.append(subs(2,chem_elect_lab_grade))


maths_elect_grade=input("Integral Transforms/Mathematical Modelling/Graph theory/Calculus/Operations Research grade: ")
ooo.append(subs(3,maths_elect_grade))

maths_elect_lab_grade=input("Integral Transforms/Mathematical Modelling/Graph theory/Calculus/Operations Research lab grade: ")
ooo.append(subs(2,maths_elect_lab_grade))

elective_credit5=float(input("Elective cred: (No elective? type 0)"))
if float(elective_credit5==0):
    elective_grade5='NA'
else:
    elective_grade5=input("Elective grade: ")
ooo.append(subs(elective_credit5,elective_grade5))

print("-------------")
print("Thank you", name)
print("Calculating CGPA of 5 semesters....")


numerator=[]
denominator=[]

for i in ooo:
    numerator.append(i.cred*i.gp)
    denominator.append(i.cred)

print("Dear",name,"your CGPA of 5 semesters is", sum(numerator)/sum(denominator))








    
       



