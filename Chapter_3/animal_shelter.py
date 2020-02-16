from class_list_node import ListNode

class Animal:
    def __init__(self, animal, arrival):
        self.animal = animal
        self.arrival = arrival

class AnimalShelter:

    def __init__(self):
        self.first = None
        self.end = None

    def enqueue(self, animal, arrival):
        new_node = ListNode(Animal(animal, arrival))
        if self.end:
            self.end.next = new_node
        self.end = new_node
        if not self.first:
            self.first = self.end

    def dequeue_any(self):
        if not self.first:
            return None
        output = self.first.item
        self.first = self.first.next
        if not self.first:
            self.end = self.first
        return output

    def dequeue_dog(self):
        return self.__dequeue_animal("dog")

    def dequeue_cat(self):
        return self.__dequeue_animal("cat")

    def __dequeue_animal(self, animal):
        if not self.first:
            return None

        if self.first.item.animal == animal:
            return self.dequeue_any()

        pointer = self.first
        while pointer.next:
            if pointer.next.item.animal == animal:
                output = pointer.next.item
                pointer.next = pointer.next.next
                if not pointer.next:
                    self.end = pointer
                return output
            pointer = pointer.next
        return None

if __name__ == "__main__":
    # TEST
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("dog", "800")
    animal_shelter.enqueue("cat", "830")
    animal_shelter.enqueue("cat", "900")
    animal_shelter.enqueue("cat", "1000")
    animal_shelter.enqueue("dog", "1030")

    a1 = animal_shelter.dequeue_cat()
    a2 = animal_shelter.dequeue_any()
    a3 = animal_shelter.dequeue_dog()
    a4 = animal_shelter.dequeue_any()
    a5 = animal_shelter.dequeue_cat()

    print(a1.animal, " : ", a1.arrival)
    print(a2.animal, " : ", a2.arrival)
    print(a3.animal, " : ", a3.arrival)
    print(a4.animal, " : ", a4.arrival)
    print(a5.animal, " : ", a5.arrival)