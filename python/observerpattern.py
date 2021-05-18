from abc import ABCMeta, abstractmethod

class Subject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def register_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class Observer:

    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

    @abstractmethod
    def register_subject(self, subject):
        pass


class weejiwon(Subject):
    def __init__(self):
        super(weejiwon, self).__init__()
        self._observer_list = []
        self.happiness = 0
        self.sadness = 0

    def register_observer(self, observer):
        if observer in self._observer_list:
            return "Already exist observer!"
        
        self._observer_list.append(observer)
        return "Success register!"

    def remove_observer(self, observer):
        if observer in self._observer_list:
            _observer_list.remove(observer)
            return "Success remove!"

        return "observer does not exist."

    def notify_observers(self): #옵저버에게 알리는 부분 (옵저버리스트에 있는 모든 옵저버들의 업데이트 메서드 실행)
        for observer in self._observer_list:
            observer.update(self.happiness,self.sadness)

    def emotionalChanged(self):
        self.notify_observers() #감정이 변하면 옵저버에게 알립니다.

    def set_emotional(self, happiness,sadness):
        self.happiness=happiness
        self.sadness=sadness
        self.emotionalChanged()

class Emotion(Observer):
    def update(self, happiness,sadness): #업데이트 메서드가 실행되면 변화된 감정내용을 화면에 출력해줍니다
        self.happiness=happiness
        self.sadness=sadness
        self.display()

    def register_subject(self, subject):
        self.subject = subject
        self.subject.register_observer(self)

    def display(self):
        print ('weejiwon Emotion happiness:',self.happiness,' sadness:',self.sadness)

def test():
    weejiwonObj = weejiwon()
    EmotionObj=Emotion()
    EmotionObj.register_subject(weejiwonObj)


    weejiwonObj.set_emotional('good','good')
    weejiwonObj.set_emotional('Not good','Not good')
    weejiwonObj.set_emotional('Bad','Bad')

if __name__ == '__main__':
    test()
