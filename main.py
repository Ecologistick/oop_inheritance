class Eggs:
  eggs = 0
  
  def eat(self, food):
    self.weight += food
    self.eggs += food // 2
  
  def colect(self):
    print('Собрано', self.eggs, 'яиц')
    self.eggs = 0

class Milk:
  milk = 0
  
  def eat(self, food):
    self.weight += food
    self.milk += food // 2
  
  def colect(self):
    print('Собрано', self.milk, 'литров молока')
    self.milk = 0

class Wool:
  wool = 0

  def eat(self, food):
    self.weight += food
    self.wool += food // 2
  
  def colect(self):
    print('Собрано', self.wool, 'килограммов шерсти')
    self.wool = 0


class Goose(Eggs):
  voice = 'Гуси гогочут' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def song(self):
    print(self.voice)

class Cow(Milk):
  voice = 'Коровы мычат' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def song(self):
    print(self.voice)

class Sheep(Wool):
  voice = 'Овцы блеют' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def song(self):
    print(self.voice)

class Chicken(Eggs):
  voice = 'Курица кудахчет' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def song(self):
    print(self.voice)

class Goat(Milk):
  voice = 'Козы блеют' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def song(self):
    print(self.voice)

class Duck(Eggs):
  voice = 'Утка крякает' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def song(self):
    print(self.voice)

white = Goose('Белый', 3)
gray = Goose('Серый', 4)
manka = Cow('Манька', 400)
lamb = Sheep('Барашек', 100)
curly = Sheep('Кудрявый', 90)
coco = Chicken('Ко-ко', 2)
kuka = Chicken('Кукареку', 1)
horns = Goat('Рога', 70)
hooves = Goat('Копыта', 90)
mallard = Duck('Кряква', 1)

animals =(white, gray, manka, lamb, curly, coco, kuka, horns, hooves, mallard)

max = 0
name_max = ''
for animal in animals:
  if animal.weight > max:
    max = animal.weight
    name_max = animal.name
print(name_max)

total_weight = 0
for animal in animals:
  total_weight += animal.weight
print('Общий вес всех животных', total_weight)