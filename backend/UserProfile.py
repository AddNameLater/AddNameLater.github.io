class UserProfile:

    foodList = []
    totalCalories = 0
    totalProtein = 0
    totalCarbs = 0
    totalFat = 0

    def __init__(self, userName, password, firstName, lastName, accountNum):
        self.userName = userName
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.accountNum = accountNum

    def getAccountNum():
        return accountNum

    def setHeight(self, height):
        self.height = height

    def getHeight():
        return height
    
    def setAge(self, age):
        self.age = age

    def getAge():
        return age

    def setSex(self, isMale):
        self.isMale = isMale

    def getSex():
        return isMale

    def setWeight(self, weight):
        self.weight = weight

    def getWeight():
        return weight

    def setNotePadID(self, noteID):
        self.noteID = noteID

    def getNotePadID(self):
        return self.noteID
    
    def setExerciseLevel(self, exerciseLevel):
        self.exerciseLevel = exerciseLevel

    def displayUserName(self):
        print(self.userName)

    def setCalories(self, calories):
        self.calories = calories

    def getCalories(self):
        return self.calories

    def getTotalCalories(self):
        self.totalCalories = self.totalCalories + self.getCalories
        return self.totalCalories

    def setProtein(self, protein):
        self.protein = protein

    def getProtein(self):
        return self.protein

    def getTotalProtein(self):
        self.totalProtein = self.totalProtein + self.getProtein
        return self.totalProtein

    def setCarbs(self, carbs):
        self.carbs = carbs

    def getCarbs(self):
        return self.carbs

    def getTotalCarbs(self):
        self.totalCarbs = self.totalCarbs + self.getCarbs
        return self.totalCarbs

    def setFat(self, fat):
        self.fat = fat

    def getFat(self):
        return self.fat

    def getTotalFat(self):
        self.totalFat = self.totalFat + self.getFat
        return self.totalFat

